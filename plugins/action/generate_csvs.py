from ansible.plugins.action import ActionBase

import yaml
import csv


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        data = self._task.args.get('data', None)

        with open(data) as f:
            data = yaml.load(f.read())

        with open('devices.csv', 'w') as f:
            devices_csv = csv.DictWriter(f, fieldnames=['device', 'mgmt_ip', 'mgmt_port'])
            devices_csv.writeheader()
            for device in data['devices']:
                devices_csv.writerow(dict(device=device['name'],
                                          mgmt_ip=device.get('mgmt_ip', ''),
                                          mgmt_port=device.get('mgmt_port', '')))

        with open('interfaces.csv', 'w') as f:
            devices_csv = csv.DictWriter(f, fieldnames=['device', 'interface', 'ip_address'])
            devices_csv.writeheader()
            for device in data['devices']:
                for interface in device['interfaces']:
                    devices_csv.writerow(dict(device=device['name'],
                                              interface=interface['name'],
                                              ip_address=interface.get('ip_address', '')))

        
        return result
