# Pyramid of Pain



## Hash Values (Trivial)

#### Types of Hashes:

* MD5
* SHA1
* SHA2

Security professionals usually use the hash values to gain insight into a specific malware sample, a malicious or a suspicious file, and as a way to uniquely identify and reference the malicious artifact.

## IP Address (Easy)

As a part of the Pyramid of Pain, we’ll evaluate how IP addresses are used as an indicator.\


In the Pyramid of Pain, IP addresses are indicated with the color green. You might be asking why and what you can associate the green colour with?

From a defense standpoint, knowledge of the IP addresses an adversary uses can be valuable. A common defense tactic is to block, drop, or deny inbound requests from IP addresses on your parameter or external firewall.&#x20;

This tactic is often not bulletproof as it’s trivial for an experienced adversary to recover simply by using a new public IP address.



One of the ways an adversary can make it challenging to successfully carry out IP blocking is by using <mark style="color:red;">Fast Flux</mark>.

According to [Akamai](https://blogs.akamai.com/2017/10/digging-deeper-an-in-depth-analysis-of-a-fast-flux-network-part-one.html), <mark style="color:red;">Fast Flux</mark> is a DNS technique used by botnets to hide phishing, web proxying, malware delivery, and malware communication activities behind compromised hosts acting as proxies. The purpose of using the <mark style="color:red;">Fast Flux</mark> network is to make the communication between malware and its <mark style="color:green;">command and control server (C2)</mark> challenging to be discovered by security professionals.&#x20;

## Domain Names (Simple)

Domain Names can be a little more of a pain for the attacker to change as they would most likely need to purchase the domain, register it and modify DNS records.&#x20;

Unfortunately for defenders, many DNS providers have loose standards and provide APIs to make it even easier for the attacker to change the domain.

\
Attackers usually hide the malicious domains under URL Shorteners.

&#x20;A URL Shortener is a tool that creates a short and unique URL that will redirect to the specific website specified during the initial step of setting up the URL Shortener link.

Some used services for shortening the URL are:

* bit.ly
* goo.gl
* ow.ly
* s.id
* smarturl.it
* tiny.pl
* tinyurl.com
* x.co

You can see the actual website the shortened link is redirecting you to by appending "+" to it . Type the shortened URL in the address bar of the web browser and add the above characters to see the redirect URL.

## Host Artifact (Annoying)

Host artifacts are the traces or observables that attackers leave on the system, such as registry values, suspicious process execution, attack patterns or <mark style="color:green;">IOCs (Indicators of Compromise)</mark>, files dropped by malicious applications, or anything exclusive to the current threat.

## Network Artifacts (Annoying)

Network Artifacts also belong to the <mark style="color:yellow;">yellow zone</mark> in the Pyramid of Pain. This means if you can detect and respond to the threat, the attacker would need more time to go back and change his tactics or modify the tools, which gives you more time to respond and detect the upcoming threats or remediate the existing ones.\


A network artifact can be a user-agent string, C2 information, or URI patterns followed by the HTTP POST requests. An attacker might use a <mark style="color:red;">User-Agent</mark> string that hasn’t been observed in your environment before or seems out of the ordinary.&#x20;

The User-Agent is defined by [RFC2616](https://datatracker.ietf.org/doc/html/rfc2616#page-145) as the <mark style="color:green;">request-header</mark> field that contains the information about the user agent originating the request.

Network artifacts can be detected in Wireshark PCAPs (file that contains the packet data of a network) by using a network protocol analyzer such as [TShark](https://www.wireshark.org/docs/wsug\_html\_chunked/AppToolstshark.html) or exploring IDS (Intrusion Detection System) logging from a source such as [Snort](https://www.snort.org/).

## Tools (Challenging)

At this stage, we have levelled﻿ up our detection capabilities against the artifacts. The attacker would most likely give up trying to break into your network or go back and try to create a new tool that serves the same purpose. It will be a game over for the attackers as they would need to invest some money into building a new tool (if they are capable of doing so), find the tool that has the same potential, or even gets some training to learn how to be proficient in a certain tool.&#x20;

Attackers would use the utilities to create malicious macro documents (maldocs) for spearphishing attempts, a backdoor that can be used to establish [C2 (Command and Control Infrastructure)](https://www.varonis.com/blog/what-is-c2/), any custom .EXE, and .DLL files, payloads, or password crackers.

<mark style="color:green;">Fuzzy hashing</mark> is also a strong weapon against the attacker's tools. Fuzzy hashing helps you to perform similarity analysis - match two files with minor differences based on the fuzzy hash values. One of the examples of fuzzy hashing is the usage of [SSDeep](https://ssdeep-project.github.io/ssdeep/index.html); on the SSDeep official website, you can also find the complete explanation for fuzzy hashing.&#x20;

## TTPs  (Tough)

<mark style="color:red;">TTPs</mark> stands for <mark style="color:red;">Tactics, Techniques & Procedures</mark>. This includes the whole [MITRE ](https://attack.mitre.org/)[ATT\&CK Matrix](https://attack.mitre.org/), which means all the steps taken by an adversary to achieve his goal, starting from phishing attempts to persistence and data exfiltration.&#x20;

































































































































