---
description: https://github.com/EnableSecurity/wafw00f
---

# WAF With wafw00f

## What is "wafww00f"?

"<mark style="color:red;">wafww00f</mark>" is a web application firewall fingerprinting tool. [https://github.com/EnableSecurity/wafw00f](https://github.com/EnableSecurity/wafw00f)

### How does it work?

* Sends a normal HTTP request and analyses the response, this identifies a number of WAF solutions.
* If that is not sucessful, it sends a number of (potentially malicious) HTTP requests and uses simple logic to deduce which WAF it is
* If that is also not sucessful, it analyses the responses previously returned and uses another simple algorithm to guess if a WAF is actively responding to our attacks

&#x20;The command to run is:

* "<mark style="color:yellow;">wafw00f http://hackersploit.org</mark>"
  * To list all WAF solutions it can detect run "<mark style="color:yellow;">wafw00f -l</mark>"
  * To test for all possible WAF instances run "<mark style="color:yellow;">wafw00f http://hackersploit.org -a</mark>"

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>
