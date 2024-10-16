# Web Application Technologies

* Understanding web technologies is essential for anyone involved in web development, web application security or web application security testing/web application penetration testing.&#x20;
* As a web application penetration tester, you will be frequently interacting, assessing and exploiting the underlying technologies that make up a web application as a whole.&#x20;
* As a result, you need to have a fundamental understanding of what server-side and client-side technologies make up a web application and what their functionalities are and when and why they are deployed.

## Client-Side Technologies

* <mark style="color:red;">HTML (Hypertext Markup Language)</mark> - HTML is the markup language used to structure and define the content of web pages. It provides the foundation for creating the layout and structure of the UI.&#x20;
* <mark style="color:red;">CSS (Cascading Style Sheets)</mark> - CSS is used to define the presentation and styling of web pages. It allows developers to control the colors, fonts, layout, and other visual aspects of the UI.&#x20;
* <mark style="color:red;">JavaScript</mark> - JavaScript is a scripting language that enables interactivity in web applications. It is used to create dynamic and responsive UI elements, handle user interactions, and perform client-side validations.&#x20;
* <mark style="color:red;">Cookies and Local Storage</mark> - Cookies and local storage are client-side mechanisms to store small amounts of data on the user's browser. They are often used for session management and remembering user preferences.

## Server-Side Technologies

* <mark style="color:red;">Web Server</mark> - The web server is responsible for receiving and responding to HTTP requests from clients (web browsers). It hosts the web application's files, processes requests, and sends responses back to clients. (Apache2, Nginx, Microsoft IIS etc)&#x20;
* <mark style="color:red;">Application Server</mark> - The application server runs the business logic of the web application. It processes user requests, accesses databases, and performs computations to generate dynamic content that the web server can serve to clients.&#x20;
* <mark style="color:red;">Database Server</mark> - The database server stores and manages the web application's data. It stores user information, content, configurations, and other relevant data required for the application's operation. (MySQL, PostgreSQL, MSSQL, Oracle etc)
* <mark style="color:red;">Server-side Scripting Languages</mark> - Server-side scripting languages (e.g., PHP, Python, Java, Ruby) are used to handle server-side processing. They interact with databases, perform validations, and generate dynamic content before sending it to the client.

## Communication & Data Flow

* Web applications communicate over the internet using HTTP (Hypertext Transfer Protocol).&#x20;
* When a user interacts with the web application by clicking on links or submitting forms, the client sends HTTP requests to the server.&#x20;
* The server processes these requests, interacts with the database if necessary, performs the required actions, and generates an HTTP response.&#x20;
* The response is then sent back to the client, which renders the content and presents it to the user.

## Data Interchange

* Data interchange refers to the process of exchanging data between different computer systems or applications, allowing them to communicate and share information.&#x20;
* It is a fundamental aspect of modern computing, enabling interoperability and data sharing between diverse systems, platforms, and technologies.&#x20;
* Data interchange involves the conversion of data from one format to another, making it compatible with the receiving system.&#x20;
* This ensures that data can be interpreted and utilized correctly by the recipient, regardless of the differences in their data structures, programming languages, or operating systems.

## Data Interchange Technologies

* <mark style="color:red;">APIs (Application Programming Interfaces)</mark> - APIs allow different software systems to interact and exchange data. Web applications use APIs to integrate with external services, share data, and provide functionalities to other applications.

## Data Interchange Protocols

* <mark style="color:red;">JSON (JavaScript Object Notation)</mark> - JSON is a lightweight and widely used data interchange format that is easy for both humans and machines to read and write. It is based on JavaScript syntax and primarily used for transmitting data between a server and a web application as an alternative to XML.&#x20;
* <mark style="color:red;">XML (eXtensible Markup Language)</mark> - XML is a versatile data interchange format that uses tags to define the structure of the data. It allows users to create their custom tags and define complex hierarchical data structures. XML is commonly used for configuration files, web services, and data exchange between different systems.
* <mark style="color:red;">REST (Representational State Transfer)</mark> - REST is a software architectural style that uses standard HTTP methods (GET, POST, PUT, DELETE) for data interchange. It is widely used for creating web APIs that allow applications to interact and exchange data over the internet.&#x20;
* <mark style="color:red;">SOAP (Simple Object Access Protocol)</mark> - SOAP is a protocol for exchanging structured information in the implementation of web services. It uses XML as the data interchange format and provides a standardized method for communication between different systems.

## Security Technologies

* <mark style="color:red;">Authentication and Authorization Mechanisms</mark> - Authentication verifies the identity of users, while authorization controls access to different parts of the web application based on user roles and permissions.&#x20;
* <mark style="color:red;">Encryption (SSL/TLS) - SSL (Secure Socket Layer)</mark> or <mark style="color:red;">TLS (Transport Layer Security)</mark> is used to encrypt data transmitted between the client and server, ensuring secure communication and data protection.

## External Technologies

* <mark style="color:red;">Content Delivery Networks (CDNs)</mark> - CDNs are used to distribute static content (e.g., images, CSS files, JavaScript libraries) to multiple servers located worldwide, improving the web application's performance and reliability.&#x20;
* <mark style="color:red;">Third-Party Libraries and Frameworks</mark> - Web applications often leverage third-party libraries and frameworks to speed up development and access advanced features.

## Web Application Architecture

<figure><img src="../../.gitbook/assets/image (137).png" alt=""><figcaption></figcaption></figure>

## How Web Pages Are Rendered

<figure><img src="../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

## How Web Browers Parse Responses

<figure><img src="../../.gitbook/assets/image (139).png" alt=""><figcaption></figcaption></figure>

