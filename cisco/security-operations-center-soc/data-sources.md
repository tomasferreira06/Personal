# Data Sources

SOC uses many data sources to monitor the network for signs of intrusions and to detect any malicious behaviour. A SOC might use a Security Information and Event Management System(SIEM). The SIEM aggregates the data from different sources in order to efficiently correlate the data and respond to attacks.

#### Some of these sources are:

### **Server logs**

* There are many types of servers ona network,such as a mail server, web server and domain controller on MS Windows networks. Logs contain information about various activites,such as successful and failed login attempts, among many others.

### **DNS Activity**

* Domain Name System is the protocol responsible for converting a domain name, such as "tryhackme.com" ,to an IP, such as  10.3.13.37, aomg other tasks. The team can gather information about domain names by merely inspecting DNS queries.

### **Firewall logs**

* A firewall is a device that controls network packets entering and leaving the network mainly by letting them through or blocking them. Consequently, firewall logs can reveal much  information about what packets passed or tried to pass through the firewall.

### **DHCP logs**

* Dynamic Host Configuration Protocol is responsible for assigning an IP address to the systems that try to connect to a network. Know that DHCP has automatically provided your device with the network settings whenever you can join a network without manual configuration. By inspecting DHCP transactions, we can learn about the devices that joined the network.
