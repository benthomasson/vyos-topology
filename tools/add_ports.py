#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    add_ports [options] <input> <output>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import yaml
import itertools

logger = logging.getLogger('add_ports')


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

    with open(parsed_args['<input>']) as f:
        data = yaml.load(f.read())

    port_range = itertools.count(9000)

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

    with open(parsed_args['<output>'], 'w') as f:
        f.write(yaml.safe_dump(data, default_flow_style=False))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

