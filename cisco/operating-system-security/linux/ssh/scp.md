# SCP

Secure copy, or <mark style="color:blue;">SCP</mark>, is just that -- a means of securely copying files.

&#x20;Unlike the regular <mark style="color:yellow;">cp</mark> command, this command allows you to transfer files between two computers using the <mark style="color:yellow;">SSH</mark> protocol to provide both authentication and encryption.

<mark style="color:red;">Working on a model of</mark> <mark style="color:yellow;">SOURCE</mark> <mark style="color:red;">and</mark> <mark style="color:yellow;">DESTINATION</mark><mark style="color:red;">,</mark> <mark style="color:blue;">SCP</mark> <mark style="color:red;">allows you to:</mark>

* Copy files & directories from your current system to a remote system
* Copy files & directories from a remote system to your current system

Provided that we know usernames and passwords for a user on your current system and a user on the remote system. For example, let's copy an example file from our machine to a remote machine:

<figure><img src="../../../../.gitbook/assets/Capture (39).PNG" alt=""><figcaption></figcaption></figure>

With this information, let's craft our <mark style="color:blue;">`scp`</mark> command (remembering that the format of <mark style="color:blue;">SCP</mark> is just <mark style="color:yellow;">SOURCE</mark> and <mark style="color:yellow;">DESTINATION</mark>)

<mark style="color:blue;">`scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`</mark>

And now let's reverse this and layout the syntax for using <mark style="color:blue;">`scp`</mark>to copy a file from a remote computer that we're not logged into:

<figure><img src="../../../../.gitbook/assets/Capture (40).PNG" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">The command will now look like the following:</mark>&#x20;

<mark style="color:blue;">`scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt notes.txt`</mark>&#x20;
