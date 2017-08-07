from ansible.plugins.action import ActionBase

import subprocess
import os


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        command = self._task.args.get('command', None)
        chdir = self._task.args.get('chdir', None)
        cwd = os.getcwd()
        if chdir:
            cwd=os.path.abspath(os.path.join(cwd, chdir))
        subprocess.check_call(command, shell=True, cwd=cwd)
        return result


