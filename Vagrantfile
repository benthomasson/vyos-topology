
Vagrant.configure("2") do |config|



    config.vm.define "leaf00" do |device|
        device.vm.hostname = "leaf00"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # leaf00 eth0 to spine00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9115',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9114',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # leaf00 eth0 to spine00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9115',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9114',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # leaf00 eth1 to spine01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9123',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9122',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # leaf00 eth1 to spine01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9123',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9122',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # leaf00 eth2 to server00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9107',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9106',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # leaf00 eth2 to server00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9107',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9106',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # leaf00 eth3 to server01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9131',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9130',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # leaf00 eth3 to server01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9131',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9130',
             :libvirt__iface_name => 'eth3',
             auto_config: false
    end # config.vm.define leaf00



    config.vm.define "leaf01" do |device|
        device.vm.hostname = "leaf01"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # leaf01 eth0 to spine00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9111',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9110',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # leaf01 eth0 to spine00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9111',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9110',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # leaf01 eth1 to spine01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9119',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9118',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # leaf01 eth1 to spine01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9119',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9118',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # leaf01 eth2 to server00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9103',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9102',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # leaf01 eth2 to server00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9103',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9102',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # leaf01 eth3 to server01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9127',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9126',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # leaf01 eth3 to server01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9127',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9126',
             :libvirt__iface_name => 'eth3',
             auto_config: false
    end # config.vm.define leaf01



    config.vm.define "server00" do |device|
        device.vm.hostname = "server00"
        device.vm.box ="boxcutter/ubuntu1404"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # server00 eth0 to leaf00 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9106',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9107',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # server00 eth0 to leaf00 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9106',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9107',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # server00 eth1 to leaf01 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9102',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9103',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # server00 eth1 to leaf01 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9102',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9103',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define server00



    config.vm.define "server01" do |device|
        device.vm.hostname = "server01"
        device.vm.box ="boxcutter/ubuntu1404"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # server01 eth0 to leaf00 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9130',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9131',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # server01 eth0 to leaf00 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9130',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9131',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # server01 eth1 to leaf01 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9126',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9127',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # server01 eth1 to leaf01 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9126',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9127',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define server01



    config.vm.define "spine00" do |device|
        device.vm.hostname = "spine00"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # spine00 eth0 to leaf00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9114',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9115',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # spine00 eth0 to leaf00 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9114',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9115',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # spine00 eth1 to leaf01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9110',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9111',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # spine00 eth1 to leaf01 eth0
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9110',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9111',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define spine00



    config.vm.define "spine01" do |device|
        device.vm.hostname = "spine01"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # spine01 eth0 to leaf00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9122',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9123',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # spine01 eth0 to leaf00 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9122',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9123',
             :libvirt__iface_name => 'eth0',
             auto_config: false
        # spine01 eth1 to leaf01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9118',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9119',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # spine01 eth1 to leaf01 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9118',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9119',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define spine01



end  # Vagrant.configure