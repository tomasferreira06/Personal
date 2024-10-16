# Web Application Architecture

* Web application architecture refers to the structure and organization of components and technologies used to build a web application.&#x20;
* It defines how different parts of the application interact with each other to deliver its functionality, handle user requests, and manage data.&#x20;
* A well-designed web application architecture is crucial for ensuring scalability, maintainability, and security.&#x20;
* Before performing a security assessment on a web application, it is vitally important to know how web applications work with regards to the underlying architecture.&#x20;
* This knowledge will provide you with a much better understanding of where and how to identify and exploit potential vulnerabilities or misconfigurations in web applications.

## Client-Server Model

* Web applications are typically built on the client-server model. In this architecture, the web application is divided into two main components:&#x20;
  * <mark style="color:red;">Client:</mark> The client represents the user interface and user interaction with the web application. It is the front-end of the application that users access through their web browsers. The client is responsible for displaying the web pages, handling user input, and sending requests to the server for data or actions.&#x20;
  * <mark style="color:red;">Server:</mark> The server represents the back-end of the web application. It processes client requests, executes the application's business logic, communicates with databases and other services, and generates responses to be sent back to the client.

<figure><img src="../../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

## Web Application Components



<figure><img src="../../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

## Client-Side Processing

* Client-side processing involves executing tasks and computations on the user's device, typically within their web browser.&#x20;
* The client-side refers to the user's end of the web application, where the web browser and user interface reside.&#x20;
* Client-side processing has some limitations. It is not suitable for handling sensitive or critical operations, as it can be easily manipulated by users or malicious actors.
* Key characteristics of client-side processing:&#x20;
  * <mark style="color:red;">User Interaction:</mark> Client-side processing is well-suited for tasks that require immediate user interaction and feedback, as there is no need to send data back and forth to the server.&#x20;
  * <mark style="color:red;">Responsive User Experience:</mark> Since processing happens locally, client-side operations can provide a smoother and more responsive user experience.&#x20;
  * <mark style="color:red;">JavaScript:</mark> JavaScript is the primary programming language used for clientside processing. It allows developers to manipulate the web page's content, handle user interactions, and perform validations without involving the server.&#x20;
  * <mark style="color:red;">Data Validation:</mark> Client-side validation ensures that user input meets specific criteria before it is sent to the server, reducing the need to make unnecessary server requests.

## Server-Side Processing

* Server-side processing involves executing tasks and computations on the web server, which is the remote computer where the web application is hosted.&#x20;
* The server-side refers to the backend of the web application, where the business logic and data processing take place.
* Key characteristics of server-side processing:&#x20;
  * <mark style="color:red;">Data Processing:</mark> Server-side processing is ideal for tasks that involve sensitive data handling, complex computations, and interactions with databases or external services.&#x20;
  * <mark style="color:red;">Security</mark>: Since server-side code is executed on a trusted server, it is more secure than client-side code, which can be manipulated by users or intercepted by attackers.&#x20;
  * <mark style="color:red;">Server-side Languages:</mark> Programming languages like PHP, Python, Java, Ruby, and others are commonly used for server-side processing.&#x20;
  * <mark style="color:red;">Data Storage:</mark> Server-side processing enables secure storage and management of sensitive data in databases or other storage systems.

## Communication & Data Flow

* Web applications communicate over the internet using HTTP (Hypertext Transfer Protocol).&#x20;
* When a user interacts with the web application by clicking on links or submitting forms, the client sends HTTP requests to the server.&#x20;
* The server processes these requests, interacts with the database if necessary, performs the required actions, and generates an HTTP response.&#x20;
* The response is then sent back to the client, which renders the content and presents it to the user.
