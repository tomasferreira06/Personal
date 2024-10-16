# URLs

When we access a website, your browser will need to make requests to a web server for assets such as HTML, Images, and download the responses. Before that, you need to tell the browser specifically how and where to access these resources, this is where <mark style="color:blue;">URLs</mark> will help.



<mark style="color:red;">What is a URL? (Uniform Resource Locator)</mark>

If you’ve used the internet, you’ve used a URL before. A URL is predominantly an instruction on how to access a resource on the internet. The below image shows what a URL looks like with all of its features (it does not use all features in every request).



<figure><img src="../../../../../.gitbook/assets/Capture (24).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">Scheme:</mark>

* &#x20;This instructs on what protocol to use for accessing the resource such as HTTP, HTTPS, FTP (File   Transfer Protocol).

<mark style="color:red;">User:</mark>&#x20;

* Some services require authentication to log in, you can put a username and password into the URL to log in.

<mark style="color:red;">Host:</mark>&#x20;

* The domain name or IP address of the server you wish to access.

<mark style="color:red;">Port:</mark>&#x20;

* The Port that you are going to connect to, usually 80 for HTTP and <mark style="color:blue;">443</mark> for HTTPS, but this can be hosted on any port between <mark style="color:blue;">1 - 65535</mark>.

<mark style="color:red;">Path:</mark>

* &#x20;The file name or location of the resource you are trying to access.

<mark style="color:red;">Query String:</mark>

* &#x20;Extra bits of information that can be sent to the requested path. For example, <mark style="color:blue;">/blog?id=1</mark> would tell the blog path that you wish to receive the blog article with the id of 1.

<mark style="color:red;">Fragment:</mark>&#x20;

* This is a reference to a location on the actual page requested. This is commonly used for pages with long content and can have a certain part of the page directly linked to it, so it is viewable to the user as soon as they access the page.\
