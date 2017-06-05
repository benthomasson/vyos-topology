from ansible.plugins.action import ActionBase

import yaml
import os


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        host_vars_directory = self._task.args.get('host_vars_directory', None)
        data = self._task.args.get('data', None)

        with open(data) as f:
            data = yaml.load(f.read())

        if not os.path.exists(host_vars_directory):
            os.makedirs(host_vars_directory)

        for device in data['devices']:
            with open(os.path.join(host_vars_directory, device['name']), 'w') as f:
                f.write(yaml.safe_dump(device, default_flow_style=False))
        return result
