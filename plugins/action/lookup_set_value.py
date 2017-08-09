from ansible.plugins.action import ActionBase

import yaml


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        lookup_path = self._task.args.get('lookup_path', None)
        set_path = str(self._task.args.get('set_path', None))
        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)

        with open(input_file) as f:
            data = yaml.load(f.read())

        value = None

        print lookup_path
        print lookup_path.split('.')
        for device in data['devices']:
            print device['name'], lookup_path.split('.')[0], device['name'] == lookup_path.split('.')[0]
            if device['name'] == lookup_path.split('.')[0]:
                for interface in device['interfaces']:
                    if interface['name'] == lookup_path.split('.')[1]:
                        value = interface[lookup_path.split('.')[2]]
                        break
                if value:
                    break

        print type(set_path), set_path
        print type(value), value
        data[set_path] = value

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
