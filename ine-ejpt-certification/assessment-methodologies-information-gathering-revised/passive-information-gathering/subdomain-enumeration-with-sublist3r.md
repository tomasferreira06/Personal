---
description: https://github.com/aboul3la/Sublist3r
---

# Subdomain Enumeration With Sublist3r

## What is Sublist3r?

<mark style="color:red;">Sublist3r</mark> ([https://github.com/aboul3la/Sublist3r](https://github.com/aboul3la/Sublist3r)) is a tool used to discover subdomains of a target domain.&#x20;

### How does it work?

* Queries multiple search engines (like Google, Bing, Yahoo) and services (such as VirusTotal, Netcraft, DNSDumpster) to gather subdomain information

It now has integrated the script "<mark style="color:red;">subbrute</mark>" to increase the possibility of finding more subdomain using bruteforce with an improved wordlist.&#x20;

<mark style="color:purple;">NOTE:</mark> Have in mind that this would be a form of <mark style="color:yellow;">ACTIVE INFORMATION GATHERING.</mark>

To install run:

* <mark style="color:yellow;">sudo apt-get install sublist3r</mark>

To use <mark style="color:red;">sublist3r</mark> run:

* <mark style="color:yellow;">sublist3r -d hackersploit.org</mark>
  * <mark style="color:blue;">"-d"</mark> is for the domain name
  * You can also add the <mark style="color:blue;">"-e"</mark> flag to specify which search engines to use

<mark style="color:purple;">NOTE:</mark> Important to know that "<mark style="color:red;">sublist3r</mark>" makes tons of requests, that can surpass the limit set by google as to what would be a normal user. Using a VPN is an advantage.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>
