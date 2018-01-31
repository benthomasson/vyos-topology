#---- create_groupdevice

from ansible.plugins.action import ActionBase

import requests
import json

NETWORKING_API = '/network_ui/api/'
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

        group = self._task.args.get('group', None)
        device = self._task.args.get('device', None)


        url = server + NETWORKING_API + API_VERSION + '/groupdevice/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(group=group,
                                                           device=device,
                                                           )),
                                 verify=False,
                                 auth=(user, password),
                                 headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result





