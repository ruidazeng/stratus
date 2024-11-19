# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/focal64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false
  
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  # The shell provisioner can also accept a script that will be executed in
  # the guest in user mode (by default). See the bootstrap.sh script
  # where we create the above directories and they all will execute
  # as the user "vagrant" by default 
  config.vm.provision "shell", path: "bootstrap.sh"

  # let's copy our pem file to the vagrant created guest. Change the file name
  # as appropriate in your case and also the file path based on where on your
  # host you have stored this file.
  #
  # Note that I am on Windows m/c and so have used the Windows path to
  # the source. I created an equivalent directory structure on my Windows
  # file system as Linux with .ssh, etc directories.
  config.vm.provision "file", source: "jh_ku_chameleon.key", destination: "~/.ssh/"

  # let's also copy our ansible.cfg, MyInventory and cloud.yaml file
  config.vm.provision "file", source: ".ansible.cfg", destination: "~/.ansible.cfg"
  config.vm.provision "file", source: "MyInventory", destination: "~/.ansible/MyInventory"
  config.vm.provision "file", source: "clouds.yaml", destination: "~/.config/openstack/clouds.yaml"
  config.vm.provision "file", source: "consumer.py", destination: "~/consumer.py"

  
  #Docker files
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/dockerfile", destination: "~/Kafka_Zoo_Deployment_dockerfile"
  config.vm.provision "file", source: "CouchDB_Deployment/dockerfile", destination: "~/couchdb_dockerfile"
  config.vm.provision "file", source: "Consumer_Deployment/dockerfile", destination: "~/consumer_dockerfile"
  config.vm.provision "file", source: "Nginx_Deployment/dockerfile", destination: "~/nginx_dockerfile"


  #Couchdb
  config.vm.provision "file", source: "CouchDB_Deployment/local.ini", destination: "~/local.ini"
  config.vm.provision "file", source: "CouchDB_Deployment/couchdb_job.yml", destination: "~/couchdb_job.yml"
  config.vm.provision "file", source: "CouchDB_Deployment/couchdb_service.yml", destination: "~/couchdb_service.yml"

  #Transfer zookeeper files
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/zookeeper_service_svc.yml", destination: "~/zookeeper_service_svc.yml"
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/zookeeper_service_job.yml", destination: "~/zookeeper_service_job.yml"
  #Transfer kafka broker 0 files
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_0_service.yml", destination: "~/kafka_broker_0_service.yml"
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_0_job.yml", destination: "~/kafka_broker_0_job.yml"

  #Transfer kafka broker 1 files
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_1_service.yml", destination: "~/kafka_broker_1_service.yml"
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_1_job.yml", destination: "~/kafka_broker_1_job.yml"

  #Transfer kafka broker 2 files
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_2_service.yml", destination: "~/kafka_broker_2_service.yml"
  config.vm.provision "file", source: "Kafka_Zoo_Deployment/kafka_broker_2_job.yml", destination: "~/kafka_broker_2_job.yml"

  #Consumer
  config.vm.provision "file", source: "Consumer_Deployment/consumer_job.yml", destination: "~/consumer_job.yml"

  #Spark
  config.vm.provision "file", source: "Spark_Deployment/dockerfile", destination: "~/spark_dockerfile"
  config.vm.provision "file", source: "Spark_Deployment/spark-driver.conf", destination: "~/spark-driver.conf"
  config.vm.provision "file", source: "Spark_Deployment/spark-worker.conf", destination: "~/spark-worker.conf"
  config.vm.provision "file", source: "Spark_Deployment/spark-env.sh", destination: "~/spark-env.sh"

  #Spark master
  config.vm.provision "file", source: "Spark_Deployment/spark-master-svc.yml", destination: "~/spark-master-svc.yml"
  config.vm.provision "file", source: "Spark_Deployment/spark-master-deploy.yml", destination: "~/spark-master-deploy.yml"
  config.vm.provision "file", source: "Spark_Deployment/ML-deployment.py", destination: "~/ML-deployment.py"

  #Spark driver and worker 
  config.vm.provision "file", source: "Spark_Deployment/spark-driver-svc.yml", destination: "~/spark-driver-svc.yml"
  config.vm.provision "file", source: "Spark_Deployment/spark-driver-deploy.yml", destination: "~/spark-driver-deploy.yml"
  config.vm.provision "file", source: "Spark_Deployment/spark-worker-deploy.yml", destination: "~/spark-worker-deploy.yml"

  #Nginx Deployment and Service 
  config.vm.provision "file", source: "Nginx_Deployment/nginx-deployment.yml", destination: "~/nginx-deployment.yml"
  config.vm.provision "file", source: "Nginx_Deployment/nginx-service.yml", destination: "~/nginx-service.yml"

  # make sure the permissions on the  pem file are not too open.
  # Note, here I show you using inline and privileged: false so the inline
  # action actually happens as the user vagrant.
  # Moreover, we also show a diff approach to put the inline code in
  # a block, and then use the block name. 
  # Change file name as appropriate. Replace this with your pem file.
  $script = <<-SCRIPT
     chmod go-rwx ~/.ssh/jh_ku_chameleon.key
  SCRIPT
  config.vm.provision "shell", inline: $script, privileged: false

  # We now use the Ansible provisioner
  #
  # in the following, install= true will install ansible in the
  # created or provisioned guest vm. Once ansible is installed, any
  # additional configuration we plan to do will be taken from the
  # supplied playbook. Moreover, we can also tell ansible which
  # Inventory file it should use. This inventory file will appear in the
  # /vagrant directory (which is the same directory on your host that has
  # the vagrantfile but is mounted as /vagrant in the guest machine)
  #
  # Please note that the get facts about cloud will fail because we haven't
  # installed openstacksdk and ansible galaxy plugin. All those steps
  # are left for you to fill up
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook_demo_master.yml"
    ansible.verbose = true
    ansible.install = true  # installs ansible (and hence python on VM)
    ansible.limit = "all"
    ansible.inventory_path = "MyInventory"  # inventory file
  end
end

