# Host Discovery Techniques

## Host Discovery

* In pentesting, host discovery is a crucial phase to identify live hosts on a network before further exploration and vulnerability assessment.

## Host Discovery Techniques

* <mark style="color:blue;">Ping Sweeps</mark> (ICMP echo requests): Sending pings to a range of IP addresses to identify live hosts
  * <mark style="color:green;">Pros</mark>: ICMP ping is a widely supported and quick method for identifying live hosts.&#x20;
  * <mark style="color:orange;">Cons</mark>: Some hosts or firewalls may be configured to block ICMP traffic, limiting its effectiveness. ICMP ping can also be easily detected.
* <mark style="color:blue;">ARP Scanning</mark>: Using ARP requests to identify hosts on a local network.
* <mark style="color:blue;">TCP SYN Ping</mark> (Half-Open Scan): Sending TCP SYN packets to a specific port to check if the host is alive. This technique is stealthier than ICMP ping.
  * <mark style="color:green;">Pros</mark>: TCP SYN ping is stealthier than ICMP and may bypass firewalls that allow outbound connections.
  * <mark style="color:orange;">Cons</mark>: Some hosts may not respond to TCP SYN requests, and the results can be affected by firewalls and security devices.
* <mark style="color:blue;">UDP Ping</mark>: Sends UDP  packets to a specific port to check if a host is alive. Can be effective for hosts that do not respond to ICMP  or TCP probes.
* <mark style="color:blue;">TCP ACK Ping</mark>: Sending TCP ACK packets to a specific port to check if a host is alive. This technique expects no response, but if a TCP RST is received, it indicates that the host is alive.
* <mark style="color:blue;">SYN-ACK Ping</mark>: Sendintg SYN-ACK packets to a specific port to check if a host is alive.
