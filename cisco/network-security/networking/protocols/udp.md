# UDP

<mark style="color:red;">**Definition:**</mark>&#x20;

* User Datagram Protocol (UDP) is a connectionless, lightweight transport layer protocol in computer networks.

<mark style="color:red;">**Connectionless Communication:**</mark>

* Operates without establishing a connection before data exchange.
* Does not guarantee reliable, ordered delivery.

<mark style="color:red;">**Low Overhead:**</mark>

* Has less protocol overhead compared to TCP, making it faster and more efficient.

<mark style="color:red;">**No Handshake:**</mark>

* Lacks a three-way handshake for connection establishment.

<mark style="color:red;">**Unreliable Delivery:**</mark>

* Does not provide acknowledgment or retransmission of lost packets.
* Suited for applications where occasional data loss is acceptable.

<mark style="color:red;">**No Flow Control:**</mark>

* No mechanism to control the flow of data, which can lead to potential congestion.

<mark style="color:red;">**Simple Header:**</mark>

* Has a minimal header with source and destination port numbers, length, and checksum.

<figure><img src="../../../../.gitbook/assets/Capture (17).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Fast Transmission:**</mark>

* Suitable for real-time applications like streaming and online gaming where speed is crucial.

<mark style="color:red;">**No Sequence Numbers:**</mark>

* Does not order packets; they may arrive out of order.

<mark style="color:red;">**Broadcast and Multicast Support:**</mark>

* Supports broadcasting and multicasting of data to multiple recipients simultaneously.

<mark style="color:red;">**Port Numbers:**</mark>

* Utilizes port numbers to identify specific applications on devices.

<mark style="color:red;">**Used in:**</mark>

* Applications where low latency and quick transmission are more critical than ensuring every piece of data reaches the destination.

<mark style="color:red;">**Examples of Applications:**</mark>

* DNS (Domain Name System), VoIP (Voice over IP), streaming media, online gaming.

<mark style="color:red;">**Part of the TCP/IP Protocol Suite:**</mark>

* Often used alongside IP (Internet Protocol) in the TCP/IP protocol suite.

In summary, UDP is a connectionless and lightweight protocol suitable for applications where speed and efficiency are prioritized over reliable, ordered delivery. It is commonly used in real-time and multimedia applications.

\
