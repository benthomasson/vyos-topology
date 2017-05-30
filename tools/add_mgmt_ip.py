#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    add_mgmt_ip [options] <ssh-config> <input> <output>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import yaml
import paramiko.config
import itertools

logger = logging.getLogger('add_mgmt_ip')

NAT_IP = '10.17.161.200'


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

    port_range = itertools.count(10000)

    ssh_config = paramiko.config.SSHConfig()
    with open(parsed_args['<ssh-config>']) as f:
        ssh_config.parse(f)

    with open(parsed_args['<input>']) as f:
        data = yaml.load(f.read())

    for device in data['devices']:
        device_data = ssh_config.lookup(device['name'])
        device['mgmt_ip'] = device_data['hostname']
        device['mgmt_port'] = int(device_data['port'])
        device['nat_ip'] = NAT_IP
        device['nat_port'] = next(port_range)

    with open(parsed_args['<output>'], 'w') as f:
        f.write(yaml.safe_dump(data, default_flow_style=False))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
