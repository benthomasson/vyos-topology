#!/usr/bin/env python
# -*- coding: utf-8 -*-

import websocket
import yaml
import os
from jinja2 import FileSystemLoader, Environment
from subprocess import call, check_call
import paramiko
import traceback
import json

stopped = False

env = Environment(loader=FileSystemLoader('templates'))
host_vars_directory = "host_vars"
group_vars_directory = "group_vars"
ssh_config_file = "ssh-config"
inventory_file = "hosts"


def on_message(ws, json_message):
    # Generate Vagrantfile
    message = json.loads(json_message)
    message_type = message.pop(0)
    topology_id = message.pop(0)

    if message_type == "Deploy":
        on_deploy(ws, topology_id, message.pop(0))

    if message_type == "Discover":
        on_discover(ws, topology_id, message.pop(0))

    if message_type == "Destroy":
        on_destroy(ws, topology_id)


def on_destroy(ws, topology_id):
    check_call("vagrant destroy -f", shell=True)


def on_discover(ws, topology_id, message):
    call("ansible-playbook -i hosts playbook/discover.yml", shell=True)


def on_deploy(ws, topology_id, message):
    with open("Vagrantfile", "w") as f:
        f.write(env.get_template("Vagrantfile.j2").render(yaml.load(message)))

    data = yaml.load(message)
    with open("topology.yml", "w") as f:
        f.write(yaml.safe_dump(data, default_flow_style=False))

    # Write host vars
    for device in data['devices']:
        with open(os.path.join(host_vars_directory, device['name']), 'w') as f:
            f.write(yaml.safe_dump(device, default_flow_style=False))

    # Write group vars
    with open(os.path.join(group_vars_directory, 'hosts'), 'w') as f:
        f.write(yaml.safe_dump(data, default_flow_style=False))

    # Vagrant up
    check_call("vagrant up", shell=True)
    check_call("vagrant ssh-config > ssh-config", shell=True)

    ssh_config = paramiko.config.SSHConfig()
    with open(ssh_config_file) as f:
        ssh_config.parse(f)

    with open(inventory_file, 'w') as f:
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

    call("ansible-playbook -i hosts playbook/hostname.yml", shell=True)
    call("ansible-playbook -i hosts playbook/interfaces.yml", shell=True)

    return 0


def on_error(ws, error):
    print "Error:", error


def on_close(ws):
    pass


def on_open(ws):
    pass


def connect():
    global stopped
    ws = websocket.WebSocketApp("ws://localhost:8001/prototype/worker",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    # websocket.enableTrace(True)
    try:
        while True:
            connect()
    except BaseException, e:
        traceback.print_exc(e)
    finally:
        print "done"
