# SMB Enumeration

## SMB Enumeration

* SMB is a network file sharing protocol that is used to facilitate the sharing of files and peripherals between computers on a local network.
* SMB uses port 445 (TCP). However, originally, SMB ran on top of NetBIOS using port 139.
* SAMBA is the Linux implementation of SMB, and allows Windows systems to access Linux shares and devices.

## Nmblookup Tool

* <mark style="color:yellow;">nmblookup -A demo.ine.local</mark>: Queries NetBIOS names on a network.
  * "<mark style="color:yellow;">-A</mark>": Defines the target.

## SMBClient Tool

* "<mark style="color:yellow;">smbclient -L demo.ine.local -N</mark>": Connecting to smb .
  * "<mark style="color:yellow;">-L</mark>": Defines the host.
  * "<mark style="color:yellow;">-N</mark>": Tries to use anonymous login.

## RPCClient Tool

* <mark style="color:yellow;">'rcpclient -U "" -N demo.ine.local</mark>': Same as SMBClient
  * "<mark style="color:yellow;">-U</mark>": Specified the user for authentication.
  * "<mark style="color:yellow;">-N</mark>": Tells rpcclient to not prompt a password.

## Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_version`**</mark>: Identifies the SMB version and the operating system of the target.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_login`**</mark>: Attempts to brute force SMB login credentials.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_enumshares`**</mark>: Enumerates SMB shares on the target system.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_enumusers`**</mark>: Enumerates SMB users on the target system.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_enum_sessions`**</mark>: Enumerates active SMB sessions on the target.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_enumdomains`**</mark>: Enumerates domain information on an SMB server.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_enum_gpp`**</mark>: Extracts Group Policy Preferences (GPP) password data.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_lsa`**</mark>: Attempts to retrieve Windows Local Security Authority (LSA) secrets from the target.
* <mark style="color:yellow;">**`auxiliary/scanner/smb/smb_uninit_cred`**</mark>: Attempts to exploit an uninitialized credential vulnerability in SMB (MS10-054).
