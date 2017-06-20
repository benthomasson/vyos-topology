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
        nat_port = self._task.args.get('nat_port', None)
        port = self._task.args.get('port', None)
        host = self._task.args.get('host', None)

        ssh_config = paramiko.config.SSHConfig()
        with open(ssh_config_file) as f:
            ssh_config.parse(f)

        with open(input_file) as f:
            data = yaml.load(f.read())

        for device in data['devices']:
            if device['name'] != host:
                continue
            device_data = ssh_config.lookup(device['name'])
            nats = device.get('nats', [])
            device['nats'] = nats
            nat = dict()
            nats.append(nat)
            nat['ip'] = device_data['hostname']
            nat['port'] = int(port)
            nat['nat_ip'] = str(nat_ip)
            nat['nat_port'] = int(nat_port)

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
