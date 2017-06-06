from ansible.plugins.action import ActionBase

import yaml
from netaddr import IPNetwork


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        supernet = self._task.args.get('supernet', None)
        subnet_size = int(self._task.args.get('subnet_size', 30))
        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)

        with open(input_file) as f:
            data = yaml.load(f.read())

        net = IPNetwork(supernet)
        subnets = net.subnet(subnet_size)

        device_interfaces = dict()

        for device in data['devices']:
            for interface in device['interfaces']:
                device_interfaces[(device['id'], interface['id'])] = interface

        for link in data['links']:
            subnet = next(subnets)
            link['subnet'] = str(subnet.network)
            link['subnet_prefixlen'] = subnet.prefixlen
            device_interfaces[(link['from_device_id'], link['from_interface_id'])]['ip_address'] = str(subnet[1])
            device_interfaces[(link['from_device_id'], link['from_interface_id'])]['netmask'] = str(net.netmask)
            device_interfaces[(link['from_device_id'], link['from_interface_id'])]['subnet_prefixlen'] = subnet_size
            device_interfaces[(link['from_device_id'], link['from_interface_id'])]['remote_ip_address'] = str(subnet[2])
            device_interfaces[(link['to_device_id'], link['to_interface_id'])]['ip_address'] = str(subnet[2])
            device_interfaces[(link['to_device_id'], link['to_interface_id'])]['netmask'] = str(net.netmask)
            device_interfaces[(link['to_device_id'], link['to_interface_id'])]['remote_ip_address'] = str(subnet[1])
            device_interfaces[(link['to_device_id'], link['to_interface_id'])]['subnet_prefixlen'] = subnet_size

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
