# VLAN

<mark style="color:red;">**Definition:**</mark>

* VLAN is a network segmentation technique that divides a physical network into multiple logical networks, allowing devices to communicate as if they are on the same physical network, regardless of their actual physical location.

<mark style="color:red;">**Logical Segmentation:**</mark>

* Creates virtual LANs that function independently within a larger physical network.

<mark style="color:red;">**Benefits:**</mark>

* <mark style="color:green;">**Isolation:**</mark>
  * Devices in one VLAN are isolated from devices in other VLANs, enhancing network security.
* <mark style="color:green;">**Broadcast Control:**</mark>
  * Reduces broadcast traffic by confining it to specific VLANs.
* <mark style="color:green;">**Logical Grouping:**</mark>
  * Enables logical grouping of devices based on function, department, or project.

<mark style="color:red;">**How it Works:**</mark>

* Devices in the same VLAN can communicate directly, even if they are physically located in different parts of the network.
* VLAN information is added to the Ethernet frame header to identify the VLAN membership of the packet.

<figure><img src="../../../.gitbook/assets/Capture (21).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Types:**</mark>

* <mark style="color:green;">**Port-Based VLAN:**</mark>
  * Devices are assigned to VLANs based on the physical port to which they are connected.
* <mark style="color:green;">**802.1Q VLAN (Tagged VLAN):**</mark>
  * VLAN information is added as a tag in the Ethernet frame, allowing a single physical port to carry traffic for multiple VLANs.

<mark style="color:red;">**Management:**</mark>

* VLANs are typically configured and managed through network switches.

<mark style="color:red;">**Inter-VLAN Routing:**</mark>

* For communication between VLANs, a router or layer 3 switch is required.

<mark style="color:red;">**Flexibility:**</mark>

* Simplifies network management by allowing changes to the logical structure without physically rewiring the network.

<mark style="color:red;">**Applications:**</mark>

* Commonly used in large networks, data centers, and environments requiring secure segmentation.

<mark style="color:red;">**Security Considerations:**</mark>

* Enhances security by isolating sensitive traffic and controlling communication between VLANs.

<mark style="color:red;">**QoS (Quality of Service):**</mark>

* Enables the prioritization of traffic within each VLAN for optimized performance.

<mark style="color:red;">**In Summary:**</mark>

* VLANs logically segment a physical network into multiple virtual LANs.
* Devices within the same VLAN can communicate as if on the same physical network.
* Enhances network security, reduces broadcast traffic, and facilitates logical grouping of devices.





\
