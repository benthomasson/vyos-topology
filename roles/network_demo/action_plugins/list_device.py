from ansible.plugins.action import ActionBase

import requests
from pprint import pprint

NETWORKING_API = 'network_ui/api/'
API_VERSION = 'v1'


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        server = self._task.args.get('server', None)
        user = self._task.args.get('user', None)
        password = self._task.args.get('password', None)
        var = self._task.args.get('var', None)
        url = server + NETWORKING_API + API_VERSION + '/device/'
        data = requests.get(url, verify=False, auth=(user, password)).json()
        result['ansible_facts'] = {var: data}
        return result

