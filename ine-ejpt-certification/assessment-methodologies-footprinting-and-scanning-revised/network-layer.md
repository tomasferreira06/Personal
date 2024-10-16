# Network Layer

## Network Layer

* The Network  Layer <mark style="color:red;">(Layer 3)</mark> of the OSI model is responsible for logical addressing, routing, and forwarding data packets between devices across different networks.
* Its primary goal is to determine the optimal path for data to travel from the source to the destination, even if the devices are on separate networks.
* The network layer abstracts the underlying physical network, allowing for the creation of a cohesive internetwork.

## Network Layer Protocols

* Several key protocols operate at the network layer of the OSI model. Here are some prominent network layer protocols:
  * <mark style="color:red;">Internet Protocol (IP):</mark>
    * <mark style="color:blue;">IPv4</mark>: The most widely used version of IP, employing 32-bit addresses and providing the foundation for communication on the Internet.
    * <mark style="color:blue;">IPv6</mark>: Developed to address the limitations of IPv4,  it uses 128-bit addresses and offers an exponentially larger address space.
  * <mark style="color:red;">Internet Control Message Protocol (ICMP)</mark>:
    * Used for error reporting and diagnostics. ICMP messages include ping (echo request and echo reply), traceroute, and various error messages.

## Internet Protocol (IP)

* The Internet Protocol is a central protocol in the suite of protocols that form the foundation of the Internet.
* It operates at the network layer of the OSI model and is responsible for logical addressing, routing and the fragmentation and reassembly of data packets.
* IP enables communication between  devices on different networks by providing a standardized way to identify and locate hosts.

## Internet Protocol Versions

* <mark style="color:red;">IPv4:</mark>&#x20;
  * IPv4 is the most widely used version of IP and employs 32-bit addresses. Each IP address is represented as four sets of octets separated by  dots (192.168.0.1).
  * IPv4 provides a finite address space, which has led to the  adoption of IPv6 to address the exhaustion of available IPv4 addresses.
* <mark style="color:red;">IPv6:</mark>
  * IPv6 was developed to overcome the limitations of IPv4 and provides a significantly larger address space using 128-bit addresses.
  * IPv6 addresses are represented in hexadecimal notation

## Internet Protocol Functionality

### Logical Addressing:

* Addresses serve as logical addresses assigned to network interfaces.
* These addresses uniquely identify each device on a network.
* IP addresses are hierarchical and structured based on network classes, subnets, and CIDR notation.

### Packet Structure:

* IP organizes data into packets for transmission across networks. Each packet consists of a header and a payload.
* The header contains essential information, including the source and destination IP addresses, version number, time-to-live (TTL), and protocol type.

### Frangmentation and Resssembly:

* IP allows for the fragmentation of large packets into smaller fragments when traversing networks with varying Maximum Transmission Unit (MTU) sizes.
* The receiving host reassembles these fragments to reconstruct the original packet.

### IP Addressing Types

* IP addresses can be classified into three types: unicast (one-to-one communication), broadcast (one-to-all communication within a subnet), and multicast (one-to-many communication to a selected group of devices).

### Subnetting:

* Subnetting is a technique that divides a large IP networks into smaller, more manageable sub-networks. It enhances network efficiency and security.

### Internet Control Message Protocol (ICMP):

* ICMP is closely assoicated with IP and is used for error reporting and diagnostic. Common ICMP messages include echo request and echo reply, which are used in the ping utility.

### Dynamic Host Configuration Protocl (DHCP):

* DHCP is often used in conjunction with IP to dynamically assign IP addresses to devices on a network, simplifying the process of network configuration.

## IP Header Format

* The IP protocol defines many differnet fields in the packet header.  These fields contain binary values that the IPv4 services reference as they forward packets across the network.
  * <mark style="color:blue;">IP Source Address</mark> - Packet  Source.
  * <mark style="color:blue;">IP Destination Address</mark> - Packet Destination.
  * <mark style="color:blue;">Time-To-Live (TTL)</mark> - An 8-bit value that indicates the remainining life of the packet.
  * <mark style="color:blue;">Type-of-Service (ToS)</mark> - The  Type-of-Service filed contains an 8-bit binary value that is used to determine the priority of each packet.
  * <mark style="color:blue;">Protocol</mark> - This 8-bit value indicates the data payload type that the packet is carrying.

## IP Header Fields

<figure><img src="../../.gitbook/assets/image (175).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

## IP Header Format

<figure><img src="../../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>

The first four bits identify the IP version. They can be used to represent IP version 4 or 6.

<figure><img src="../../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

The 32 bits/4 bytes starting at the bit position 96 are allocated for the specification of the source address.

<figure><img src="../../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

The followin 4 bytes represent the destination address.

<figure><img src="../../.gitbook/assets/image (181).png" alt=""><figcaption></figcaption></figure>

## IPv4 Addresses

* The vast majority of networks run IP version 4
* An IPv4 address consists of four bytes, or octets; a byte consists of 8 bits.
* A dot delimits every octet in the address.

<figure><img src="../../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

## Reserved IPv4 Addresses

* For example, some reserved intervals are:
  * 0.0.0.0 - 0.255.255.255 representing "this" network.
  * 127.0.0.0 - 127.255.255.255 representing the local host
  * 192.168.0.0 - 192.168.255.255 is reserved for private networks
* You can find the details about the special use of IPv4 addresses in RFC5735
