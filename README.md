

A set of templates to generate vyos networks topologies for vagrant-libvirt.


Requirements
------------

    pip install -r requirements.txt

    ssh-keygen -f key -t rsa -N ''



Remote Start
-------------

    ansible-playbook -i hypervisor playbook/start_vms.yml

Remote Destroy
-------------

    ansible-playbook -i hypervisor playbook/destroy_vms.yml


Start
-----

    ansible-playbook playbook/up.yml
    ansible-playbook -i hosts playbook/key.yml


Configure
---------

    ansible-playbook -i hosts playbook/interfaces.yml
    ansible-playbook -i hosts playbook/routing.yml

Verify
---------

    ansible-playbook -i hosts playbook/ping_interfaces.yml
    ansible-playbook -i hosts playbook/ping_reachable.yml


Deploy Pipeline
---------------

    ansible-playbook -i hosts playbook/pipeline.yml


Break Networking
----------------

    ansible-playbook -i hosts playbook/break.yml
    ansible-playbook -i hosts playbook/no_routing.yml



Tear down
---------

    ansible-playbook playbook/down.yml
