# ARP

* <mark style="color:green;">**Definition:**</mark>&#x20;
  * Address Resolution Protocol (ARP) is a communication protocol used to map IP addresses to MAC addresses in a local network.
* <mark style="color:green;">**Purpose:**</mark>
  * Resolves layer 3 (IP) addresses to layer 2 (MAC) addresses for data transmission within the same network.
* <mark style="color:green;">**Process:**</mark>
  * When a device wants to communicate with another device in the local network, it sends an ARP request, asking for the MAC address associated with a specific IP address.
* <mark style="color:green;">**ARP Request:**</mark>
  * Broadcasts a request to the entire network, asking "Who has this IP address?"
* <mark style="color:green;">**ARP Reply:**</mark>
  * The device with the corresponding IP address replies with its MAC address.
* <mark style="color:green;">**ARP Table:**</mark>
  * Each device maintains an ARP table, associating known IP addresses with their corresponding MAC addresses.
* <mark style="color:green;">**Caching:**</mark>
  * Devices store ARP information in their cache to avoid repeated ARP broadcasts for frequently accessed addresses.
* <mark style="color:green;">**Dynamic Nature:**</mark>
  * ARP is dynamic and can change as devices join or leave the network.
* <mark style="color:green;">**Use Case:**</mark>
  * Vital for local communication within a network before data is transmitted over the larger internet.

In summary, ARP is a protocol that resolves IP addresses to MAC addresses within a local network, enabling devices to communicate effectively.

\
