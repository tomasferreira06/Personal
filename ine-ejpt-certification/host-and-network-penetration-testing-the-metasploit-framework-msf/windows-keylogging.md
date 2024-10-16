# Windows Keylogging

* Keylogging is the process of recording or capturing the keystrokes entered on a target system.
* This technique is not limited to post exploitation, there are plenty of programs and USB devices that can be used to capture and transmit the keystroked entered on a system.
* Meterpreter on a Windows sytem provides us with the ability to capture the keystrokes entered on a target system and download them back to our local system.

## Practice Demo

Start the database because the keylogger will save the keystrokes there.

In this case we use the <mark style="color:red;">badblue</mark> module

<mark style="color:purple;">NOTE:</mark> Keylogger in meterpreter only works well when migrated to the <mark style="color:red;">explorer.exe</mark> process.

#### Capture keystrokes

* <mark style="color:yellow;">keyscan\_start</mark>

#### Dump the keystrokes

* <mark style="color:yellow;">keyscan\_dump</mark>
