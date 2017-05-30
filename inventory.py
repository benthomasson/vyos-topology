#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    inventory [options] --list

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import os
import logging
import sys
import requests
import json
import configparser

logger = logging.getLogger('inventory')


# Ansible API 2.0
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'inventory.ini')
    config.read(config_path)
    server = config.get('network_ui', 'server')
    topology_id = config.get('network_ui', 'topology_id')
    data = requests.get("http://{0}/network_ui/topology_json?topology_id={1}".format(server, topology_id)).json()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader,
                          variable_manager=variable_manager,
                          host_list=config.get('network_ui', 'inventory')
                          )

    inventory_data = {'group': {'hosts': []}, '_meta': {'hostvars': {}}}
    for device in data.get('devices', []):
        inventory_data['group']['hosts'].append(device['name'])

    for section in inventory.get_groups():
        for item in inventory.get_group(section).hosts:
            inventory_data['_meta']['hostvars'][str(item)] = item.serialize()['vars']

    print json.dumps(inventory_data, sort_keys=True, indent=4)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
