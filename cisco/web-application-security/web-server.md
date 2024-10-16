# Web Server

<mark style="color:red;">**Definition:**</mark>

* A web server is software that listens for connections and uses the HTTP protocol to deliver web content to clients.

<mark style="color:red;">**Common Web Server Software:**</mark>

* Apache, Nginx, IIS, NodeJS.

<mark style="color:red;">**Root Directory:**</mark>

* Web servers have a root directory where they store and deliver files.
* Example: Apache and Nginx default to <mark style="color:yellow;">/var/www/html</mark> on Linux; IIS uses <mark style="color:yellow;">C:\inetpub\wwwroot</mark> on Windows.

<mark style="color:red;">**Content Delivery Example:**</mark>

* Requesting [<mark style="color:blue;">http://www.example.com/picture.jpg</mark>](http://www.example.com/picture.jpg) delivers the file <mark style="color:yellow;">/var/www/html/picture.jpg</mark> from the server.

<mark style="color:red;">**Virtual Hosts:**</mark>

* <mark style="color:green;">**Definition:**</mark>
  * Web servers use virtual hosts to host multiple websites with different domain names.
* <mark style="color:green;">**Matching Hostnames:**</mark>
  * The server checks the requested hostname from HTTP headers against virtual hosts.
  * If a match is found, the correct website is provided; otherwise, the default website is used.
* <mark style="color:green;">**Root Directory Mapping:**</mark>
  * Virtual hosts can have root directories mapped to different locations on the hard drive.
* <mark style="color:green;">**No Limit:**</mark>
  * Web servers can host an unlimited number of different websites.

<mark style="color:red;">**Static vs. Dynamic Content:**</mark>

* <mark style="color:green;">**Static Content:**</mark>
  * Never changes; includes pictures, JavaScript, CSS, etc.
  * Served directly from the web server.
* <mark style="color:green;">**Dynamic Content:**</mark>
  * Can change with different requests; for example, blog homepages or search pages.
  * Changes are done in the backend using programming languages.

<mark style="color:red;">**Scripting and Backend Languages:**</mark>

* <mark style="color:green;">**Backend Definition:**</mark>
  * The backend handles processing behind the scenes, making websites interactive.
* <mark style="color:green;">**Backend Languages Examples:**</mark>
  * PHP, Python, Ruby, NodeJS, Perl, etc.
* <mark style="color:green;">**Capabilities:**</mark>
  * Backend languages can interact with databases, call external services, and process user data, making websites dynamic and interactive.
* <mark style="color:green;">**Frontend vs. Backend:**</mark>
  * Frontend is what users see in the browser, while the Backend processes and generates the HTML source.



A very basic PHP example of this would be if you requested the website [<mark style="color:blue;">http://example.com/index.php?name=adam</mark>](http://example.com/index.php?name=adam)\


<mark style="color:red;">If index.php was built like this:</mark>

<mark style="color:blue;">`<html><body>Hello <?php echo $_GET["name"]; ?></body></html>`</mark>

<mark style="color:red;">It would output the following to the client:</mark>

<mark style="color:blue;">`<html><body>Hello adam</body></html>`</mark>

\
