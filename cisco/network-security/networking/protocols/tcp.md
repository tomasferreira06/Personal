# TCP

<mark style="color:red;">**Definition:**</mark>&#x20;

* Transmission Control Protocol (TCP) is a connection-oriented, reliable, and widely used transport layer protocol in computer networks.

<mark style="color:red;">**Connection-Oriented:**</mark>

* Establishes a connection before data exchange and ensures reliable, ordered delivery.

<mark style="color:red;">**Reliability Features:**</mark>

* <mark style="color:green;">**Acknowledgment:**</mark>
  * Receives acknowledgments for sent data, ensuring delivery confirmation.
* <mark style="color:green;">**Retransmission:**</mark>
  * Retransmits lost or corrupted packets for reliability.
* <mark style="color:green;">**Flow Control:**</mark>
  * Prevents overwhelming the receiver with too much data by using a sliding window mechanism.
* <mark style="color:green;">**Ordered Data Delivery:**</mark>
  * Ensures that data arrives at the destination in the order it was sent.

<mark style="color:red;">**Three-Way Handshake:**</mark>

* <mark style="color:green;">**SYN (Synchronize):**</mark>
  * Initiates a connection request.
* <mark style="color:green;">**ACK (Acknowledge):**</mark>
  * Acknowledges the SYN and signals acceptance of the connection.
* <mark style="color:green;">**SYN-ACK:**</mark>
  * Acknowledges the ACK, completing the connection establishment.

<mark style="color:red;">**Connection Termination:**</mark>

* <mark style="color:green;">**Four-Way Handshake:**</mark>
  * <mark style="color:purple;">**FIN (Finish):**</mark>
    * Initiates connection termination.
  * <mark style="color:purple;">**ACK (Acknowledge):**</mark>
    * Acknowledges the FIN.
  * <mark style="color:purple;">**FIN-ACK:**</mark>
    * Acknowledges the FIN, indicating agreement to terminate.
  * <mark style="color:purple;">**ACK:**</mark>
    * Final acknowledgment, completing the termination.

<mark style="color:red;">**Ports:**</mark>

* Uses port numbers to identify specific applications on devices.

<mark style="color:red;">**Multiplexing:**</mark>

* Supports multiple applications on a single device by using port numbers.

<mark style="color:red;">**Full-Duplex Communication:**</mark>

* Allows simultaneous two-way communication.

<mark style="color:red;">**Header Information:**</mark>

* Includes source and destination port numbers, sequence and acknowledgment numbers, flags, window size, and checksum.

<figure><img src="../../../../.gitbook/assets/Capture (16).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Commonly Paired with IP:**</mark>

* Often used together with Internet Protocol (IP) to form the TCP/IP protocol suite.

<mark style="color:red;">**Applications:**</mark>

* Widely used for applications such as HTTP (web), FTP (file transfer), and email (SMTP).

In summary, TCP is a connection-oriented, reliable protocol that ensures ordered data delivery, employs a three-way handshake for connection establishment, and supports full-duplex communication. It plays a crucial role in the reliable transmission of data across computer networks.

\
