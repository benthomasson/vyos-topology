from ansible.plugins.action import ActionBase

import yaml


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)

        with open(input_file) as f:
            data = yaml.load(f.read())

        for device in data['devices']:
            device['nats'] = []

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
