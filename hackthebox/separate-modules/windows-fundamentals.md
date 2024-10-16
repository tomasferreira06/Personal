# Windows Fundamentals

## Windows Versions

List of major Windows operating systems and associated version numbers:

<figure><img src="../../.gitbook/assets/image (256).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (257).png" alt=""><figcaption></figcaption></figure>

{% embed url="https://adamtheautomator.com/get-wmiobject/" %}

[https://ss64.com/ps/get-wmiobject.html](https://ss64.com/ps/get-wmiobject.html)

Get-WmiObject - Get instances of WMI classes or information about available WMI classes / Can be used to start and stop services on local and remote computers.

win32\_OperatingSystem - Information about the OS

Win32\_Process - Process Listing

Win32\_Service - listing of services

Win32\_Bios - BIOS information



Some of the most common remote access technologies:

* Virtual Private Networks (VPN)
* Secure Shell (SSH) (Port 22)
* File Transfer Protocol (FTP) (Port 20/21)
* Virtual Network Computing (VNC)
* Windows Remote Management (or Powershell Remoting) (WinRM)
* Remote Desktop Protocol (RDP) (Port 3389)



**Windows Directory structure of the boot partition is as follows:**



<figure><img src="../../.gitbook/assets/image (258).png" alt=""><figcaption></figcaption></figure>

## Windows Fily Systems

There are 5 types of Windows file systems:&#x20;

* FAT12 (no longer used)
* FAT16 (no longer used)
* FAT32&#x20;
* NFTS
* exFAT

FAT32 is widely used across many types of storage devices such as USB and SD cards.&#x20;

The "32" in the name refers to the fact that FAT32 uses 32 bits of data for identifying data clusters on a storage device.

**`Pros of FAT32:`**

* Device compatibility - it can be used on computers, digital cameras, gaming consoles, smartphones, tablets, and more.
* Operating system cross-compatibility - It works on all Windows operating systems starting from Windows 95 and is also supported by MacOS and Linux.

**`Cons of FAT32:`**

* Can only be used with files that are less than 4GB.
* No built-in data protection or file compression features.
* Must use third-party tools for file encryption.

NTFS (New Technology File System) is the default Windows file system since Windows NT 3.1.&#x20;

In addition to making up for the shortcomings of FAT32, NTFS also has better support for metadata and better performance due to improved data structuring.

**`Pros of NTFS:`**

* NTFS is reliable and can restore the consistency of the file system in the event of a system failure or power loss.
* Provides security by allowing us to set granular permissions on both files and folders.
* Supports very large-sized partitions.
* Has journaling built-in, meaning that file modifications (addition, modification, deletion) are logged.

**`Cons of NTFS:`**

* Most mobile devices do not support NTFS natively.
* Older media devices such as TVs and digital cameras do not offer support for NTFS storage devices.

### Permissions

Some of the key permission types of NFTS file system are:

<figure><img src="../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

#### Integrity Control Access Control List (icacls)

[https://ss64.com/nt/icacls.html](https://ss64.com/nt/icacls.html)

* We can list out the NTFS permissions on a specific directory by running either `icacls` from within the working directory or `icacls C:\Windows` against a directory not currently in.

<figure><img src="../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

**The possible inheritance settings are:**

* `(CI)`: container inherit
* `(OI)`: object inherit
* `(IO)`: inherit only
* `(NP)`: do not propagate inherit
* `(I)`: permission inherited from parent container

**Basic access permissions are as follows:**

* `F` : full access
* `D` :  delete access
* `N` :  no access
* `M` :  modify access
* `RX` :  read and execute access
* `R` :  read-only access
* `W` :  write-only access

## SMB

* The Server Message Block protocol is used in Windows to connect shared resources like files and printers.&#x20;
* It is used in large, medium, and small enterprise environments.  &#x20;

<figure><img src="../../.gitbook/assets/image (261).png" alt=""><figcaption></figcaption></figure>

NTFS permissions and share permissions are often understood to be the same. Please know that they are not the same but often apply to the same shared resource.

### Share Permissions

<figure><img src="../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

### NFTS Basic permissions

<figure><img src="../../.gitbook/assets/image (263).png" alt=""><figcaption></figcaption></figure>

### NFTS special permissions

<figure><img src="../../.gitbook/assets/image (264).png" alt=""><figcaption></figcaption></figure>

* NFTS permissions apply to the system where the folder and files are hosted.
* Share permissions apply when the folder is being accessed through SMB, typically from a different system over the network.

#### Using "smbclient" to list available Shares

<figure><img src="../../.gitbook/assets/image (265).png" alt=""><figcaption></figcaption></figure>

#### Connecting to the Company Data Share

<figure><img src="../../.gitbook/assets/image (266).png" alt=""><figcaption></figcaption></figure>

#### Installing CIFS Utilities

```shell-session
TomasFerreira@htb[/htb]$ sudo apt-get install cifs-utils
```

#### Mounting to the Share

```shell-session
TomasFerreira@htb[/htb]$ sudo mount -t cifs -o username=htb-student,password=Academy_WinFun! //ipaddoftarget/"Company Data" /home/user/Desktop/
```



The `net share` command allows us to view all the shared folders on the system.&#x20;

<mark style="color:red;">NOTE</mark>: We didn't manually share C:. The most important drive with the most critical files on a Windows system is shared via SMB at install. This means anyone with the proper access could remotely access the entire C:\ of each Windows system on a network.



Displaying Shares using Net share

<figure><img src="../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

## Windows Services

[https://en.wikipedia.org/wiki/List\_of\_Microsoft\_Windows\_components#Services](https://en.wikipedia.org/wiki/List\_of\_Microsoft\_Windows\_components#Services)

* Windows Services are managed via the Service Control Manager (SCM) system, acessible via the services.msc MMC add-in.
* It is also possible to query and manage services via the command line using `sc.exe` using [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7) cmdlets such as `Get-Service`.

<figure><img src="../../.gitbook/assets/image (202).png" alt=""><figcaption></figcaption></figure>

#### There are 3 categories of services in Windows:

* Local Services
* Network Services
* System Services

### Critical System Services

* In Windows, we have some [critical system services](https://docs.microsoft.com/en-us/windows/win32/rstmgr/critical-system-services) that cannot be stopped and restarted without a system restart.&#x20;
* If we update any file or resource in use by one of these services, we must restart the system.

<figure><img src="../../.gitbook/assets/image (203).png" alt=""><figcaption></figcaption></figure>

## **Processes**

* Processes run in the background on Windows system.&#x20;
* Either started by the OS, or by other installed applications
* Some of this processes, if terminated, will stop certain components of the OS from running properly.



### Local Security Authority Subsystem Service (LSASS)

* <mark style="color:green;">lsass.exe</mark> is the process that is responsible for enforicing the security policy on Windows systems.&#x20;
* When a user attempts to log on to the system, this process verifies their log on attempt and creates access tokens based on the user's permission levels.&#x20;
* <mark style="color:blue;">LSASS</mark> is also responsible for user account password changes.&#x20;
* All events associated with this process (logon/logoff attempts, etc.) are logged within the Windows Security Log.&#x20;
* <mark style="color:blue;">LSASS</mark> is an extremely high-value target as several tools exist to extract both cleartext and hashed credentials stored in memory by this process.



### Sysinternals Tools

* The [SysInternals Tools suite](https://docs.microsoft.com/en-us/sysinternals) is a set of portable Windows applications that can be used to administer Windows systems (for the most part without requiring installation).&#x20;
* The tools can be either downloaded from the Microsoft website or by loading them directly from an internet-accessible file share by typing `\\live.sysinternals.com\tools` into a Windows Explorer window.

For example, we can run procdump.exe directly from this share without downloading it directly to disk.

<figure><img src="../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

* The suite includes tools such as `Process Explorer`, an enhanced version of `Task Manager`, and `Process Monitor`, which can be used to monitor file system, registry, and network activity related to any process running on the system.&#x20;
* Some additional tools are TCPView, which is used to monitor internet activity, and PSExec, which can be used to manage/connect to systems via the SMB protocol remotely.

## Task Manager

* Windows Task Manager provides information about running processes, system performance, running services, startup programs, logged-in users/logged in user processes, and services.

<figure><img src="../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

### Process Explorer

* [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) is a part of the Sysinternals tool suite. This tool can show which handles and DLL processes are loaded when a program runs.&#x20;
* Process Explorer shows a list of currently running processes, and from there, we can see what handles the process has selected in one view or the DLLs and memory-swapped files that have been loaded in another view.&#x20;
* We can also search within the tool to show which processes tie back to a specific handle or DLL.&#x20;
* The tool can also be used to analyze parent-child process relationships to see what child processes are spawned by an application and help troubleshoot any issues such as orphaned processed that can be left behind when a process is terminated.



### Service Permissions

* Services allow for the management of long-running processes and are a critical part of Windows operating systems.
* On server operating systems, critical network services like DHCP and Active Directory Domain Services commonly get installed using the account assigned to the admin performing the install.
* Part of the install process includes assigning a specific service (DHCP for example) to run using the credentials and privileges of a designated user, which by default is set within the currently logged-on user context.

Examining Services using services.msc

* We can use "services.msc" to view and manage just about every detail regarding all services.&#x20;

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

* Knowing the service name is especially useful when using command-line tools to examine and manage services.&#x20;
* Path to the executable is the full path to the program and command to execute when the service starts.&#x20;
* If the NTFS permissions of the destination directory are configured with weak permissions, an attacker could replace the original executable with one created for malicious purposes.

Most services run with LocalSystem privileges by default which is the highest level of access allowed on an individual Windows OS.

&#x20;Not all applications need Local System account-level permissions, so it is beneficial to perform research on a case-by-case basis when considering installing new applications in a Windows environment.&#x20;

It is a good practice to identify applications that can run with the least privileges possible to align with the principle of least privilege.

[Here is one breakdown of the principle of least privilege](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)

Notable built-in service account in Windows:

* LocalService
* NetworkService
* LocalSystem

Note: We can also create new accounts and use them for the sole purpose of running a service.

![](<../../.gitbook/assets/image (6).png>)

The recovery tab allows steps to be configured should a service fail. Notice how this service can be set to run a program after the first failure. This is yet another vector that an attacker could use to run malicious programs by utilizing a legitimate service.



Examining Services using sc

* Sc can also be used to configure and manage services.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

The `sc qc` command is used to query the service. This is where knowing the names of services can come in handy. If we wanted to query a service on a device over the network, we could specify the hostname or IP address immediately after `sc`.

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

We can also use sc to start and stop services.

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

If we were investigating a situation where we suspected that the system had malware, sc would give us the ability to quickly search and analyze commonly targeted services and newly created services. It’s also much more script-friendly than utilizing GUI tools like `services.msc`.

```cmd-session
C:\WINDOWS\system32> sc sdshow wuauserv

D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)S:(AU;FA;CCDCLCSWRPWPDTLOSDRCWDWO;;;WD)
```

Every named object in Windows is a [securable object](https://docs.microsoft.com/en-us/windows/win32/secauthz/securable-objects), and even some unnamed objects are securable. If it's securable in a Windows OS, it will have a [security descriptor](https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptors). Security descriptors identify the object’s owner and a primary group containing a `Discretionary Access Control List` (`DACL`) and a `System Access Control List` (`SACL`).

Generally, a DACL is used for controlling access to an object, and a SACL is used to account for and log access attempts.

This amalgamation of characters crunched together and delimited by opened and closed parentheses is in a format known as the `Security Descriptor Definition Language` (`SDDL`).

```
D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)
```

`D: (A;;CCLCSWRPLORC;;;AU)`

1. D: - the proceeding characters are DACL permissions
2. AU: - defines the security principal Authenticated Users
3. A;; - access is allowed
4. CC - SERVICE\_QUERY\_CONFIG is the full name, and it is a query to the service control manager (SCM) for the service configuration
5. LC - SERVICE\_QUERY\_STATUS is the full name, and it is a query to the service control manager (SCM) for the current status of the service
6. SW - SERVICE\_ENUMERATE\_DEPENDENTS is the full name, and it will enumerate a list of dependent services
7. RP - SERVICE\_START is the full name, and it will start the service
8. LO - SERVICE\_INTERROGATE is the full name, and it will query the service for its current status
9. RC - READ\_CONTROL is the full name, and it will query the security descriptor of the service

As we read the security descriptor, it can be easy to get lost in the seemingly random order of characters, but recall that we are essentially viewing access control entries in an access control list. Each set of 2 characters in between the semi-colons represents actions allowed to be performed by a specific user or group.

`;;CCLCSWRPLORC;;;`

After the last set of semi-colons, the characters specify the security principal (User and/or Group) that is permitted to perform those actions.

`;;;AU`

The character immediately after the opening parentheses and before the first set of semi-colons defines whether the actions are Allowed or Denied.

`A;;`

This entire security descriptor associated with the `Windows Update` (`wuauserv`) service has three sets of access control entries because there are three different security principals. Each security principal has specific permissions applied.



### Examine service permissions using PowerShell

Using the `Get-Acl` PowerShell cmdlet, we can examine service permissions by targeting the path of a specific service in the registry.

Service Permissions

```powershell-session
PS C:\Users\htb-student> Get-ACL -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List

Path   : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\wuauserv
Owner  : NT AUTHORITY\SYSTEM
Group  : NT AUTHORITY\SYSTEM
Access : BUILTIN\Users Allow  ReadKey
         BUILTIN\Users Allow  -2147483648
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadKey
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -2147483648
         S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 Allow
         ReadKey
         S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 Allow
         -2147483648
Audit  :
Sddl   : O:SYG:SYD:AI(A;ID;KR;;;BU)(A;CIIOID;GR;;;BU)(A;ID;KA;;;BA)(A;CIIOID;GA;;;BA)(A;ID;KA;;;SY)(A;CIIOID;GA;;;SY)(A
         ;CIIOID;GA;;;CO)(A;ID;KR;;;AC)(A;CIIOID;GR;;;AC)(A;ID;KR;;;S-1-15-3-1024-1065365936-1281604716-3511738428-1654
         721687-432734479-3232135806-4053264122-3456934681)(A;CIIOID;GR;;;S-1-15-3-1024-1065365936-1281604716-351173842
         8-1654721687-432734479-3232135806-4053264122-3456934681)
```

Notice how this command returns specific account permissions in an easy-to-read format and in SDDL. Also, the SID that represents each security principal (User and/or Group) is present in the SDDL. This is something we do not get when running `sc` from the command prompt.



Windows Sessions

**Interactive**

An interactive, or local logon session, is initiated by a user authenticating to a local or domain system by entering their credentials. An interactive logon can be initiated by logging directly into the system, by requesting a secondary logon session using the `runas` command via the command line, or through a Remote Desktop connection.

**Non-interactive**

Non-interactive accounts in Windows differ from standard user accounts as they do not require login credentials. There are 3 types of non-interactive accounts: the Local System Account, Local Service Account, and the Network Service Account. Non-interactive accounts are generally used by the Windows operating system to automatically start services and applications without requiring user interaction. These accounts have no password associated with them and are usually used to start services when the system boots or to run scheduled tasks.

| Account                 | Description                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local System Account    | Also known as the `NT AUTHORITY\SYSTEM` account, this is the most powerful account in Windows systems. It is used for a variety of OS-related tasks, such as starting Windows services. This account is more powerful than accounts in the local administrators group. |
| Local Service Account   | Known as the `NT AUTHORITY\LocalService` account, this is a less privileged version of the SYSTEM account and has similar privileges to a local user account. It is granted limited functionality and can start some services.                                         |
| Network Service Account | This is known as the `NT AUTHORITY\NetworkService` account and is similar to a standard domain user account. It has similar privileges to the Local Service Account on the local machine. It can establish authenticated sessions for certain network services.        |

Remote Desktop Protocl (RDP)

* [RDP](https://support.microsoft.com/en-us/help/186607/understanding-the-remote-desktop-protocol-rdp) is a proprietary Microsoft protocol which allows a user to connect to a remote system over a network connection and obtain a graphical user interface.&#x20;
* The user connects using RDP client software to a target system running RDP server software.
* &#x20;RDP uses port 3389

S-1–5–21–2614195641–1726409526–3792725429–1006

Execution Policy (Scripts)

Sometimes we will find that we are unable to run scripts on a system. This is due to a security feature called the `execution policy`, which attempts to prevent the execution of malicious scripts. The possible policies are:

| **Policy**     | **Description**                                                                                                                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AllSigned`    | All scripts can run, but a trusted publisher must sign scripts and configuration files. This includes both remote and local scripts. We receive a prompt before running scripts signed by publishers that we have not yet listed as either trusted or untrusted. |
| `Bypass`       | No scripts or configuration files are blocked, and the user receives no warnings or prompts.                                                                                                                                                                     |
| `Default`      | This sets the default execution policy, `Restricted` for Windows desktop machines and `RemoteSigned` for Windows servers.                                                                                                                                        |
| `RemoteSigned` | Scripts can run but requires a digital signature on scripts that are downloaded from the internet. Digital signatures are not required for scripts that are written locally.                                                                                     |
| `Restricted`   | This allows individual commands but does not allow scripts to be run. All script file types, including configuration files (`.ps1xml`), module script files (`.psm1`), and PowerShell profiles (`.ps1`) are blocked.                                             |
| `Undefined`    | No execution policy is set for the current scope. If the execution policy for ALL scopes is set to undefined, then the default execution policy of `Restricted` will be used.                                                                                    |
| `Unrestricted` | This is the default execution policy for non-Windows computers, and it cannot be changed. This policy allows for unsigned scripts to be run but warns the user before running scripts that are not from the local intranet zone.                                 |

Below is an example of changing the execution policy for the current process (session).

```powershell-session
PS C:\htb> Set-ExecutionPolicy Bypass -Scope Process

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
```



Windows Management Instrumentation (WMI)

* MI is a subsystem of PowerShell that provides system administrators with powerful tools for system monitoring.

It is made up of the following components:

| **Component Name** | **Description**                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WMI service        | The Windows Management Instrumentation process, which runs automatically at boot and acts as an intermediary between WMI providers, the WMI repository, and managing applications. |
| Managed objects    | Any logical or physical components that can be managed by WMI.                                                                                                                     |
| WMI providers      | Objects that monitor events/data related to a specific object.                                                                                                                     |
| Classes            | These are used by the WMI providers to pass data to the WMI service.                                                                                                               |
| Methods            | These are attached to classes and allow actions to be performed. For example, methods can be used to start/stop processes on remote machines.                                      |
| WMI repository     | A database that stores all static data related to WMI.                                                                                                                             |
| CIM Object Manager | The system that requests data from WMI providers and returns it to the application requesting it.                                                                                  |
| WMI API            | Enables applications to access the WMI infrastructure.                                                                                                                             |
| WMI Consumer       | Sends queries to objects via the CIM Object Manager.                                                                                                                               |

Some of the uses for WMI are:

* Status information for local/remote systems
* Configuring security settings on remote machines/applications
* Setting and changing user and group permissions
* Setting/modifying system properties
* Code execution
* Scheduling processes
* Setting up logging

WMI can be run via the Windows command prompt by typing `WMIC` to open an interactive shell or by running a command directly such as `wmic computersystem get name` to get the hostname.

```cmd-session
C:\htb> wmic os list brief

BuildNumber  Organization  RegisteredUser  SerialNumber             SystemDirectory      Version
19041                      Owner           00123-00123-00123-AAOEM  C:\Windows\system32  10.0.19041
```

WMIC uses aliases and associated verbs, adverbs, and switches. The above command example uses `LIST` to show data and the adverb `BRIEF` to provide just the core set of properties.&#x20;

WMI can be used with PowerShell by using the `Get-WmiObject` [module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1). This module is used to get instances of WMI classes or information about available classes. This module can be used against local or remote machines.

We can also use the `Invoke-WmiMethod` [module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/invoke-wmimethod?view=powershell-5.1), which is used to call the methods of WMI objects. A simple example is renaming a file.

```powershell-session
PS C:\htb> Invoke-WmiMethod -Path "CIM_DataFile.Name='C:\users\public\spns.csv'" -Name Rename -ArgumentList "C:\Users\Public\kerberoasted_users.csv"


__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 1
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ReturnValue      : 0
PSComputerName   :
```



Microsoft Management Console (MMC)

* The MMC can be used to group snap-ins, or administrative tools, to manage hardware, software, and network components within a Windows host.
* MMC works with the concept of snap-ins, allowing administrators to create a customized console with only the administrative tools needed to manage several services.



Windows Subsystem for Linux (WSL)

* [WSL](https://docs.microsoft.com/en-us/windows/wsl/) is a feature that allows Linux binaries to be run natively on Windows 10 and Windows Server 2019.
* WSL can be installed by running the PowerShell command `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux` as an Administrator.



Windows Security

Security Identifier (SID)

* Each of the security principals on the system has a unique security identifier (SID).
* SIDs are string values with different lengths, which are stored in the security database. These SIDs are added to the user's access token to identify all actions that the user is authorized to take.

A SID consists of the Identifier Authority and the Relative ID (RID). In an Active Directory (AD) domain environment, the SID also includes the domain SID.

```powershell-session
PS C:\htb> whoami /user

USER INFORMATION
----------------

User Name           SID
=================== =============================================
ws01\bob S-1-5-21-674899381-4069889467-2080702030-1002
```

Let's break down the SID piece by piece.

| **Number**                      | **Meaning**          | **Description**                                                                                                                                                                                    |
| ------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S                               | SID                  | Identifies the string as a SID.                                                                                                                                                                    |
| 1                               | Revision Level       | To date, this has never changed and has always been `1`.                                                                                                                                           |
| 5                               | Identifier-authority | A 48-bit string that identifies the authority (the computer or network) that created the SID.                                                                                                      |
| 21                              | Subauthority1        | This is a variable number that identifies the user's relation or group described by the SID to the authority that created it. It tells us in what order this authority created the user's account. |
| 674899381-4069889467-2080702030 | Subauthority2        | Tells us which computer (or domain) created the number                                                                                                                                             |
| 1002                            | Subauthority3        | The RID that distinguishes one account from another. Tells us whether this user is a normal user, a guest, an administrator, or part of some other group                                           |



Security Accounts Manager (SAM) and Access Control Entries (ACE)

* SAM grants rights to a network to execute specific processes.
* The access rights themselves are managed by Access Control Entries (ACE) in Access Control Lists (ACL).
* The ACLs contain ACEs that define which users, groups, or processes have access to a file or to execute a process, for example.



User Account Control (UAC)

* [User Account Control (UAC)](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) is a security feature in Windows to prevent malware from running or manipulating processes that could damage the computer or its contents.

Surely you have already seen the consent prompt if you have installed a specific software, and your system has asked for confirmation if you want to have it installed. Since the installation requires administrator rights, a window pops up, asking you if you want to confirm the installation. With a standard user who has no rights for the installation, execution will be denied, or you will be asked for the administrator password.

The following diagram, illustrates how UAC works.

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Registry

* The [Registry](https://en.wikipedia.org/wiki/Windows\_Registry) is a hierarchical database in Windows critical for the operating system.
* It stores low-level settings for the Windows operating system and applications that choose to use it.
* The entire system registry is stored in several files on the operating system. You can find these under `C:\Windows\System32\Config\`.
* We can open the Registry Editor by typing `regedit` from the command line or Windows search bar.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

The tree-structure consists of main folders (root keys) in which subfolders (subkeys) with their entries/files (values) are located. There are 11 different types of values that can be entered in a subkey.

| **Value**                  | **Type**                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG\_BINARY                | Binary data in any form.                                                                                                                                                                                                                                                                                                                                                                                              |
| REG\_DWORD                 | A 32-bit number.                                                                                                                                                                                                                                                                                                                                                                                                      |
| REG\_DWORD\_LITTLE\_ENDIAN | A 32-bit number in little-endian format. Windows is designed to run on little-endian computer architectures. Therefore, this value is defined as REG\_DWORD in the Windows header files.                                                                                                                                                                                                                              |
| REG\_DWORD\_BIG\_ENDIAN    | A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures.                                                                                                                                                                                                                                                                                                                             |
| REG\_EXPAND\_SZ            | A null-terminated string that contains unexpanded references to environment variables (for example, "%PATH%"). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions. To expand the environment variable references, use the [**ExpandEnvironmentStrings**](https://docs.microsoft.com/en-us/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) function. |
| REG\_LINK                  | A null-terminated Unicode string containing the target path of a symbolic link created by calling the [**RegCreateKeyEx**](https://docs.microsoft.com/en-us/windows/desktop/api/Winreg/nf-winreg-regcreatekeyexa) function with REG\_OPTION\_CREATE\_LINK.                                                                                                                                                            |
| REG\_MULTI\_SZ             | A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: _String1_\0_String2_\0_String3_\0_LastString_\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string.                                    |
| REG\_NONE                  | No defined value type.                                                                                                                                                                                                                                                                                                                                                                                                |
| REG\_QWORD                 | A 64-bit number.                                                                                                                                                                                                                                                                                                                                                                                                      |
| REG\_QWORD\_LITTLE\_ENDIAN | A 64-bit number in little-endian format. Windows is designed to run on little-endian computer architectures. Therefore, this value is defined as REG\_QWORD in the Windows header files.                                                                                                                                                                                                                              |
| REG\_SZ                    | A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions.                                                                                                                                                                                                                                                                                |

Each folder under `Computer` is a key. The root keys all start with `HKEY`. A key such as `HKEY-LOCAL-MACHINE` is abbreviated to `HKLM`. HKLM contains all settings that are relevant to the local system. This root key contains six subkeys like `SAM`, `SECURITY`, `SYSTEM`, `SOFTWARE`, `HARDWARE`, and `BCD`, loaded into memory at boot time (except `HARDWARE` which is dynamically loaded).

















































