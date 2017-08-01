
Vagrant.configure("2") do |config|



    config.vm.define "Host1" do |device|
        device.vm.hostname = "Host1"
        device.vm.box ="boxcutter/ubuntu1404"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Host1 eth1 to Leaf1 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9123',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9122',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define Host1



    config.vm.define "Host2" do |device|
        device.vm.hostname = "Host2"
        device.vm.box ="boxcutter/ubuntu1404"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Host2 eth1 to Leaf2 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9117',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9116',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define Host2



    config.vm.define "Host3" do |device|
        device.vm.hostname = "Host3"
        device.vm.box ="boxcutter/ubuntu1404"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Host3 eth1 to Leaf3 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9119',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9118',
             :libvirt__iface_name => 'eth1',
             auto_config: false
    end # config.vm.define Host3



    config.vm.define "Leaf1" do |device|
        device.vm.hostname = "Leaf1"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Leaf1 eth1 to Spine1 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9103',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9102',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Leaf1 eth2 to Spine2 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9109',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9108',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # Leaf1 eth3 to Host1 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9122',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9123',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # Leaf1 eth4 to Leaf1 eth5
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9121',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9120',
             :libvirt__iface_name => 'eth4',
             auto_config: false
        # Leaf1 eth5 to Leaf1 eth4
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9120',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9121',
             :libvirt__iface_name => 'eth5',
             auto_config: false
    end # config.vm.define Leaf1



    config.vm.define "Leaf2" do |device|
        device.vm.hostname = "Leaf2"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Leaf2 eth1 to Spine1 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9105',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9104',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Leaf2 eth2 to Spine2 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9111',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9110',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # Leaf2 eth3 to Host2 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9116',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9117',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # Leaf2 eth4 to Leaf2 eth5
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9101',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9100',
             :libvirt__iface_name => 'eth4',
             auto_config: false
        # Leaf2 eth5 to Leaf2 eth4
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9100',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9101',
             :libvirt__iface_name => 'eth5',
             auto_config: false
    end # config.vm.define Leaf2



    config.vm.define "Leaf3" do |device|
        device.vm.hostname = "Leaf3"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Leaf3 eth1 to Spine1 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9107',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9106',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Leaf3 eth2 to Spine2 eth3
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9113',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9112',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # Leaf3 eth3 to Host3 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9118',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9119',
             :libvirt__iface_name => 'eth3',
             auto_config: false
    end # config.vm.define Leaf3



    config.vm.define "Spine1" do |device|
        device.vm.hostname = "Spine1"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Spine1 eth1 to Leaf1 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9102',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9103',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Spine1 eth2 to Leaf2 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9104',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9105',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # Spine1 eth3 to Leaf3 eth1
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9106',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9107',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # Spine1 eth4 to Spine2 eth4
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9114',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9115',
             :libvirt__iface_name => 'eth4',
             auto_config: false
    end # config.vm.define Spine1



    config.vm.define "Spine2" do |device|
        device.vm.hostname = "Spine2"
        device.vm.box ="higebu/vyos"
        device.vm.synced_folder ".", "/vagrant", disabled: true

        
        # Spine2 eth1 to Leaf1 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9108',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9109',
             :libvirt__iface_name => 'eth1',
             auto_config: false
        # Spine2 eth2 to Leaf2 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9110',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9111',
             :libvirt__iface_name => 'eth2',
             auto_config: false
        # Spine2 eth3 to Leaf3 eth2
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9112',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9113',
             :libvirt__iface_name => 'eth3',
             auto_config: false
        # Spine2 eth4 to Spine1 eth4
        device.vm.network "private_network",
             :libvirt__tunnel_type => 'udp',
             :libvirt__tunnel_local_ip => '127.0.0.1',
             :libvirt__tunnel_local_port => '9115',
             :libvirt__tunnel_ip => '127.0.0.1',
             :libvirt__tunnel_port => '9114',
             :libvirt__iface_name => 'eth4',
             auto_config: false
    end # config.vm.define Spine2



end  # Vagrant.configure