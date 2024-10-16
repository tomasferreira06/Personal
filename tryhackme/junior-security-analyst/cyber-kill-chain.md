# Cyber Kill Chain

<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

This framework defines the steps used by adversaries or malicious actors in cyberspace. To succeed, an adversary needs to go through all phases of the <mark style="color:red;">Kill Chain</mark>. We will go through the attack phases and help you better understand adversaries and their techniques used in the attack to defend yourself.

By understanding the <mark style="color:red;">Kill Chain</mark> as a SOC Analyst, Security Researcher, Threat Hunter, or Incident Responder, you will be able to recognize the intrusion attempts and understand the intruder's goals and objectives.

## Reconnaissance

**Reconnaissance** is discovering and collecting information on the system and the victim. The reconnaissance phase is the planning phase for the adversaries.

OSINT (Open-Source Intelligence) also falls under reconnaissance. OSINT is the first step an attacker needs to complete to carry out the further phases of an attack.

<mark style="color:red;">Email harvesting</mark> is the process of obtaining email addressesfrom public, paid, or free services.&#x20;

An attacker can use email-address harvesting for a <mark style="color:green;">phishing attack</mark> (a type of social-engineering attack used to steal sensitive data, including login credentials and credit card numbers). The attacker will have a big arsenal of tools available for reconnaissance purposes. Here are some of them:

* [theHarvester](https://github.com/laramies/theHarvester) - other than gathering emails, this tool is also capable of gathering names, subdomains, IPs, and URLs using multiple public data sources&#x20;
* [Hunter.io](https://hunter.io/) - this is  an email hunting tool that will let you obtain contact information associated with the domain
* [OSINT Framework](https://osintframework.com/) - <mark style="color:orange;">OSINT Framework</mark> provides the collection of <mark style="color:orange;">OSINT</mark> tools based on various categories

An attacker would also use social media websites such as LinkedIn, Facebook, Twitter, and Instagram to collect information on a specific victim he would want to attack or the company.

## Weaponization

Let's first define some terminology before we analyze the Weaponization phase.\


<mark style="color:red;">Malware</mark> is a program or software that is designed to damage, disrupt, or gain unauthorized access to a computer.

An <mark style="color:red;">exploit</mark> is a program or a code that takes advantage of the vulnerability or flaw in the application or system.

A <mark style="color:red;">payload</mark> is a malicious code that the attacker runs on the system.

In the <mark style="color:green;">Weaponization</mark> phase, the attacker would:

* Create an infected Microsoft Office document containing a malicious macro or VBA (Visual Basic for Applications) scripts.
* An attacker can create a malicious payload or a very sophisticated worm, implant it on the USB drives, and then distribute them in public. An example of the virus.&#x20;
* An attacker would choose <mark style="color:green;">Command and Control (C2)</mark> techniques for executing the commands on the victim's machine or deliver more payloads.
* An attacker would select a backdoor implant (the way to access the computer system, which includes bypassing the security mechanisms).

## Delivery

The Delivery phase is when "Megatron" decides to choose the method for transmitting the payload or the malware. He has plenty of options to choose from:

* <mark style="color:purple;">Phishing /Spear phishing</mark> email: the malicious actor would craft a malicious email that would target either a specific person (spearphishing attack) or multiple people in the company.
* <mark style="color:purple;">USB Drop Attack</mark>: Distributing infected USB drives in public places like coffee shops, parking lots, or on the street.
* <mark style="color:purple;">Watering hole attack</mark>:&#x20;
  * A watering hole attack is a targeted attack designed to aim at a specific group of people by compromising the website they are usually visiting and then redirecting them to the malicious website of an attacker's choice.&#x20;
  * The attacker would look for a known vulnerability for the website and try to exploit it. The attacker would encourage the victims to visit the website by sending "harmless" emails pointing out the malicious URL to make the attack work more efficiently.&#x20;
  * After visiting the website, the victim would unintentionally download malware or a malicious application to their computer.&#x20;
  * This type of attack is called a <mark style="color:red;">drive-by download</mark>. An example can be a malicious pop-up asking to download a fake Browser extension.

## Exploitation

To gain access to the system, an attacker needs to exploit the vulnerability.

After gaining access to the system, the malicious actor could exploit software, system, or server-based vulnerabilities to escalate the privileges or move laterally through the network.&#x20;

According to [CrowdStrike](https://www.crowdstrike.com/cybersecurity-101/lateral-movement/), <mark style="color:red;">lateral movement</mark> refers to the techniques that a malicious actor uses after gaining initial access to the victim's machine to move deeper into a network to obtain sensitive data.&#x20;

These are examples of how an attacker carries out exploitation:

* The victim triggers the exploit by opening the email attachment or clicking on a malicious link.
* Using a <mark style="color:purple;">zero-day exploit</mark>.
* Exploit software, hardware, or even human vulnerabilities.&#x20;
* An attacker triggers the exploit for server-based vulnerabilities.&#x20;

## Installation

As you have learned from the <mark style="color:green;">Weaponization</mark> phase, the backdoor lets an attacker bypass security measures and hide the access. A backdoor is also known as an access point.

Once the attacker gets access to the system, he would want to reaccess the system if he loses the connection to it or if he got detected and got the initial access removed, or if the system is later patched.

The persistence can be achieved through:

* Installing a <mark style="color:purple;">web shell</mark> on the webserver: A web shell is a malicious script written in web development programming languages such as ASP, PHP, or JSP used by an attacker to maintain access to the compromised system. Because of the web shell simplicity and file formatting (<mark style="background-color:orange;">.php, .asp, .aspx, .jsp, etc.</mark>) can be difficult to detect and might be classified as benign.
* Installing a <mark style="color:purple;">backdoo</mark>r on the victim's machine. For example, the attacker can use [Meterpreter ](https://www.offensive-security.com/metasploit-unleashed/meterpreter-backdoor/)to install a backdoor on the victim's machine. <mark style="color:red;">Meterpreter</mark> is a Metasploit Framework payload that gives an interactive shell from which an attacker can interact with the victim's machine remotely and execute the malicious code.
* Creating or modifying Windows services: An attacker can <mark style="color:green;">create</mark> or <mark style="color:green;">modify</mark> the Windows services to execute the malicious scripts or payloads regularly as a part of the persistence.
* Adding the entry to the <mark style="color:orange;">"run keys"</mark> for the malicious payload in the <mark style="color:blue;">Registry</mark> or the <mark style="color:blue;">Startup Folder</mark>. By doing that, the payload will execute each time the user logs in on the computer. According to <mark style="color:red;">MITRE ATT\&CK</mark>, there is a startup folder location for individual user accounts and a system-wide startup folder that will be checked no matter what user account logs in.

## Command and Control (C2)

After getting <mark style="color:green;">persistence</mark> and executing the malware on the victim's machine, "Megatron" opens up the <mark style="color:red;">C2 (Command and Control)</mark> channel through the malware to remotely control and manipulate the victim.&#x20;

This term is also known as <mark style="color:red;">C\&C</mark> or <mark style="color:red;">C2 Beaconing</mark> as a type of malicious communication between a C\&C server and malware on the infected host. The infected host will consistently communicate with the C2 server; that is also where the <mark style="color:purple;">beaconing</mark> term came from.

The most common C2 channels used by adversaries nowadays:

* The protocols <mark style="color:green;">HTTP</mark> on port <mark style="color:blue;">80</mark> and <mark style="color:green;">HTTPS</mark> on port <mark style="color:blue;">443</mark>- this type of beaconing blends the malicious traffic with the legitimate traffic and can help the attacker evade firewalls. &#x20;
* <mark style="color:orange;">DNS (Domain Name Server)</mark>. The infected machine makes constant DNS requests to the DNS server that belongs to an attacker, this type of C2 communication is also known as <mark style="color:orange;">DNS Tunneling</mark>.

## Actions on Objectives (Exfiltration)

After going through six phases of the attack, "Megatron" can finally achieve his goals, which means taking action on the original objectives. With hands-on keyboard access, the attacker can achieve the following:&#x20;

* Collect the credentials from users.
* Perform <mark style="color:orange;">privilege escalation</mark> (gaining elevated access like domain administrator access from a workstation by exploiting the misconfiguration).
* <mark style="color:orange;">Internal reconnaissance</mark> (for example, an attacker gets to interact with internal software to find its vulnerabilities).
* <mark style="color:orange;">Lateral movement</mark> through the company's environment.
* Collect and exfiltrate sensitive data.
* Deleting the backups and shadow copies. Shadow Copy is a Microsoft technology that can create backup copies, snapshots of computer files, or volumes.&#x20;
* Overwrite or corrupt data.







































