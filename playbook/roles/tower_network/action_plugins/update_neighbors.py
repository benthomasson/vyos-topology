
from ansible.plugins.action import ActionBase

import requests
import os
import yaml
import json
from collections import namedtuple
from pprint import pprint
import itertools

Link = namedtuple('Link', ['to_device',
                           'from_device',
                           'to_interface',
                           'from_interface',
                           'link_id',
                           'id',
                           'name'])


def unpaginate(server, url, verify, auth, filter_data):
    results = []
    while url is not None:
        url = "{0}{1}".format(server, url)
        data = requests.get(url, verify=verify, auth=auth, params=filter_data).json()
        results.extend(data.get('results', []))
        url = data.get('next', None)
    return results


def create_interface(server, verify, auth, device, id, name):
        url = server + '/api/v2/canvas/interface/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(device=device,
                                                           name=name,
                                                           id=id,
                                                           )),
                                 verify=verify,
                                 auth=auth,
                                 headers=headers)
        return response.json()


def create_link(server, verify, auth, from_device, to_device, from_interface, to_interface, id, name):
        url = server + '/api/v2/canvas/link/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(from_device=from_device,
                                                           to_device=to_device,
                                                           from_interface=from_interface,
                                                           to_interface=to_interface,
                                                           id=id,
                                                           name=name,
                                                           )),
                                 verify=verify,
                                 auth=auth,
                                 headers=headers)
        return response.json()


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        server = self._task.args.get('server',
                                     "{0}:{1}".format(self._play_context.remote_addr,
                                                      self._play_context.port))
        user = self._task.args.get('user', self._play_context.remote_user)
        password = self._task.args.get('password', self._play_context.password)

        host_facts_dir = self._task.args.get('host_facts', 'host_facts')
        inventory_id = self._task.args.get('inventory_id', None)

        url = '/api/v2/inventories/' + str(inventory_id) + '/hosts'
        hosts = unpaginate(server, url, verify=False, auth=(user, password), filter_data={})

        url = server + '/api/v2/canvas/topologyinventory/'
        filter_data = dict(inventory_id=inventory_id)
        topology_results = requests.get(url, verify=False, auth=(user, password), params=filter_data).json()

        print (topology_results)

        if len(topology_results['results']) == 1:
            topology_id = (topology_results['results'][0]['topology'])
        else:
            raise Exception("{0} topologies found".format(len(topology_results['results'])))

        print (topology_id)

        url = '/api/v2/canvas/device/'
        filter_data = dict(topology_id=topology_id)
        devices = unpaginate(server, url, verify=False, auth=(user, password), filter_data=filter_data)
        device_map_by_name = {x['name']: x for x in devices}
        device_map_by_id = {x['device_id']: x for x in devices}

        print (devices)

        for device in devices:
            url = '/api/v2/canvas/interface/'
            filter_data = dict(device_id=device['device_id'])
            interfaces = unpaginate(server, url, verify=False, auth=(user, password), filter_data=filter_data)
            device['interfaces'] = interfaces
            device['interfaces_map_by_name'] = {x['name']: x for x in interfaces}
            device['interfaces_map_by_id'] = {x['interface_id']: x for x in interfaces}
            if not interfaces:
                device['interface_id_seq'] = itertools.count(1)
            else:
                device['interface_id_seq'] = itertools.count(max([interface['interface_id'] for interface in interfaces]))
            print (interfaces)

        pprint(device_map_by_name)
        pprint(device_map_by_id)
        links = set()

        for device in devices:
            url = '/api/v2/canvas/link/'
            filter_data = dict(from_device=device['device_id'])
            links.update([Link(**x) for x in unpaginate(server, url, verify=False, auth=(user, password), filter_data=filter_data)])

        print (links)
        links_map_by_from_device_id_interface_id = {(x.from_device, x.from_interface): x for x in links}
        links_map_by_to_device_id_interface_id = {(x.to_device, x.to_interface): x for x in links}
        if not links:
            link_id_seq = itertools.count(1)
        else:
            link_id_seq = itertools.count(max([link.id for link in links]))

        for host in hosts:
            if os.path.exists(os.path.join(host_facts_dir, host['name'])):
                with open(os.path.join(host_facts_dir, host['name'])) as f:
                    print host['name']
                    if not host['name'] in device_map_by_name:
                        print ("Did not find {0} on canvas".format(host['name']))
                        continue
                    host_facts = yaml.load(f.read())
                    local_device = device_map_by_name[host['name']]
                    print host_facts
                    for interface_name, neighbor_details in host_facts.get('ansible_net_neighbors', []).iteritems():
                        print interface_name, neighbor_details
                        if interface_name not in local_device['interfaces_map_by_name']:
                            new_interface = create_interface(server,
                                                             False,
                                                             (user, password),
                                                             local_device['device_id'],
                                                             next(local_device['interface_id_seq']),
                                                             interface_name)
                            local_device['interfaces_map_by_id'][new_interface['interface_id']] = new_interface
                            local_device['interfaces_map_by_name'][new_interface['name']] = new_interface
                        local_interface = local_device['interfaces_map_by_name'][interface_name]
                        print(local_interface)
                        for remote_neighbor in neighbor_details:
                            if (local_device['device_id'], local_interface['interface_id']) in links_map_by_from_device_id_interface_id:
                                print ("Found link!")
                            elif (local_device['device_id'], local_interface['interface_id']) in links_map_by_to_device_id_interface_id:
                                print ("Found link!")
                            else:
                                if remote_neighbor['host'] in device_map_by_name:
                                    remote_device = device_map_by_name[remote_neighbor['host']]
                                    if not remote_neighbor['port'] in remote_device['interfaces_map_by_name']:
                                        new_interface = create_interface(server,
                                                                         False,
                                                                         (user, password),
                                                                         remote_device['device_id'],
                                                                         next(remote_device['interface_id_seq']),
                                                                         remote_neighbor['port'])
                                        remote_device['interfaces_map_by_id'][new_interface['interface_id']] = new_interface
                                        remote_device['interfaces_map_by_name'][new_interface['name']] = new_interface
                                    remote_interface = remote_device['interfaces_map_by_name'][remote_neighbor['port']]
                                    new_link = create_link(server,
                                                           False,
                                                           (user, password),
                                                           local_device['device_id'],
                                                           remote_device['device_id'],
                                                           local_interface['interface_id'],
                                                           remote_interface['interface_id'],
                                                           next(link_id_seq),
                                                           "x")
                                    new_link = Link(**new_link)
                                    links.add(new_link)
                                    links_map_by_from_device_id_interface_id[(local_device['device_id'], local_interface['interface_id'])] = new_link
                                    links_map_by_to_device_id_interface_id[(remote_device['device_id'], remote_interface['interface_id'])] = new_link
        return result
