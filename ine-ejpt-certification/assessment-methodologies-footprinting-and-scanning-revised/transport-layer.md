# Transport Layer

## Transport Layer

* The transport layer is the fourrth of the OSI model, and it plays a crucial role in facilitating communication between two devices across a network.
* This layer ennsures reliable, end-to-end communication, handling tasks such as error detection, flow control and segmentation of data into smaller units.
* The Transport Layer, is responsible for providing end-to-end communication and ensuring the reliable and ordered delivery of data between two devices on a network.

## Transport Layer Protocols

* <mark style="color:red;">TCP</mark> : Connection-oriented protocol providing reliable and ordered delivery of data.
* <mark style="color:red;">UDP</mark>: Connectionless protocol that is faster but provides no guarantees regarding the order or reliability of data delivery.

## TCP

* TCP, is one of the main protocols operating at Layer 4 of the OSI model.
* It is a connection-oriented, reliable protocol that provides a dependable and ordered delivery of data between two devices over a network.
* TCP ensures that data sent from one application on a device is received accurately and in the correct order by another application on a different device.

### Connection-Oriented

* TCP establishes a connection between the sender and receiver before any data is exchanged. This connection is a virtual circuit that ensures reliable and ordered  data transfer.

### Reliability

* TCP guarantees reliable delivery of data. It achieves this through mechanisms such as acknowledgments <mark style="color:red;">(ACK)</mark> and retransmission of lost or corrupted packets. If a segment of data is not acknowledged , TCP automatically resends the segment.

### Ordered Data Transfer

* TCP  enables that data is delivered in the correct order. If segments of data arrive out of oder, TCP reorders them before passing them to te higher-layer application.

## TCP 3-Way Handshake

* The TCP three-way handshake is a process used to establish a reliable connection between two devices before they begin data transmission.
* It involves a series of three messages exchanged between the sender (client) and the receiver (server).

<figure><img src="../../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

* <mark style="color:blue;">SYN</mark> <mark style="color:blue;">(Synchronize)</mark>: The process begins with the client sending a TCP segment with the SYN (Synchronize) flag set. This initial message indicates the client's intention to establish a connection and includes an initial sequence number (ISN), which is a randomly chosen value.
* <mark style="color:blue;">SYN-ACK</mark> <mark style="color:blue;">(Synchronize-Acknowledge)</mark>: Upon receiving the SYN segment, the server responds with a TCP segment that has both the SYN and ACK (Acknowledge) flags set. The acknowledgment (ACK) number is set to one more than the initial sequence number received in the client's SYN segment. The server also generates its own initial sequence number.
* <mark style="color:blue;">ACK (Acknowledge)</mark>: Finally, the client acknowledges the server's response by sending a TCP segment with the ACK flag set. The acknowledgment number is set to one more than the server's initial sequence number.&#x20;
* At this point, the connection is established, and both devices can begin transmitting data.&#x20;
* After the three-way handshake is complete, the devices can exchange data in both directions. The acknowledgment numbers in subsequent segments are used to confirm the receipt of data and to manage the flow of information.

## TCP Header Finds

<figure><img src="../../.gitbook/assets/image (184).png" alt=""><figcaption></figcaption></figure>

The SRC (16 bits) & DST (16 bits). Port identifies the source and destination port.

<figure><img src="../../.gitbook/assets/image (185).png" alt=""><figcaption></figcaption></figure>

## TCP Control Flags

* TCP uses a set of control flags to manage various aspects of the communication process.
* These  flags are included in the TCP header and controll different features during the establishment, maintenance and termination of a TCP connection.

### Establishing a Connection:

* <mark style="color:blue;">SYN (Set):</mark> Initiates a connection request.
* <mark style="color:blue;">ACK (Clear)</mark>: No acknowledgment yet.
* <mark style="color:blue;">FIN (Clear)</mark>: No termination request.&#x20;

### Establishing a Connection (Response):

* <mark style="color:blue;">SYN (Set)</mark>: Acknowledges the connection request.
* <mark style="color:blue;">ACK (Set)</mark>: Acknowledges the received data.
* <mark style="color:blue;">FIN (Clear)</mark>: No termination request.

### Terminating a Connection:

* <mark style="color:blue;">SYN (Clear):</mark> No connection request.
* <mark style="color:blue;">ACK (Set):</mark> Acknowledges the received data.
* <mark style="color:blue;">FIN (Set):</mark> Initiates connection termination.

## TCP Port Range

* TCP (Transmission Control Protocol) uses port numbers to distinguish between different services or applications on a device.&#x20;
* Port numbers are 16-bit unsigned integers, and they are divided into three ranges.&#x20;
* The maximum port number in the TCP/IP protocol suite is 65,535.

Well-Known Ports (0-1023): Port numbers from 0 to 1023 are reserved for well-known services and protocols. These are standardized by the Internet Assigned Numbers Authority (IANA). Examples include:

* 80: HTTP (Hypertext Transfer Protocol)
* 443: HTTPS (HTTP Secure)
* 21: FTP (File Transfer Protocol)
* 22: SSH (Secure Shell)
* 25: SMTP (Simple Mail Transfer Protocol)
* 110: POP3 (Post Office Protocol version 3)

Registered Ports (1024-49151): Port numbers from 1024 to 49151 are registered for specific services or applications. These are typically assigned by the IANA to software vendors or developers for their applications. While they are not standardized, they are often used for well-known services. Examples include:

* 3389: Remote Desktop Protocol (RDP)
* 3306: MySQL Database
* 8080: HTTP alternative port
* 27017: MongoDB Database

## UDP

* UDP, or User Datagram Protocol, is a connectionless and lightweight transport layer protocol that provides a simple and minimalistic way to transmit data between devices on a network.&#x20;
* UDP does not establish a connection before sending data and does not provide the same level of reliability and ordering guarantees. Instead, it focuses on simplicity and efficiency, making it suitable for certain types of applications.
* Connectionless: UDP is a connectionless protocol, meaning that it does not establish a connection before sending data. Each UDP packet (datagram) is treated independently, and there is no persistent state maintained between sender and receiver.&#x20;
* Unreliable: UDP does not provide reliable delivery of data. It does not guarantee that packets will be delivered, and there is no mechanism for retransmission of lost packets. This lack of reliability makes UDP faster but less suitable for applications that require guaranteed delivery.
* Used for Real-Time Applications: UDP is commonly used in real-time applications where low latency is crucial, such as audio and video streaming, online gaming, and voice-over-IP (VoIP) communication.&#x20;
* Simple and Stateless: UDP is a stateless protocol, meaning that it does not maintain any state information about the communication.&#x20;
* Each UDP packet is independent of previous or future packets.

## TCP vs UDP

<figure><img src="../../.gitbook/assets/image (186).png" alt=""><figcaption></figcaption></figure>
