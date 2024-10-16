# Ping Sweeps

## Ping Sweeps

* A ping sweep is a network scanning technique used to discover live hosts (computers, servers, or other devices) within a specific IP address range on a network.
* The <mark style="color:red;">ping</mark> command is a utility designed to check if a host is alive/reachable.

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

## How they work

* Ping sweeps work by sending one or more specially crafted ICMP packets <mark style="color:red;">(Type 8 - echo request)</mark> to a host.&#x20;
* If the destination host replies with an ICMP echo reply <mark style="color:red;">(Type 0)</mark> packet, then the host is alive/online.&#x20;

In the context of ICMP (Internet Control Message Protocol), the ICMP Echo Request and Echo Reply messages are used for the purpose of ping. These messages have specific ICMP type and code values associated with them.

* ICMP Echo Requests:
  * Type: 8
  * Code: 0
* ICMP Echo Reply:
  * Type: 0&#x20;
  * Code: 0

The "<mark style="color:red;">Type</mark>" field indicates the purpose of function of the ICMP message.

The "<mark style="color:red;">Code</mark>" field  provides additional information or context related to the message type.

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>
