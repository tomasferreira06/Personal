# Website Recon & Footprinting

## What are we looking for?

* IP addresses
* Directories hidden from search engines
* Names
* Email addresses
* Phone Numbers
* Physical Addresses
* Web technologies being used

## Practical Demo

Example site used: <mark style="color:blue;">hackersploit.org</mark>

### Obtain the IP address

*   Use the <mark style="color:red;">host</mark> (DNS lookup utility) command: <mark style="color:yellow;">host hackersploit.org</mark>

    * **Output**: This output shows us that the website is behind a proxy/firewall like CloudFlare.

    &#x20;

    <figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

### Look for information on the website:

* Social media, names, emails etc...
* For the practical demo, the first file searched for was <mark style="color:red;">robots.txt</mark>.
  * <mark style="color:red;">robots.txt</mark> file is a public accessible file that tells search engines which pages it can crawl or not when loading the website.

<figure><img src="../../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

* The second file was <mark style="color:red;">sitemap.xml</mark>:
  * <mark style="color:red;">sitemap.xml</mark> is used to provide search engines with an organized way of indexing the website.

<figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

### Browser Plugins

* <mark style="color:blue;">Built-With</mark> tells you what is running on a certain website
  * Widgets/Plugins
  * Web Technologies/Frameworks
  * Subdomains
* <mark style="color:blue;">Wappalyzer</mark> is another useful plugin with the same purpose of Built-With

#### Another useful utility for web footprinting is <mark style="color:red;">WhatWeb</mark>:

* Comes installed with Kali
* **Command**:
  * <mark style="color:yellow;">whatweb hackersploit.org</mark>

<figure><img src="../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

### Downloading entire website

* If you need to analyse the source code of a website you can use HTTrack to download an entire website to your computer
* **To install**:
  * <mark style="color:yellow;">sudo apt-get install webhttrack</mark>

<figure><img src="../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

Obviously, if a website is behind a <mark style="color:red;">proxy/firewall</mark> like the example website "<mark style="color:blue;">hackersploit.org</mark>" it won't work.
