#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    generate_host_vars [options] <data> <host-vars-directory>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import yaml
import os

logger = logging.getLogger('generate_host_vars')


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

    host_vars_directory = os.path.abspath(parsed_args['<host-vars-directory>'])

    with open(parsed_args['<data>']) as f:
        data = yaml.load(f.read())

    for device in data['devices']:
        with open(os.path.join(host_vars_directory, device['name']), 'w') as f:
            f.write(yaml.safe_dump(device, default_flow_style=False))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
