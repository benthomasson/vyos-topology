#---- create_device

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

        topology = self._task.args.get('topology', None)
        name = self._task.args.get('name', None)
        x = self._task.args.get('x', None)
        y = self._task.args.get('y', None)
        id = self._task.args.get('id', None)
        type = self._task.args.get('type', None)

        interface_id_seq = self._task.args.get('interface_id_seq', 0)
        process_id_seq = self._task.args.get('process_id_seq', 0)
        host_id = self._task.args.get('host_id', 0)

        url = server + NETWORKING_API + API_VERSION + '/device/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(topology=topology,
                                                           name=name,
                                                           x=x,
                                                           y=y,
                                                           id=id,
                                                           type=type,
                                                           interface_id_seq=interface_id_seq,
                                                           process_id_seq=process_id_seq,
                                                           host_id=host_id,
                                                           )),
                                 verify=False,
                                 auth=(user, password),
                                 headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result


