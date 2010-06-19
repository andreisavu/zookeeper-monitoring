
Configuration Recipe for monitoring ZooKeeper using Nagios
----------------------------------------------------------

I will start by making the assumption that you already have an working Nagios install.

WARNING: I have wrote these instructions while installing and configuring the plugin on my desktop computer running Ubuntu 9.10. I've installed Nagios using apt-get.


1. Install the plugin

$ cp check_zookeeper.py /usr/lib/nagios/plugins/

2. Install the new commands

$ cp zookeeper.cfg /etc/nagios-plugins/config

3. Update the list of servers in zookeeper.cfg. It should contain all the ZooKeeper servers in the cluster. 

4. Create a virtual host in Nagios used for monitoring the cluster as a whole. 

5. Define service checks like this: 

define service {
    use         generic-service
    host_name   zookeeper-cluster
    service_description ...
    check_command check_zookeeper!<exported-var>!<warning-level>!<critical-level>
}

Ex: 

a. check the number of open file descriptors

define service{
        use         generic-service
        host_name   zookeeper-cluster
        service_description ZK_Open_File_Descriptor_Count
        check_command check_zookeeper!zk_open_file_descriptor_count!500!800
}

b. check the number of ephemerals nodes

define service {
        use generic-service
        host_name localhost
        service_description ZK_Ephemerals_Count
        check_command check_zookeeper!zk_ephemerals_count!10000!100000
}


