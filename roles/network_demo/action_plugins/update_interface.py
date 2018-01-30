#---- update_interface

from ansible.plugins.action import ActionBase

import requests
import json

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

        interface_id = self._task.args.get('interface_id', None)
        device = self._task.args.get('device', None)
        name = self._task.args.get('name', None)
        id = self._task.args.get('id', None)

        url = server + NETWORKING_API + API_VERSION + '/interface/' + str(interface_id) + '/'
        headers = {'content-type': 'application/json'}
        data=dict(device=device,
                  name=name,
                  id=id,
                  )
        data={x:y for x,y in data.iteritems() if y is not None}
        response = requests.patch(url,
                                  data=json.dumps(data),
                                  verify=False,
                                  auth=(user, password),
                                  headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result


