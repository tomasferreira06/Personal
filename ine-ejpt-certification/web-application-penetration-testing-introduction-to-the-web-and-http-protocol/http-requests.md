# HTTP Requests

## HTTP Request Components

### Request Line

* The request line is the first line of an HTTP request and contains the following three components:&#x20;
  * <mark style="color:red;">HTTP method (e.g., GET, POST, PUT, DELETE, etc.)</mark>: Indicates the type of request being made.&#x20;
  * <mark style="color:red;">URL (Uniform Resource Locator)</mark>: The address of the resource the client wants to access.&#x20;
  * <mark style="color:red;">HTTP version:</mark> The version of the HTTP protocol being used (e.g., HTTP/1.1).

### Request Headers

* Headers provide additional information about the request. Common headers include:
  * &#x20;<mark style="color:red;">User-Agent:</mark> Information about the client making the request (e.g., browser type).&#x20;
  * <mark style="color:red;">Host:</mark> The hostname of the server.&#x20;
  * <mark style="color:red;">Accept:</mark> The media types the client can handle in the response (e.g., HTML, JSON).&#x20;
  * <mark style="color:red;">Authorization:</mark> Credentials for authentication, if required.&#x20;
  * <mark style="color:red;">Cookie:</mark> Information stored on the client-side and sent back to the server with each request.

### Request Body (Optional)

Some HTTP methods (like POST or PUT) include a request body where data is sent to the server, typically in JSON or form data format.

## HTTP Request Example

* Let’s examine an HTTP request in detail. The following is the data contained in a request that we send when we navigate to www.google.com with a web browser.

<figure><img src="../../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Headers

* An HTTP request to www.google.com is initiated. What you see here are the headers (HTTP Request Headers) for this request.&#x20;
* Note that a connection to www.google.com on port 80 is initiated before sending HTTP commands to the webserver.

<figure><img src="../../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Methods

* HTTP request methods (HTTP Verbs) provide a standardized way for clients and servers to communicate and interact with resources on the web. The choice of the appropriate method depends on the type of operation that needs to be performed on the resource.&#x20;
* GET is the default request method used when you make a request to a web application, in this case we are trying to connect to www.google.com.

<figure><img src="../../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Methods Explained

<figure><img src="../../.gitbook/assets/image (145).png" alt=""><figcaption></figcaption></figure>

## HTTP Request URL/Path

* The address of the resource/URI the client wants to access.&#x20;
* The home page of a website is always "/". Other pages can be requested, of course, for example: /downloads/index.php.&#x20;
* Your request always refers to the root folder to specify the requested file (hence the leading "/").

<figure><img src="../../.gitbook/assets/image (146).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Protocol

* This is the HTTP protocol version that your browser wants to communicate with (HTTP 1.0/HTTP 1.1).

<figure><img src="../../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Host Header

* This is the beginning of HTTP Request Headers. HTTP Headers have the following structure: Header-name:Header-Value.&#x20;
* The Host header allows a web server to host multiple websites at a single IP address. Our browser is specifying in the Host header which website you are interested in.

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

* After each request header, you will find its corresponding value. In this case we want to access the Host www.google.com.&#x20;
* <mark style="color:purple;">NOTE:</mark> Host value + Path combine to create the full URL you are requesting: the home page of www.google.com/

## HTTP Request User-Agent Header

* The User-Agent is used to specify and send your browser, browser version, operating system and language to the remote web server.&#x20;
* All web browsers have their own user-agent identification string. This is how most web sites recognize the type of browser in use.

<figure><img src="../../.gitbook/assets/image (149).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Accept Header

* The Accept header is used by your browser to specify which document/file types are expected to be returned from the web server as a result of this request.

<figure><img src="../../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Accept-Encoding Header

* The Accept-Encoding header is similar to Accept, and is used to restrict the content encoding that is acceptable in the response.&#x20;
* Content encoding is primarily used to allow a document to be compressed or transformed without losing the original format and without the loss of information.

<figure><img src="../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

## HTTP Request Connection Header

* When using HTTP 1.1, you can maintain/re-use the connection to the remote web server for an unspecified amount of time using the value "keep-alive".&#x20;
* This indicates that all requests to the web server will continue to be sent through this connection without initiating a new connection every time (as in HTTP 1.0).

<figure><img src="../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>
