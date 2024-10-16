# SubNetting

* <mark style="color:green;">**Definition:**</mark>&#x20;
  * Subnetting is the process of dividing a larger network into smaller, more manageable sub-networks or subnets.
* <mark style="color:green;">**Purpose:**</mark>
  * Enhances network efficiency by reducing broadcast domains.
  * Allows for better organization and management of IP addresses.
* <mark style="color:green;">**Method:**</mark>
  * Involves allocating a portion of the host bits in an IP address for network segmentation.
  * Enables the creation of distinct subnets with their own unique range of IP addresses.
* <mark style="color:green;">**Benefits:**</mark>
  * Optimizes IP address utilization.
  * Improves network performance and security.
* <mark style="color:green;">**Example:**</mark>
  * Original IP: 192.168.1.0
  * Subnetted into smaller subnets like 192.168.1.0/24 and 192.168.2.0/24.

Subnetting is achieved by splitting up the number of hosts that can fit within the network, represented by a number called a subnet mask.

<figure><img src="../../../.gitbook/assets/Capture (11).PNG" alt=""><figcaption></figcaption></figure>

As we can recall, an IP address is made up of four sections called octets.&#x20;

The same goes for a subnet mask which is also represented as a number of four bytes (32 bits), ranging from 0 to 255 (0-255).

<mark style="color:red;">Subnets use IP addresses in three different ways:</mark>

* Identify the network address.
* Identify the host address.
* Identify the default gateway.

<figure><img src="../../../.gitbook/assets/Capture (12).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">Subnetting provides a range of benefits, including:</mark>

* Efficiency.
* Security.
* Full control.

\
