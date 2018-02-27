from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        start = self._task.args.get('start', 0)
        end = self._task.args.get('end', None)
        increment = self._task.args.get('increment', 1)
        var = self._task.args.get('var', None)
        result['ansible_facts'] = {var: range(int(start), int(end), int(increment))}
        return result

