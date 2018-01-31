#---- list_interface

from ansible.plugins.action import ActionBase

import requests

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


        interface_id = self._task.args.get('interface_id', None)
        device = self._task.args.get('device', None)
        name = self._task.args.get('name', None)
        id = self._task.args.get('id', None)

        filter_data=dict(interface_id=interface_id,
                         device=device,
                         name=name,
                         id=id,
                         )
        filter_data={x:y for x,y in filter_data.iteritems() if y is not None}

        url = NETWORKING_API + API_VERSION + '/interface/'
        results = []
        while url is not None:
            url = server + url
            data = requests.get(url, verify=False, auth=(user, password), params=filter_data).json()
            results.extend(data.get('results', []))
            url = data.get('next', None)
        result['ansible_facts'] = {var: results}
        return result


