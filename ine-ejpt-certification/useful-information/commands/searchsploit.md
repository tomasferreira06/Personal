# Searchsploit

#### Searching for exploits and filtering for only Metasploit modules

* "<mark style="color:yellow;">searchsploit "name of service" | grep -e "Metasploit"</mark>"

Searchsploit's database needs to be kept updated:

* <mark style="color:yellow;">sudo apt-get update && sudo apt-get install exploitdb -y</mark>

The database is at:

* <mark style="color:yellow;">/usr/share/exploitdb</mark>

<figure><img src="../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

## Using searchsploit

#### To update the searchsploit repository:

* <mark style="color:yellow;">searchsploit -u</mark>

#### Search for a exploit

* <mark style="color:yellow;">searchsploit vsftpd 2.3.4</mark>

#### Copy an exploit to your current directory:

* <mark style="color:yellow;">searchsploit -m 'exploitID'</mark>

The ID is the name of the exploit file.

#### Perform a case-sensitive search:

* <mark style="color:yellow;">searchsploit -c OpenSSH</mark>

#### Perform a title search

* <mark style="color:yellow;">searchsploit -t vsftpd</mark>

#### Search for exact matches

* <mark style="color:yellow;">searchsploit -e "Windows XP"</mark>

### Utilize filters used on the exploit-db website

#### Search for exploit for Windows OS that target SMB&#x20;

* <mark style="color:yellow;">searchsploit remote windows smb</mark>

#### Now for buffer overflow for windows

* <mark style="color:yellow;">searchsploit remote windows buffer</mark>

#### Linux exploits ssh

* <mark style="color:yellow;">searchsploit remote linux ssh</mark>

#### Remote WordPress Exploits

* <mark style="color:yellow;">searchsploit remote webapps wordpress</mark>

#### Local Exploit for Windows

* <mark style="color:yellow;">searchsploit local windows</mark>

#### Show links to the exploits online

* <mark style="color:yellow;">searchsploit remote windows smb -w</mark>&#x20;


















