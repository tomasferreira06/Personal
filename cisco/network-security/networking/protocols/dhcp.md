# DHCP

* <mark style="color:green;">**Definition:**</mark>&#x20;
  * Dynamic Host Configuration Protocol (DHCP) is a network protocol used to automatically assign IP addresses and network configuration information to devices on a network.
* <mark style="color:green;">**Purpose:**</mark>
  * Simplifies network administration by automating the IP address assignment process.

<mark style="color:red;">**Key Components:**</mark>

* <mark style="color:green;">**DHCP Server:**</mark>
  * Manages and assigns IP addresses to devices on the network.
* <mark style="color:green;">**DHCP Client:**</mark>
  * Device requesting an IP address from the DHCP server.
* <mark style="color:green;">**Lease Process:**</mark>
  * DHCP server leases an IP address to a client for a specified duration.
  * Lease can be renewed or released based on network requirements.
* <mark style="color:green;">**Dynamic Configuration:**</mark>
  * Provides dynamic configuration settings, including subnet mask, default gateway, and DNS servers.

<mark style="color:red;">**Allocation Methods:**</mark>

* <mark style="color:green;">**Dynamic Allocation:**</mark>
  * Server assigns a new IP address to a client each time it connects to the network.
* <mark style="color:green;">**Static Allocation:**</mark>
  * Server assigns a fixed IP address to a specific client based on its MAC address.
* <mark style="color:green;">**Dynamic Allocation with Reservation:**</mark>
  * Server dynamically assigns IP addresses but reserves specific addresses for certain devices.

<mark style="color:red;">**DHCP Discover, Offer, Request, Acknowledge (DORA) Process:**</mark>

* <mark style="color:green;">**Discover:**</mark>&#x20;
  * Client broadcasts a request for available DHCP servers.
* <mark style="color:green;">**Offer:**</mark>&#x20;
  * DHCP server responds with an IP address offer.
* <mark style="color:green;">**Request:**</mark>&#x20;
  * Client formally requests the offered IP address.
* <mark style="color:green;">**Acknowledge:**</mark>
  * &#x20;DHCP server acknowledges the client's request and finalizes the IP address assignment.

<mark style="color:red;">**Benefits:**</mark>

* Efficient IP address management.
* Minimizes configuration errors.
* Simplifies network changes and additions.

In summary, DHCP automates the process of assigning and managing IP addresses, providing dynamic network configuration to devices on a network.

\
