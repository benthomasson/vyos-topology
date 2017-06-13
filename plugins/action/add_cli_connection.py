from ansible.plugins.action import ActionBase

import yaml
import paramiko.config


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)
        ssh_config = paramiko.config.SSHConfig()
        ssh_config_file = self._task.args.get('ssh_config', None)
        use_nat = self._task.args.get('use_nat', False)
        ssh_key = self._task.args.get('ssh_key', '')

        with open(ssh_config_file) as f:
            ssh_config.parse(f)

        with open(input_file) as f:
            data = yaml.load(f.read())

        for device in data['devices']:
            host_data = ssh_config.lookup(device['name'])
            if use_nat:
                device['cli'] = dict(host=device['nat_ip'],
                                     port=device['nat_port'],
                                     ssh_keyfile=str(ssh_key),
                                     transport='cli',
                                     username=host_data['user'])

            else:
                device['cli'] = dict(host=host_data['hostname'],
                                     port=int(host_data['port']),
                                     username=host_data['user'],
                                     ssh_keyfile=str(ssh_key) or host_data['identityfile'][0],
                                     transport='cli')

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))

        return result
