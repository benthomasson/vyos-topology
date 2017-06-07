

A set of templates to generate vyos networks topologies for vagrant-libvirt.


Requirements
------------

    pip install -r requirements.txt

    ssh-keygen -T key




Start
-----

    ansible-playbook playbook/up.yml


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


Tear down
---------

    ansible-playbook playbook/down.yml
