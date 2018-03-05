from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        p = self._task.args.get('p', None)
        q = self._task.args.get('q', None)
        var = self._task.args.get('var', None)
        result['ansible_facts'] = {var: zip(p, q)}
        return result
