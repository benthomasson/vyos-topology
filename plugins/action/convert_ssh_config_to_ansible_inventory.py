from ansible.plugins.action import ActionBase

import paramiko.config


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        ssh_config = paramiko.config.SSHConfig()
        ssh_config_file = self._task.args.get('ssh_config', None)
        output_file = self._task.args.get('output', None)
        with open(ssh_config_file) as f:
            ssh_config.parse(f)

        with open(output_file, 'w') as f:
            f.write("[hosts]\n")
            for name in ssh_config.get_hostnames():
                if name != '*':
                    data = ssh_config.lookup(name)
                    f.write(" ".join([name] +
                                     ["=".join(x) for x in [["ansible_host", data['hostname']],
                                                            ["ansible_port", data['port']],
                                                            ["ansible_user", data['user']],
                                                            ["ansible_ssh_private_key_file", data['identityfile'][0]],
                                                            ]]))
                    f.write("\n")

        return result
