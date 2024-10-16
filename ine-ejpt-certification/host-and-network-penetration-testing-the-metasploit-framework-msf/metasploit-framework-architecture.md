# Metasploit Framework Architecture

## MSF Architecture

* A module in the context of MSF, is a piece of code that can be utilized by the MSF.
* The MSF libraries facilitate the execution of modules without having to write the code necessary in order to execute them.

<figure><img src="../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

## MSF Modules

* <mark style="color:red;">Exploit</mark> - A module that is used to take advantage of vulnerability and is typically paired with a payload.
* <mark style="color:red;">Payload</mark> - Code that is delivered by MSF and remotely executed on the target after successful exploitation. An example of a payload is a reverse shell that initiates a connection from the target system back to the attacker.
* <mark style="color:red;">Encoder</mark> - Used to encode payloads in order to avoid AV detection. For example, shikata\_ga\_nai is used to encode Windows payloads.
* <mark style="color:red;">NOPS</mark> - Used to ensure that payloads sizes are consistent and ensure the stability of a payload when executed.
* <mark style="color:red;">Auxiliary</mark> - A module that is used to perform additional functionality like port scanning and enumeration.

## MSF Payload Types

When working with exploits, MSF provides you with two types of payloads that can be paired with an exploit:

* <mark style="color:red;">Non-Staged Payload</mark> - Payload that is sent to the target system as is along with the exploit.
* <mark style="color:red;">Staged Payload</mark> - A staged payload is sent to the target in two parts, whereby:
  * The first <mark style="color:red;">(stager)</mark> contains a payload that is used to establish a reverse connection back to the attacker, download the second part of the payload <mark style="color:red;">(Stage)</mark> and execute it.

## Stagers & Stages

* <mark style="color:red;">Stagers</mark> - Stagers are typically used to establish a stable communication channel between the attacker and target, after which a stage payload is downloaded and executed on the target system.
* <mark style="color:red;">Stage</mark> - Payload components that are downloaded by the stager

## Meterpreter Payload

The meterpreter payload is an advanced multi-functional payload that is executed in memory on the target system making it difficult to detect.

It communicates over a stager socket and provides an attacker with an interactive command interpreter on the target system that facilitates the execution of system commands, file system navigation, keylogging and much more.

## MSF File System Structure

The MSF file system is organized in a simple and easy to understand format and is organized into various directories.

## MSF Module Locations

MSF stores modules under the following directory on Linux systems:

* &#x20;<mark style="color:red;">/usr/share/metasploit-framework/modules</mark>

User specified modules are stored under the following directory on Linux systems:

* <mark style="color:red;">\~/-ms4/modules</mark>

## Practical Demo







































