# John The Ripper

#### Cracking NTLM hashes with John the Ripper

* <mark style="color:yellow;">john --format=NT  'filewithhashes'</mark>

If you don't specify a password list it will use the default john the rippers list.

#### Using a wordlist

* <mark style="color:yellow;">john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt</mark>

#### Cracking the NTLM hash with John the Ripper

* <mark style="color:yellow;">john --format=sha512crypt pathtothefilefromthemodule --wordlist=/usr/share/wordlists/rockyou.txt</mark>

