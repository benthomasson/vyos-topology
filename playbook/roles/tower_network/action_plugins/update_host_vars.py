
from ansible.plugins.action import ActionBase

import requests
import os
import yaml
import json


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        server = self._task.args.get('server',
                                     "{0}:{1}".format(self._play_context.remote_addr,
                                                      self._play_context.port))
        user = self._task.args.get('user', self._play_context.remote_user)
        password = self._task.args.get('password', self._play_context.password)

        inventory_id = self._task.args.get('inventory_id', None)
        host_vars_dir = self._task.args.get('host_vars', 'host_vars')

        url = '/api/v2/inventories/' + str(inventory_id) + '/hosts'
        hosts = []
        while url is not None:
            url = server + url
            data = requests.get(url, verify=False, auth=(user, password)).json()
            hosts.extend(data.get('results', []))
            url = data.get('next', None)
        print ([x['name'] for x in hosts])
        print (os.path.exists(host_vars_dir))
        for host in [x['name'] for x in hosts]:
            print(host, os.path.exists(os.path.join(host_vars_dir, host)))
        for host in hosts:
            if os.path.exists(os.path.join(host_vars_dir, host['name'])):
                url = server + '/api/v2/hosts/' + str(host['id']) + '/variable_data'
                with open(os.path.join(host_vars_dir, host['name'])) as f:
                    data = yaml.load(f)
                headers = {'content-type': 'application/json'}
                data = requests.post(url,
                                     verify=False,
                                     data=json.dumps(data),
                                     auth=(user, password),
                                     headers=headers).json()
                print (data)


        result['ansible_facts'] = {'hosts': hosts}
        return result
