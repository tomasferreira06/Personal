# Overview of Windows Vulnerabilities

## A Brief History of Windows Vulnerabilities

* Microsoft Windows is the dominant operating system worldwide with a market share >= 70% as of 2021.
* Over the last 15 years, Windows has had its fair share of severe vulnerabilities, ranging from MS08-067 (Conflicker) to MS17-010 (EternalBlue).
* Given the popularity of Windows, most of these vulnerabilities have publicly accessibe exploit code making them relatively straightforward to exploit.

## Windows Vulnerabilities

* Regardless of the various versions and releases, all Windows OS´s share a likeness given the development model and philosophy.
  * Windows OS´s have been developed in the C programming language, making them vulnerable to buffer overflows, arbitrary code execution etc..
  * By default, Windows is not configured to run securely and require a proactive implementation of security practices in order to configure Windows to run securely.
  * Newly discovered vulnerabilities are not immediately patched by Micrsoft and given the fragmented nature of Windows, many systems are left unpatched.

## Types of Windows Vulnerabilities

* <mark style="color:yellow;">Information disclosure</mark> - Vulnerability that allows an attacker to access confidential data.&#x20;
* <mark style="color:yellow;">Buffer overflows</mark> - Caused by a programming error, allows attackers to write data to a buffer and overrun the allocated buffer, consequently writing data to allocated memory addresses.&#x20;
* <mark style="color:yellow;">Remote code execution</mark> - Vulnerability that allows an attacker to remotely execute code on the target system.&#x20;
* <mark style="color:yellow;">Privilege escalation</mark> - Vulnerability that allows an attacker to elevate their privileges after initial compromise.&#x20;
* <mark style="color:yellow;">Denial of Service (DOS)</mark> - Vulnerability that allows an attacker to consume a system/host’s resources (CPU, RAM, Network etc) consequently preventing the system from functioning normally.
