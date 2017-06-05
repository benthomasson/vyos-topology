from ansible.plugins.action import ActionBase

import yaml
import itertools
import paramiko.config


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        nat_ip = self._task.args.get('nat_ip', None)
        ssh_config_file = self._task.args.get('ssh_config', None)
        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)
        port_range_start = self._task.args.get('port_range_start', None)

        port_range = itertools.count(int(port_range_start))

        ssh_config = paramiko.config.SSHConfig()
        with open(ssh_config_file) as f:
            ssh_config.parse(f)

        with open(input_file) as f:
            data = yaml.load(f.read())

        for device in data['devices']:
            device_data = ssh_config.lookup(device['name'])
            device['mgmt_ip'] = device_data['hostname']
            device['mgmt_port'] = int(device_data['port'])
            device['nat_ip'] = str(nat_ip)
            device['nat_port'] = next(port_range)

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
