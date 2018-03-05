from ansible.plugins.action import ActionBase

import jinja2
import yaml


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        template = self._task.args.get('template', None)
        context = self._task.args.get('context', None)
        with open(context) as f:
            context = yaml.load(f.read())
        with open(template) as f:
            template = f.read()
        output = self._task.args.get('output', None)
        with open(output, 'w') as f:
            f.write(jinja2.Template(template).render(**context))
        return result
