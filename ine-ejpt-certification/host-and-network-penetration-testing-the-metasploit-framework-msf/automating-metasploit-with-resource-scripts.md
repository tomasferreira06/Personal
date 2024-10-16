# Automating Metasploit With Resource Scripts

* Metasploit resource scripts are a great feature of MSF that allow you to automate repetitive tasks and commands
* They operate similarly to batch scripts, whereby, you can specify a set of Msfconsole commands that you want to execute sequentially.
* You can then load the script with Msfconsole and automate the execution of the commands you specified in the resource script.
* We can use resource scripts to automate various tasks like setting up multi handlers as well as loading and executing payloads.

## Pratice Demo

Kali Linux comes prepackaged with resource scripts in the dreictory <mark style="color:red;">/usr/share/metasploit-framework/scripts/resource/</mark>.

### Generating a resource script to automate the creation of a multi/handler for a specific payload

#### Create the script

* "<mark style="color:yellow;">vim handler.rc</mark>"

#### Contents of the script

<figure><img src="../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

This can be extremely useful for creating default scripts for most of the payloads I use.

#### Load the script

* <mark style="color:yellow;">msfconsole -r pathtoscript</mark>

### Create a resource script to automatically port scan

#### Creating the script

* "<mark style="color:yellow;">vim port\_scan.rc</mark>"

#### Contents of the script

<figure><img src="../../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

#### Loading the script

* "<mark style="color:yellow;">msfconsole -r 'pathtoscript'</mark>"

### Load a resource script from within the msfconsole

* "<mark style="color:yellow;">resource 'pathtoscript</mark>'"

### Creating a resoure script from within the msfconsole

To achieve this the commands need to be run in the msfconsole, and then you can export them into a resource script you define by running:

* "<mark style="color:yellow;">makerc 'pathtofile'</mark>"







