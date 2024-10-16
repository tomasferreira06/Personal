# Dumping Hashes With Hashdump

We can dump Linux user hashes with the hashdump post exploitation module.

* Linux password  hashes are stored in the /etc/shadow file and can <mark style="color:orange;">only be accessed by the root user or users with root privileges.</mark>
* The hashdump module can be used to dump the user account hashes from the <mark style="color:red;">/etc/shadow</mark> file and can also be used to unshadow the hashes for password cracking with John the Ripper.

## Practice Demo

* <mark style="color:yellow;">post/linux/gather/hashdump:</mark> Dumps password hashes

