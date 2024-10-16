# Commands

## Database/Workspaces

### Installing and initializing PostgreSQL&#x20;

* <mark style="color:yellow;">sudo apt update</mark>
* <mark style="color:yellow;">sudo apt install postgresql postgresql-contrib</mark>
* <mark style="color:yellow;">service postgresql start</mark>
* <mark style="color:yellow;">msfdb init</mark>

### Organizing/Navigating it inside Metasploit

* <mark style="color:yellow;">workspace -a pentest1</mark>: Adds a new workspace called "<mark style="color:green;">pentest1</mark>".
  * <mark style="color:yellow;">-r 'defineworkspace'</mark>: Rename the workspace
* <mark style="color:yellow;">db\_status</mark>: To confirm Metasploit is connected to the database.
* <mark style="color:yellow;">db\_import specifyfile</mark>: Import nmap scan file.
* <mark style="color:yellow;">hosts</mark>: To see the imported nmap results.
* <mark style="color:yellow;">services</mark>: To display open ports and services related to the imported results.
* <mark style="color:yellow;">db\_nmap</mark>: Allows you to run nmap from inside the metasploit framework saving the results automatically to the database and updating the information related to that specific host. You can add whatever flags you like.
* <mark style="color:yellow;">loot</mark>: Lists all the post exploitation information obtained&#x20;
* <mark style="color:yellow;">notes</mark>: Notes from the information gathered by the post exploitation modules

## Autopwn Plugin

Using this plugin to search for exploit modules based on the services saved on the database.

#### Install the plugin

* <mark style="color:yellow;">git clone https://github.com/hahwul/metasploit-autopwn</mark>

Move the <mark style="color:red;">db\_autopwn.rb</mark> to the <mark style="color:green;">/usr/share/metassploitable-framework/plugins</mark> folder

* <mark style="color:yellow;">load db\_autopwn</mark>

To use the plugin just enter

* <mark style="color:yellow;">db\_autopwn</mark>

## Analyze Vulnerabilities for Hosts in the MSF Databse

* <mark style="color:yellow;">analyze</mark>

## Banner Grabbing:

Command "<mark style="color:red;">connect</mark>" is similar to using Netcat

* <mark style="color:yellow;">connect 'targetIP' 'port'</mark>

## Manage Sessions

* <mark style="color:yellow;">sessions</mark>: Lists sessions
* <mark style="color:yellow;">sessions -C sysinfo -i 1</mark>: Run commands without having to interact with the session
  * <mark style="color:yellow;">-C</mark>: Specify the command to run
  * <mark style="color:yellow;">-i</mark>: Specify the ID of the session
  * <mark style="color:yellow;">sessions -k 1</mark>: Kills specified session
    * <mark style="color:yellow;">-K</mark>: Kills all sessions
  * <mark style="color:yellow;">session -n 'name' -i 1</mark>: Name or rename a session
* <mark style="color:yellow;">background</mark>: Background meterpreter session

### Upgrade a session to Meterpreter session

* <mark style="color:yellow;">sessions -u 'numberofsessiontoupgrade'</mark>
  * <mark style="color:yellow;">post/multi/manage/shell\_to\_meterpreter:</mark> We can also use this module

## Meterpreter Session

***

### <mark style="color:red;">Help for any command</mark>

* <mark style="color:yellow;">'command' -h</mark>



### Obtaining  a Shell

* <mark style="color:yellow;">shell</mark>: Pop a shell on the target system
* <mark style="color:yellow;">/bin/bash -i</mark>: Get interactive shell

### Obtaining Current Session info

* <mark style="color:yellow;">getprivs</mark>: Lists current user priviliges
* <mark style="color:yellow;">getuid</mark>: Shows current user

### Execute Commands

* <mark style="color:yellow;">execute -f 'commandtoexecute' -a 'argumentstothecommand'</mark>

### Navigate/Manipulate File System

<mark style="color:red;">When navigating FILE SYSTEM IN METERPRETER USE "\\\\"</mark>

* <mark style="color:yellow;">showmount</mark>: Shows attached drives and mounts
* <mark style="color:yellow;">upload</mark>: Transfers file
* <mark style="color:yellow;">download</mark>: Download file
* <mark style="color:yellow;">edit 'nameoffile</mark>: Let's you edit file
* <mark style="color:yellow;">cat 'file'</mark>: Cats the contents
* <mark style="color:yellow;">search -d /usr/bin -f \*backdoor\*</mark>
  * In this case searching inside the directory /usr/bin
  * <mark style="color:yellow;">-f</mark>: Defines that it is a file
* <mark style="color:yellow;">search -f \*.jpg:</mark> Search for files with ".jpg" extension
* <mark style="color:yellow;">cd</mark>: Navigate file system

### Adding a route to the subnet of the specfied IP

* <mark style="color:yellow;">run autoroute -s 10.1.2.3</mark>
  * <mark style="color:yellow;">-s</mark>: Subnet

### Get the checksum of a file

* <mark style="color:yellow;">checksum md5 /bin/bash</mark>

### Get environment variables

* <mark style="color:yellow;">getenv 'variabletoget'</mark>

### Escalating privileges

* <mark style="color:yellow;">getsystem</mark>: Tries several privesc techniques&#x20;

## Meterpreter on Windows targets

* <mark style="color:yellow;">screenshot</mark>: Takes a screenshot of the target screen (ACTUAL SCREEN)

#### Clearing Windows Event Viewer Logs

* <mark style="color:yellow;">clearev</mark>

### Hash Dumping

<mark style="color:yellow;">hashdump</mark>: Dumps NTLM hashes

* <mark style="color:purple;">NOTE:</mark> Not the same as dumping hashes using the kiwi extension or mimikatz executable.

### Processes

* <mark style="color:yellow;">ps</mark>: Lists processes

#### To elevate from a 32-bit to 64-bit meterpreter session run:

* <mark style="color:yellow;">pgrep 'nameofprocess'</mark>
* <mark style="color:yellow;">migrate 'PID'</mark>

<mark style="color:purple;">NOTE:</mark> Can only be done in a privileged account



\-------------------------------------------------------------------------------

## Metasploit Modules

#### <mark style="color:red;">NOTE: ALWAYS SPECIFY THE "</mark><mark style="color:yellow;">LHOST</mark><mark style="color:red;">" OPTION ON MODULES TO ACTUAL IP OF MACHINE WE ARE USING, NOT THE LOOPBACK.</mark>

### Setting Modules Options

* <mark style="color:yellow;">show targets:</mark> Shows possible OS versions for that exploit
* <mark style="color:yellow;">set target</mark>: Sets the environment (target) in which the exploit will be executed...sometimes it is architecture, OS version, shell types etc...
