from ansible.plugins.action import ActionBase

import requests


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        output = self._task.args.get('output', None)
        url = self._task.args.get('url', None)
        with open(output, 'w') as f:
            f.write(requests.get(url).text)
        return result
