# Request and Responses

<mark style="color:red;">Making a Request</mark>

It's possible to make a request to a web server with just one line <mark style="color:blue;">"GET / HTTP/1.1".</mark>

<figure><img src="../../../../../.gitbook/assets/Capture (25).PNG" alt=""><figcaption></figcaption></figure>

But for a much richer web experience, you’ll need to send other data as well.&#x20;

This other data is sent in what is called headers, where headers contain extra information to give to the web server you’re communicating with.

<mark style="color:red;">Example Request:</mark>

<figure><img src="../../../../../.gitbook/assets/Capture (26).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">Line 1:</mark>&#x20;

* This request is sending the <mark style="color:blue;">GET</mark> method ( more on this in the HTTP Methods task ), request the home page with / and telling the web server we are using HTTP protocol version 1.1.

<mark style="color:red;">Line 2:</mark>&#x20;

* We tell the web server we want the website <mark style="color:blue;">tryhackme.com</mark>

<mark style="color:red;">Line 3:</mark>

* &#x20;We tell the web server we are using the Firefox version 87 Browser

<mark style="color:red;">Line 4:</mark>&#x20;

* We are telling the web server that the web page that referred us to this one is [<mark style="color:blue;">https://tryhackme.com</mark>](https://tryhackme.com/)

<mark style="color:red;">Line 5:</mark>

* &#x20;HTTP requests always end with a blank line to inform the web server that the request has finished.\


<mark style="color:red;">Example Response:</mark>

<figure><img src="../../../../../.gitbook/assets/Capture (27).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">Line 1:</mark>&#x20;

* HTTP 1.1 is the version of the HTTP protocol the server is using and then followed by the HTTP Status Code in this case "200 Ok" which tells us the request has completed successfully.

<mark style="color:red;">Line 2:</mark>&#x20;

* This tells us the web server software and version number.

<mark style="color:red;">Line 3:</mark>&#x20;

* The current date, time and timezone of the web server.

<mark style="color:red;">Line 4:</mark>&#x20;

* The Content-Type header tells the client what sort of information is going to be sent, such as HTML, images, videos, pdf, XML.

<mark style="color:red;">Line 5:</mark>

* &#x20;Content-Length tells the client how long the response is, this way we can confirm no data is missing.

<mark style="color:red;">Line 6:</mark>

* &#x20;HTTP response contains a blank line to confirm the end of the HTTP response.

<mark style="color:red;">Lines 7-14:</mark>&#x20;

* The information that has been requested, in this instance the homepage.\
