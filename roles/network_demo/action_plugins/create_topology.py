#---- create_topology

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

        name = self._task.args.get('name', None)
        scale = self._task.args.get('scale', None)
        panX = self._task.args.get('panX', None)
        panY = self._task.args.get('panY', None)

        device_id_seq = self._task.args.get('device_id_seq', 0)
        link_id_seq = self._task.args.get('link_id_seq', 0)
        group_id_seq = self._task.args.get('group_id_seq', 0)
        stream_id_seq = self._task.args.get('stream_id_seq', 0)

        url = server + NETWORKING_API + API_VERSION + '/topology/'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(dict(name=name,
                                                           scale=scale,
                                                           panX=panX,
                                                           panY=panY,
                                                           device_id_seq=device_id_seq,
                                                           link_id_seq=link_id_seq,
                                                           group_id_seq=group_id_seq,
                                                           stream_id_seq=stream_id_seq,
                                                           )),
                                 verify=False,
                                 auth=(user, password),
                                 headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result





