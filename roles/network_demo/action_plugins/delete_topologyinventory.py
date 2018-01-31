#---- delete_topologyinventory

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

        server = self._task.args.get('server',
                                     "{0}:{1}".format(self._play_context.remote_addr,
                                                      self._play_context.port))
        user = self._task.args.get('user', self._play_context.remote_user)
        password = self._task.args.get('password', self._play_context.password)

        topology_inventory_id = self._task.args.get('topology_inventory_id', None)

        url = server + NETWORKING_API + API_VERSION + '/topologyinventory/' + str(topology_inventory_id) + '/'
        response = requests.delete(url,
                                   verify=False,
                                   auth=(user, password))
        return result
