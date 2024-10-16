# Networking Fundamentals

## Network Protocols

* In computer networks, hosts communicate with each other through the use of network protocols.
* Network protocols ensure that different computer systems, using different hardware and software can communicate with each other.
* There are a large number of network protocols used by different services for different objectives/functionality.
* Communication between different hosts via protocol is transferred/facilitated through the use of packets.

## Packets

* The primary goal of networking is to exchange information between networked computes; this information is transferred by packets.
* Packets are nothing but streams of bits running as electric signals on physical media used for data transmission. (Ethernet, Wi-fi etc).
* These electrical signals are then interpreted as bits (zeros and ones) that make up the information.

Every packet in every protocol has the following structure.

* <mark style="color:red;">Header</mark>
  * Has a protocol-specific structure: this ensures that the receiving host can correctly interpret the payload and handle the overall communication.
* <mark style="color:red;">Payload</mark>
  * Is the actual information being set.  It could be something like part of an email message or the content of a file during a download.

### OSI Model

* The <mark style="color:red;">OSI (Open Systems Interconnection)</mark> model is a conceptual framework that standardized the functions of a telecommunication or computing system into seven abstraction layers.
* It was developed by ISO to facilitate communication between different systems and devices, ensuring interoperability and understanding across a wide range of networking technologies.
* The OSI model is divided into seven layers, each representing a specific functionality in the process of network communication.

<figure><img src="../../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>
