# Packets and Frames

<mark style="color:red;">**Packets:**</mark>

* <mark style="color:green;">**Definition:**</mark>
  * Packets are units of data that are transmitted over a network.
  * They are small, self-contained chunks of information.
* <mark style="color:green;">**Contents:**</mark>
  * Include both data and control information.
  * Data can be part of a message, file, or any information being sent.
* <mark style="color:green;">**Headers:**</mark>
  * Contain metadata such as source and destination addresses, sequencing information, and error-checking codes.
* <mark style="color:green;">**Purpose:**</mark>
  * Efficiently divides and transmits data across a network.
  * Allows for the transmission of large amounts of information in manageable chunks.
* <mark style="color:green;">**Examples:**</mark>
  * In the context of the Internet Protocol (IP), data is broken into packets for transmission.

<figure><img src="../../../../.gitbook/assets/Capture (14).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Frames:**</mark>

* <mark style="color:green;">**Definition:**</mark>
  * Frames are the data units at the data link layer (Layer 2) of the OSI model.
  * They encapsulate packets for transmission over a physical network.
* <mark style="color:green;">**Headers and Trailers:**</mark>
  * Contain framing information such as source and destination MAC addresses.
  * May include error-checking information like a Frame Check Sequence (FCS).

<figure><img src="../../../../.gitbook/assets/Capture (15).PNG" alt=""><figcaption></figcaption></figure>

* <mark style="color:green;">**Physical Transmission:**</mark>
  * Frames are the formatted data that is actually transmitted over the physical medium, such as cables.
* <mark style="color:green;">**Switching and Routing:**</mark>
  * Used by network devices like switches and routers to forward data to the correct destination.
* <mark style="color:green;">**Ethernet Frames:**</mark>
  * In Ethernet networks, data is encapsulated into Ethernet frames for transmission over the Ethernet medium.
* <mark style="color:green;">**Error Detection:**</mark>
  * Frames often include error-checking information to ensure data integrity during transmission.



<mark style="color:red;">**In Summary:**</mark>

* <mark style="color:green;">**Packets:**</mark>
  * Units of data at the network layer.
  * Include both data and control information.
* <mark style="color:green;">**Frames:**</mark>
  * Data units at the data link layer.
  * Encapsulate packets for physical transmission.

\
