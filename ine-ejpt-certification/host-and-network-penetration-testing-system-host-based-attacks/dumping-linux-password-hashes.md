# Dumping Linux Password Hashes

## Linux Password Hashes

* All of the information for all accounts on Linux is stored in the "passwd" file located in:&#x20;
  * <mark style="color:red;">/etc/passwd</mark>
* We cannot view the passwords for the users in the "passwd" file because they are encrypted and the "passwd" file is readable by any user on the system.
* All the encrypted passwords for the users are stored in the shadow file, it can be found in the following directory:
  * <mark style="color:red;">/etc/shadow</mark>
  * The shadow file can only be accessed and read <mark style="color:orange;">by the root account</mark>, this is a very important security feature as it  prevents other accounts on the system from accessing the hashed passwords.
* The passwd file gives us information in regards to the <mark style="color:orange;">hashing algorithm</mark> that is being used and the password hash,this is very helpful as we are able to determine the type of hashing algorithm that is being used and its strength. We can determine this by looking at the number after the username encapsulated by the dollar symbol <mark style="color:red;">($)</mark>.

<figure><img src="../../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

## Practice Demo

Enumerate the system

In this case we exploit the ftp server version <mark style="color:red;">ProFTPD 1.3.3c</mark>

Used searchsploit to search for exploit.

### Metasploit Module

* <mark style="color:yellow;">exploit/unix/proftpd\_133c\_backdoor</mark>

After upgrading our session to meterpreter using:

* <mark style="color:yellow;">sessions -u 1</mark>

To dump hashes manually we run:

* <mark style="color:yellow;">cat /etc/shadow</mark>

### Dump hashes with Metasploit Module

* <mark style="color:yellow;">post/linux/gather/hashdump</mark>

Set the options and run

This dumps the hashes for the root user on the target system.

Finally we will crack the hash using a new module:

* <mark style="color:yellow;">auxiliary/analyze/crack\_linux</mark>

Set the hash type to "<mark style="color:red;">true</mark>" based on the "$"sign before the hash.
