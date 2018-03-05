from ansible.plugins.action import ActionBase

import dpath


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        the_list = self._task.args.get('list', 0)
        attribute = self._task.args.get('attribute', None)
        var = self._task.args.get('var', None)
        attribute = attribute.replace('.', '/')
        result['ansible_facts'] = {
            var: [dpath.util.get(x, attribute) for x in the_list]}
        return result
