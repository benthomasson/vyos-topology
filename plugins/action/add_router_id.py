from ansible.plugins.action import ActionBase

import yaml
from netaddr import IPNetwork


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        input_file = self._task.args.get('input', None)
        output_file = self._task.args.get('output', None)
        router_id_range = self._task.args.get('router_id_range', None)

        router_ids = IPNetwork(router_id_range)

        with open(input_file) as f:
            data = yaml.load(f.read())

        for device, ip_address in zip(data['devices'], router_ids[1:]):
            device['router_id'] = str(ip_address)

        with open(output_file, 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))
        return result
