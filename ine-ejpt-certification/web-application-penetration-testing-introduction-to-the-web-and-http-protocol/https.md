# HTTPS

* Now that you have an understanding of how HTTP works, let us explore how it is secured/protected.&#x20;
* By default, HTTP requests are sent in clear-text and can be easily intercepted or mangled by an attacker on the way to its destination.&#x20;
* Moreover, HTTP does not provide strong authentication between the two communicating parties.&#x20;
* <mark style="color:red;">HTTPS (Hypertext Transfer Protocol Secure)</mark> is a secure version of the HTTP protocol, which is used to transmit data between a user's web browser and a website or web application.&#x20;
* HTTPS provides an added layer of security by encrypting the data transmitted over the internet, making it more secure and protecting it from unauthorized access and interception.
* HTTPS is also commonly referred to as HTTP Secure.&#x20;
* HTTPS is the preferred way to use and configure HTTP and involves running HTTP over <mark style="color:red;">SSL/TLS.</mark>&#x20;
* SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are cryptographic protocols used to provide secure communication over a computer network, most commonly the internet.&#x20;
* They are essential for establishing a secure and encrypted connection between a user's web browser or application and a web server.

This layering technique provides confidentiality, integrity protection and authentication to the HTTP protocol.

<figure><img src="../../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

## HTTPS Advantages

* <mark style="color:red;">Encryption of Data in Transit</mark> - One of the primary benefits of HTTPS is data encryption during transmission. When data is sent over an HTTPS connection, it is encrypted using strong cryptographic algorithms. This ensures that even if an attacker intercepts the data while it's in transit, they cannot decipher or read its contents.&#x20;
* <mark style="color:red;">Protection Against Eavesdropping</mark> - HTTPS prevents unauthorized parties from eavesdropping on the data exchanged between the user's browser and the web server. This is particularly crucial when users input sensitive information, such as login credentials, credit card numbers, or personal details.

## HTTPS Security Considerations

* HTTPS does not protect against web application flaws! Various web application attacks will still work regardless of the use of SSL/TLS. (Attacks like XSS and SQLi will still work)&#x20;
* The added encryption layer only protects data exchanged between the client and the server and does stop attacks against the web application itself.
