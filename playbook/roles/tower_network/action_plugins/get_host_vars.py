#---- update_device

from ansible.plugins.action import ActionBase

import requests
import json


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

        host_id = self._task.args.get('host_id', None)
        var = self._task.args.get('var', None)

        url = server + '/api/v2/hosts/' + str(host_id) + '/variable_data'
        print (url)
        response = requests.get(url,
                                verify=False,
                                auth=(user, password))
        print (response)
        result['ansible_facts'] = {var: response.json()}
        return result
