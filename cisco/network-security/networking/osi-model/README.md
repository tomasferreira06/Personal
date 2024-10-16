# OSI Model

<mark style="color:red;">**Definition:**</mark>&#x20;

* The <mark style="color:yellow;">Open Systems Interconnection (OSI)</mark> Model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers.

<mark style="color:red;">**Layered Structure:**</mark>

* Divides the network communication process into hierarchical layers to simplify design and troubleshooting.

<mark style="color:red;">**Seven Layers:**</mark>

* <mark style="color:green;">**Physical Layer:**</mark>
  * Concerned with the physical connection between devices.
  * Deals with cables, connectors, and transmission of raw bits.
* <mark style="color:green;">**Data Link Layer:**</mark>
  * Manages the reliable transmission of data frames between devices on the same network.
  * Includes protocols like Ethernet and PPP.
* <mark style="color:green;">**Network Layer:**</mark>
  * Handles routing and logical addressing.
  * Involves IP (Internet Protocol) for addressing and routing.
* <mark style="color:green;">**Transport Layer:**</mark>
  * Ensures end-to-end communication, error recovery, and flow control.
  * TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) operate at this layer.
* <mark style="color:green;">**Session Layer:**</mark>
  * Manages sessions or connections between applications.
  * Establishes, maintains, and terminates communication sessions.
* <mark style="color:green;">**Presentation Layer:**</mark>
  * Deals with the syntax and semantics of the data exchanged between applications.
  * Translates data between the application layer and lower layers.
* <mark style="color:green;">**Application Layer:**</mark>
  * Provides a user interface and network services directly to applications.
  * Supports communication between software applications.

<figure><img src="../../../../.gitbook/assets/Capture (13).PNG" alt=""><figcaption></figcaption></figure>



<mark style="color:red;">**Encapsulation:**</mark>

* Each layer adds its own header to the data it receives, creating a protocol data unit (PDU).

<mark style="color:red;">**Decapsulation:**</mark>

* At the receiving end, each layer removes its header, extracting the relevant information.

<mark style="color:red;">**Interoperability:**</mark>

* Allows different vendors to develop protocols for each layer independently, promoting interoperability.

<mark style="color:red;">**Model for Understanding:**</mark>

* Provides a conceptual framework for understanding how different networking protocols interact.

In summary, the OSI Model divides network communication into seven layers, each with specific functions, facilitating a standardized approach to networking protocols and communication.
