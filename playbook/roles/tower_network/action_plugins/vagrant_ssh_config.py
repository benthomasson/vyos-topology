from ansible.plugins.action import ActionBase

import subprocess


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        output_file = self._task.args.get('output', None)
        with open(output_file, 'w') as f:
            f.write(subprocess.check_output('vagrant ssh-config', shell=True))
        return result
