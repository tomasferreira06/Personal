# Pass-The-Hash With PsExec

## Practice Demo

After gaining a meterpreter session as the administrator run:

* <mark style="color:yellow;">pgrep lsass</mark>
* <mark style="color:yellow;">migrate PID</mark>

Get the Administrator NTLM hash.

### Pass-the-Hash using PSExec module

<mark style="color:purple;">NOTE:</mark> To  perform this using PSExec module you need the LM and NTLM hash...use <mark style="color:red;">hashdump</mark> in meterpreter

Background the meterpreter session, to search for the PSExec module.

* <mark style="color:yellow;">exploit/windows/smb/psexec</mark>: Choose the authenticated one

This module accepts <mark style="color:red;">SMBuser</mark> and <mark style="color:red;">SMBpass</mark>.

You can pass it the <mark style="color:blue;">NTLM/LM</mark> hash as the pass.

<mark style="color:purple;">NOTE:</mark> Be aware to set the <mark style="color:red;">LPORT</mark> to be different from the initial session.
