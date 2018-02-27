from ansible.plugins.action import ActionBase

import yaml
import itertools


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)
        range_start = int(self._task.args.get('range_start', None))

        with open(input_file) as f:
            data = yaml.load(f.read())

        port_range = itertools.count(range_start)

        from_interface_map = dict()
        to_interface_map = dict()

        for link in data['links']:
            link['from_port'] = next(port_range)
            link['to_port'] = next(port_range)
            from_interface_map[(link['from_device'], link['from_interface'])] = (link['from_port'], link['to_port'])
            to_interface_map[(link['to_device'], link['to_interface'])] = (link['to_port'], link['from_port'])

        for device in data['devices']:
            for interface in device['interfaces']:
                key = (device['name'], interface['name'])
                if key in from_interface_map:
                    interface['local_port'] = from_interface_map[key][0]
                    interface['remote_port'] = from_interface_map[key][1]
                if key in to_interface_map:
                    interface['local_port'] = to_interface_map[key][0]
                    interface['remote_port'] = to_interface_map[key][1]

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))

        return result
