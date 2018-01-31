#---- create_process

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

        server = self._task.args.get('server',
                                     "{0}:{1}".format(self._play_context.remote_addr,
                                                      self._play_context.port))
        user = self._task.args.get('user', self._play_context.remote_user)
        password = self._task.args.get('password', self._play_context.password)

        var = self._task.args.get('var', None)

        device = self._task.args.get('device', None)
        name = self._task.args.get('name', None)
        type = self._task.args.get('type', None)

        id = self._task.args.get('id', 0)

        url = server + NETWORKING_API + API_VERSION + '/process/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(device=device,
                                                           name=name,
                                                           type=type,
                                                           id=id,
                                                           )),
                                 verify=False,
                                 auth=(user, password),
                                 headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result
