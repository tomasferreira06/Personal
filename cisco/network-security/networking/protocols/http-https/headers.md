# Headers

Headers are additional bits of data you can send to the web server when making requests.

Although no headers are strictly required when making a HTTP request, you’ll find it difficult to view a website properly.\


<mark style="color:red;">Common Request Headers</mark>

﻿These are headers that are sent from the client (usually your browser) to the server.

<mark style="color:green;">Host:</mark>&#x20;

* Some web servers host multiple websites so by providing the host headers you can tell it which one you require, otherwise you'll just receive the default website for the server.

<mark style="color:green;">User-Agent:</mark>&#x20;

* This is your browser software and version number, telling the web server your browser software helps it format the website properly for your browser and also some elements of <mark style="color:blue;">HTML, JavaScript</mark> and <mark style="color:blue;">CSS</mark> are only available in certain browsers.

<mark style="color:green;">Content-Length:</mark>&#x20;

* When sending data to a web server such as in a form, the content length tells the web server how much data to expect in the web request. This way the server can ensure it isn't missing any data.

<mark style="color:green;">Accept-Encoding:</mark>

* &#x20;Tells the web server what types of compression methods the browser supports so the data can be made smaller for transmitting over the internet.\
  Cookie:&#x20;
* Data sent to the server to help remember your information (see cookies task for more information).\


<mark style="color:red;">Common Response Headers</mark>

These are the headers that are returned to the client from the server after a request.

<mark style="color:green;">Set-Cookie:</mark>

* &#x20;Information to store which gets sent back to the web server on each request (see cookies task for more information).

<mark style="color:green;">Cache-Control:</mark>

* &#x20;How long to store the content of the response in the browser's cache before it requests it again.

<mark style="color:green;">Content-Type:</mark>&#x20;

* This tells the client what type of data is being returned, i.e., <mark style="color:blue;">HTML, CSS, JavaScript, Images, PDF, Video</mark>, etc. Using the content-type header the browser then knows how to process the data.

<mark style="color:green;">Content-Encoding:</mark>&#x20;

* What method has been used to compress the data to make it smaller when sending it over the internet.
