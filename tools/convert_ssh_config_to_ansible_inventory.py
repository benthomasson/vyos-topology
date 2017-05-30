#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    convert_ssh_config_to_ansible_inventory [options] <ssh-config> <output-file>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import paramiko.config

logger = logging.getLogger('convert_ssh_config_to_ansible_inventory')


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

    ssh_config = paramiko.config.SSHConfig()
    with open(parsed_args['<ssh-config>']) as f:
        ssh_config.parse(f)

    with open(parsed_args['<output-file>'], 'w') as f:
        f.write("[hosts]\n")
        for name in ssh_config.get_hostnames():
            if name != '*':
                data = ssh_config.lookup(name)
                f.write(" ".join([name] +
                                 ["=".join(x) for x in [["ansible_host", data['hostname']],
                                                        ["ansible_port", data['port']],
                                                        ["ansible_user", data['user']],
                                                        ["ansible_ssh_private_key_file", data['identityfile'][0]],
                                                        ]]))
                f.write("\n")

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
