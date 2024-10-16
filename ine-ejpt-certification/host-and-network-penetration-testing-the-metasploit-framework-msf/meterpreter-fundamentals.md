# Meterpreter Fundamentals

## Post Exploitation

* <mark style="color:red;">Post exploitation</mark> refers to the actions performed on the target system after initial access has been obtained.
* The post exploitation phase of a penetration test consists of various techniques like:
  * <mark style="color:blue;">Local Enumeration</mark>
  * <mark style="color:blue;">Privilege Escalation</mark>
  * <mark style="color:blue;">Dumping Hashes</mark>
  * <mark style="color:blue;">Establishing Persistence</mark>
  * <mark style="color:blue;">Clearing your Tracks</mark>
  * <mark style="color:blue;">Pivoting</mark>

<figure><img src="../../.gitbook/assets/image (233).png" alt=""><figcaption></figcaption></figure>

## Meterpreter

* The Meterpreter payload is an advanced multi-functional payload that operates via <mark style="color:red;">DLL injection</mark> and is executed <mark style="color:blue;">in memory</mark> on the target system, consequently making it difficult to detect.
* It communicates over a stager socket and provides an attacker with an interactive command interpreter on the target system that facilitates the execution of system commands, file system navigation, key logging and much more.
* Meterpreter also allows us to load custom script and plugins dynamically.
* MSF provides us with various types of meterpreter payloads that can be used based on the target environment and the OS architecture.
