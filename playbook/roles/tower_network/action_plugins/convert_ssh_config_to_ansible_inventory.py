from ansible.plugins.action import ActionBase

import yaml
import paramiko.config


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        ssh_config = paramiko.config.SSHConfig()
        ssh_config_file = self._task.args.get('ssh_config', None)
        output_file = self._task.args.get('output', None)
        data_file = self._task.args.get('data', None)
        groups = self._task.args.get('groups', '').split(',')
        with open(ssh_config_file) as f:
            ssh_config.parse(f)

        with open(data_file) as f:
            data = yaml.load(f.read())

        devices = {device.get(
            'name'): device for device in data.get('devices', [])}

        with open(output_file, 'w') as f:
            for group in groups:
                group = group.strip()
                f.write("[{0}]\n".format(group))
                for name in ssh_config.get_hostnames():
                    if name == '*':
                        continue
                    if name not in devices:
                        continue
                    if devices[name].get('type') == group:
                        data = ssh_config.lookup(name)
                        f.write(" ".join([name] +
                                         ["=".join(x) for x in [["ansible_host", data['hostname']],
                                                                ["ansible_port",
                                                                    data['port']],
                                                                ["ansible_user",
                                                                    data['user']],
                                                                ["ansible_ssh_private_key_file",
                                                                    data['identityfile'][0]],
                                                                ]]))
                        f.write("\n")

        return result
