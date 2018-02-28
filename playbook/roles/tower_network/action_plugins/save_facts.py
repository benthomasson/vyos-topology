
from ansible.plugins.action import ActionBase

import requests
import os
import yaml
import json
from pprint import pprint

from yaml.dumper import Dumper
from yaml.representer import SafeRepresenter

class KludgeDumper(Dumper):
   pass

KludgeDumper.add_representer(str, SafeRepresenter.represent_str)

KludgeDumper.add_representer(unicode, SafeRepresenter.represent_unicode)


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        host_facts_dir = self._task.args.get('host_facts', 'host_facts')
        facts = self._task.args.get('facts', [])

        if not os.path.exists(host_facts_dir):
            os.makedirs(host_facts_dir)

        data = {}
        for fact in facts:
            data[str(fact)] = json.loads(json.dumps(task_vars[fact]))

        with open(os.path.join(host_facts_dir, task_vars['inventory_hostname_short']), 'w') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False))

        return result
