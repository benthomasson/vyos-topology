
Vagrant.configure("2") do |config|



    config.vm.define "Switch1" do |device|
        device.vm.hostname = "Switch1"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Switch1 eth1 to Switch4 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9105',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9104',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Switch1 eth2 to Switch3 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9106',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9107',
             :libvirt__iface_name => 'eth2',
             auto_config: false
    end # config.vm.define Switch1



    config.vm.define "Switch2" do |device|
        device.vm.hostname = "Switch2"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Switch2 eth1 to Switch4 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9101',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9100',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Switch2 eth2 to Switch3 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9103',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9102',
             :libvirt__iface_name => 'eth2',
             auto_config: false
    end # config.vm.define Switch2



    config.vm.define "Switch3" do |device|
        device.vm.hostname = "Switch3"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Switch3 eth1 to Switch2 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9102',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9103',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Switch3 eth2 to Switch1 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9107',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9106',
             :libvirt__iface_name => 'eth2',
             auto_config: false
    end # config.vm.define Switch3



    config.vm.define "Switch4" do |device|
        device.vm.hostname = "Switch4"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Switch4 eth1 to Switch2 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9100',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9101',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Switch4 eth2 to Switch1 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9104',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9105',
             :libvirt__iface_name => 'eth2',
             auto_config: false
    end # config.vm.define Switch4



end  # Vagrant.configure