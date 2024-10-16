# LAB: SMTP Recon

#### What is the SMTP server name and banner?

```
Server: Postfix
Banner: openmailbox.xyz ESMTP Postfix: Welcome to our mail server.
```

#### Connect to SMTP service using netcat and retrieve the hostname of the server (domain name).

```
openmailbox.xyz
```

#### Does user "admin" exist on the server machine? Connect to SMTP service using netcat and check manually.

```
Yes.
```

<figure><img src="../../.gitbook/assets/image (221).png" alt=""><figcaption></figcaption></figure>

#### Does user "commander" exist on the server machine? Connect to SMTP service using netcat and check manually.

```
No
```

<figure><img src="../../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure>

#### What commands can be used to check the supported commands/capabilities? Connect to SMTP service using telnet and check.

<figure><img src="../../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure>

#### How many of the common usernames present in the dictionary /usr/share/commix/src/txt/usernames.txt exist on the server. Use smtp-user-enum tool for this task.

<figure><img src="../../.gitbook/assets/image (225).png" alt=""><figcaption></figcaption></figure>

#### How many common usernames present in the dictionary /usr/share/metasploit-framework/data/wordlists/unix\_users.txt exist on the server. Use suitable metasploit module for this task.

<figure><img src="../../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

#### Connect to SMTP service using telnet and send a fake mail to root user.

<figure><img src="../../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">**Note:**</mark> There is a dot(.) in the last line which indicates the termination of data.

<figure><img src="../../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>

#### Send a fake mail to root user using sendemail command.

```
sendemail -f admin@attacker.xyz -t root@openmailbox.xyz -s demo.ine.local -u Fakemail -m "Hi root, a fake from admin" -o tls=no
```















