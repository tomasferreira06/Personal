# OSI Model

## What is the OSI Model?

* The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a communication system into seven distinct layers.
* Each layer has specific responsibilities and interacts with the layers above and below it.

## OSI Model Layers

### Physical Layer

* The physical layer is responsible for the transmission and reception of raw unstructured data bits over a physical medium.
* It defines the electrical, mechanical, and functional characteristics of the physical interface between devices.

### Data Link Layer

* The data link layer handles the reliable transmission of data frames between directly connected nodes over a physical link.
* It provides error detection and correction, flow control, and handles access to the physical medium.
* Ethernet, Wi-Fi, and PPP (Point-to-Point Protocol) are examples of data link layer protocols.

### Network Layer

* The network layer enables the routing of data packets across different networks.
* It deals with logical addressing and determines the best path for data delivery based on network conditions and routing protocols.
* The IP (Internet Protocol) is a key network layer protocol.

### Transport Layer

* The transport layer ensures the reliable and orderly delivery of data between end systems.
* It breaks data into smaller segments, manages end-to-end communication, and provides error recovery, flow control, and congestion control.
* TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) operate at this layer.

### Session Layer

* The session layer establishes, manages, and terminates communication sessions between applications.
* It provides synchronization and dialog control mechanisms to enable seamless communication between devices.
* This layer also handles session checkpointing and recovery.

### Presentation Layer

* The presentation layer is responsible for data representation, encryption, compression, and formatting.
* It ensures that data sent by the application layer of one system is understandable by the application layer of another system.
* This layer deals with data syntax and semantics.

### Application Layer

* The application layer is the closest layer to the end-user and provides services directly to user applications.
* It includes protocols for various application-level services such as file transfer, email, web browsing, and remote access.
* Examples of protocols at this layer include HTTP, SMTP, FTP, and DNS.









































