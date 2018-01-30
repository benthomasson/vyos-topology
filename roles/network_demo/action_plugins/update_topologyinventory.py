#---- update_topologyinventory

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

        topology_inventory_id = self._task.args.get('topology_inventory_id', None)
        topology = self._task.args.get('topology', None)
        inventory_id = self._task.args.get('inventory_id', None)

        url = server + NETWORKING_API + API_VERSION + '/topologyinventory/' + str(topology_inventory_id) + '/'
        headers = {'content-type': 'application/json'}
        data=dict(topology=topology,
                  inventory_id=inventory_id,
                  )
        data={x:y for x,y in data.iteritems() if y is not None}
        response = requests.patch(url,
                                  data=json.dumps(data),
                                  verify=False,
                                  auth=(user, password),
                                  headers=headers)
        result['ansible_facts'] = {var: response.json()}
        return result










