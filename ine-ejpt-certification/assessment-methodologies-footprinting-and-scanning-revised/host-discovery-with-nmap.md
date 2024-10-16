# Host Discovery with Nmap

## Host Discovery

Host discovery in "<mark style="color:red;">nmap</mark>" is when you only use ping probes to identify what devices exist in a given network.

## Practical Demo

Commands:

* <mark style="color:yellow;">sudo nmap -sn 192.168.2.0/24</mark>
  * "<mark style="color:blue;">-sn</mark>": This flag turns off the port scanning probes, making it so that the scan only sends ping requests to identify devices in a given network
    * <mark style="color:purple;">NOTE:</mark> Always use this option when discovering hosts
* "<mark style="color:yellow;">-PS</mark>": SYN Ping overrides the "<mark style="color:yellow;">-sn</mark>" ping
  * If used with "<mark style="color:yellow;">-sn</mark>", it will only do host discovery using the SYN Ping.
  * If used alone will do the SYN Ping and port scanning for services
* "<mark style="color:yellow;">-PA</mark>": ACK Ping&#x20;
  * Usually not very reliable, because normally hosts are configured to block ACK pings, or block RST packets out
* "<mark style="color:yellow;">-PE</mark>": ICMP Echo request scan
* "<mark style="color:yellow;">-PU</mark>": UDP Scan

### netdiscover

"Netdiscover" works by sending "<mark style="color:red;">ARP</mark>" requests, which is the protocol that resolves MAC addresses into IP addresses or vice-versa.

#### Command to run:

* <mark style="color:yellow;">sudo</mark> <mark style="color:yellow;">netdiscover -i eth0 -r 192.168.2.0/24</mark>
  * "<mark style="color:blue;">-i</mark>": This flag is used to define the network interface

<figure><img src="../../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

### Example Methodology Steps

* "<mark style="color:yellow;">nmap -sn -v -T4 10.1.2.3</mark>"
* "<mark style="color:yellow;">nmap -sn -PS(Indicate most used ports) -T4 10.1.2.3</mark>"
* "<mark style="color:yellow;">nmap -sn -PS(Indicate most used ports) -PU -T4 10.1.2.3</mark>"
  * <mark style="color:purple;">NOTE:</mark> In case it is a Windows machine for Netbios etc.. that use UDP
