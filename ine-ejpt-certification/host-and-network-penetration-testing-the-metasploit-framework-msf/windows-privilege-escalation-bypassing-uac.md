# Windows Privilege Escalation: Bypassing UAC

## Practice Demo

To perform this you need to have a 64-bit meterpreter session on the target.

Enumerate the target

We use the <mark style="color:red;">rejetto exploit</mark> module, and set the payload to a <mark style="color:red;">64-bit meterpreter</mark> payload

We try to privesc with "<mark style="color:red;">getsystem</mark>"..it fails

We enumerate the current privs with "<mark style="color:red;">getprivs</mark>"

### Finding out if a user is part of the Administrators group&#x20;

Move to a shell

#### Enumerating all users

* <mark style="color:yellow;">net user</mark>

#### Enumerating users part of the Administrators group

* <mark style="color:yellow;">net localgroup administrators</mark>

### Bypassing UAC

* <mark style="color:yellow;">exploit/windows/local/bypassuac\_injection</mark>

Change the payload to a 64-bit

Set the LPORT to something different than the current session

In this case we need to set the target option to a 64bit

* <mark style="color:yellow;">set TARGET Windows\ x64</mark>

<mark style="color:purple;">NOTEEEEE:</mark> The reason the initial <mark style="color:red;">getsystem</mark> command failed is because the <mark style="color:red;">first meterpreter</mark> obtained through the rejetto exploit had the <mark style="color:red;">UAC enabled</mark>, thus not letting us access because we are in a terminal. The UAC bypass module created a new meterpreter session with the <mark style="color:red;">UAC disabled</mark>, but still no elevated privileges. But now we can run the <mark style="color:red;">getsystem</mark> command to elevate them.
