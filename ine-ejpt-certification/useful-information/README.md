# Useful Information

### WATCH ALL THE SOLUTION VIDEOS OF THE LABS FOR A REMINDER

WHEN COURSE IS FINISHED MAKE A NOTES PAGE FOR EACH SERVICE WITH EVERYTHING RELATED TO IT...SPECIALLY COMMANDS

### Transfer files over scp

* <mark style="color:yellow;">scp /root/payload.exe vagrant@10.2.16.128:C:\\\\</mark>

### Unzip .gz file:

* <mark style="color:yellow;">gzip -d 'nameoffile'</mark>

### Unzip -tar file:

* <mark style="color:yellow;">tar -xf 'nameoffile'</mark>

## Windows Commands

#### Start/Stop services

* <mark style="color:yellow;">net start 'nameofservice'</mark>
* <mark style="color:yellow;">net stop 'nameofservice'</mark>

#### Search for file in given directory&#x20;

* <mark style="color:yellow;">dir C:\example.txt /s</mark>
  * <mark style="color:yellow;">/s:</mark> Search in all subdirectories

#### Change existing user password (Privileged Account necessary)

* <mark style="color:yellow;">net user 'usertochangepass' 'newpassword'</mark>

## Linux Commands

### Managing/Creating Users

#### Add new user

* <mark style="color:yellow;">useradd -m ftp -s /bin/bash</mark>

#### Set password for defined user

* <mark style="color:yellow;">passwd 'user'</mark>

#### Give the user root privileges

<mark style="color:yellow;">usermod -aG root ftp</mark>

#### Change the user ID to make it look like it wasn't just created

* <mark style="color:yellow;">usermod -u 15 ftp</mark>
  * Sets the ID as 15

### System Enumeration

#### Enumerate the distribution release version

* <mark style="color:yellow;">cat /etc/\*issue</mark>

#### Enumerate the kernel version

* <mark style="color:yellow;">uname -r</mark>

#### Enumerate more info

* <mark style="color:yellow;">uname -a</mark>&#x20;

#### List services listening on open ports

* <mark style="color:yellow;">netstat -antp</mark>

#### List all running processes

* <mark style="color:yellow;">ps aux</mark>

#### Enumerate environment variables

* <mark style="color:yellow;">env</mark>







































