# Switch

* **Function:**&#x20;
* A networking device operating at the Data Link Layer (Layer 2) of the OSI model and Network Layer (Layer 3).
* **Connectivity:** Links multiple devices within a local area network (LAN).

<mark style="color:red;">How it works:</mark>

* <mark style="color:green;">**MAC Address Learning:**</mark>
  * Learns MAC addresses of connected devices by examining source MAC addresses in incoming frames.
  * Maintains a MAC address table associating each address with the corresponding port.
* <mark style="color:green;">**Frame Forwarding:**</mark>
  * Directly forwards frames to the port where the destination device is located based on the MAC address table.
  * Unicast forwarding for communication between specific devices.
* <mark style="color:green;">**Broadcast and Unknown Unicast:**</mark>
  * Forwards frames to all ports (except the source) for broadcast or unknown unicast addresses.
  * Learns new MAC addresses through this process.
* <mark style="color:green;">**Filtering and Collision Domains:**</mark>
  * Creates individual collision domains for each port, preventing collisions on the network.
  * Efficiently filters and forwards frames only to the relevant ports.
* <mark style="color:green;">**Full-Duplex Communication:**</mark>
  * Supports full-duplex communication, allowing simultaneous data transmission and reception on the same connection.
* <mark style="color:green;">**Efficiency Improvement:**</mark>
  * Enhances network efficiency by reducing collisions and creating isolated communication paths.

In summary, a switch intelligently manages network traffic, improves efficiency, and facilitates direct communication between devices within a LAN.

<figure><img src="../../../../.gitbook/assets/Capture (9).PNG" alt=""><figcaption></figcaption></figure>

\


