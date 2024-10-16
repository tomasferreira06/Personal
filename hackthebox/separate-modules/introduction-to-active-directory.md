# Introduction to Active Directory

Active Directory

* Active Directory (AD) is a distributed, hierarchical structure that allows for centralized management of an organization's resources, including users, computers, groups, network devices, file shares, group policies, devices, and trusts.
* Active Directory makes information easy to find and use for administrators and users. AD is highly scalable, supports millions of objects per domain, and allows the creation of additional domains as an organization grows.

<figure><img src="../../.gitbook/assets/image (250).png" alt=""><figcaption></figcaption></figure>



Ransomware operators have been increasingly targeting Active Directory as a key part of their attack paths. The [Conti Ransomware](https://www.cisa.gov/sites/default/files/publications/AA21-265A-Conti\_Ransomware\_TLP\_WHITE.pdf) which has been used in more than 400 attacks around the world has been shown to leverage recent critical Active Directory flaws such as [PrintNightmare (CVE-2021-34527)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) and [Zerologon (CVE-2020-1472)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472) to escalate privileges and move laterally in a target network.



### AD Attacks & Tools Timeline

### 2021

The [PrintNightmare](https://en.wikipedia.org/wiki/PrintNightmare) vulnerability was released. This was a remote code execution flaw in the Windows Print Spooler that could be used to take over hosts in an AD environment. The [Shadow Credentials](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab) attack was released which allows for low privileged users to impersonate other user and computer accounts if conditions are right, and can be used to escalate privileges in a domain. The [noPac](https://www.secureworks.com/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware) attack was released in mid-December of 2021 when much of the security world was focused on the Log4j vulnerabilities. This attack allows an attacker to gain full control over a domain from a standard domain user account if the right conditions exist.

### 2020

The [ZeroLogon](https://blog.malwarebytes.com/exploits-and-vulnerabilities/2021/01/the-story-of-zerologon/) attack debuted late in 2020. This was a critical flaw that allowed an attacker to impersonate any unpatched domain controller in a network.

### 2019

harmj0y delivered the talk ["Kerberoasting Revisited"](https://www.slideshare.net/harmj0y/derbycon-2019-kerberoasting-revisited) at DerbyCon which laid out new approaches to Kerberoasting. Elad Shamir released a [blog post](https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html) outlining techniques for abusing resource-based constrained delegation (RBCD) in Active Directory. The company BC Security released [Empire 3.0](https://github.com/BC-SECURITY/Empire) (now version 4) which was a re-release of the PowerShell Empire framework written in Python3 with many additions and changes.

### 2018

The "Printer Bug" bug was discovered by Lee Christensen and the [SpoolSample](https://github.com/leechristensen/SpoolSample) PoC tool was released which leverages this bug to coerce Windows hosts to authenticate to other machines via the MS-RPRN RPC interface. harmj0y released the [Rubeus toolkit](http://www.harmj0y.net/blog/redteaming/from-kekeo-to-rubeus/) for attacking Kerberos. Late in 2018 harmj0y also released the blog ["Not A Security Boundary: Breaking Forest Trusts"](http://www.harmj0y.net/blog/redteaming/not-a-security-boundary-breaking-forest-trusts/) which presented key research on performing attacks across forest trusts. The [DCShadow](https://www.dcshadow.com/) attack technique was also released by Vincent LE TOUX and Benjamin Delpy at the Bluehat IL 2018 conference. The [Ping Castle](https://github.com/vletoux/pingcastle/commits/master?after=f128d84e86e675f1ad65c4b9b05bd529e1f9dc7c+34\&branch=master) tool was released by Vincent LE TOUX for performing security audits of Active Directory by looking for misconfigurations and other flaws that can raise the risk level of a domain and producing a report that can be used to identify ways to further harden the environment.

### 2017

The [ASREPRoast](http://www.harmj0y.net/blog/activedirectory/roasting-as-reps/) technique was introduced for attacking user accounts that don't require Kerberos preauthentication. \_wald0 and harmj0y delivered the pivotal talk on Active Directory ACL attacks ["ACE Up the Sleeve"](https://www.slideshare.net/harmj0y/ace-up-the-sleeve) at Black Hat and DEF CON. harmj0y released his ["A Guide to Attacking Domain Trusts"](https://www.harmj0y.net/blog/redteaming/a-guide-to-attacking-domain-trusts/) blog post on enumerating and attacking domain trusts.

### 2016

[BloodHound](https://wald0.com/?p=68) was released as a game changing tool for visualizing attack paths in AD at [DEF CON 24](https://www.youtube.com/watch?v=wP8ZCczC1OU).

### 2015

2015 saw the release of some of the most impactful Active Directory tools of all time. The [PowerShell Empire framework](https://github.com/EmpireProject/Empire) was released. [PowerView 2.0](http://www.harmj0y.net/blog/redteaming/powerview-2-0/) released as part of the (now deprecated) [PowerTools](https://github.com/PowerShellEmpire/PowerTools/) repository, which was a part of the PowerShellEmpire GitHub account. The DCSync attack was first released by Benjamin Delpy and Vincent Le Toux as part of the [mimikatz](https://github.com/gentilkiwi/mimikatz/) tool. It has since been included in other tools. The first stable release of CrackMapExec ([(v1.0.0)](https://github.com/byt3bl33d3r/CrackMapExec/releases?page=3) was introduced. Sean Metcalf gave a talk at Black Hat USA about the dangers of Kerberos Unconstrained Delegation and released an excellent [blog post](https://adsecurity.org/?p=1667) on the topic. The [Impacket](https://github.com/SecureAuthCorp/impacket/releases?page=2) toolkit was also released in 2015. This is a collection of Python tools, many of which can be used to perform Active Directory attacks. It is still actively maintained as of January 2022 and is a key part of most every penetration tester's toolkit.

### 2014

Veil-PowerView first [released](https://github.com/darkoperator/Veil-PowerView/commit/fdfd47c0a1e06e529bf31c93da7caed3479d08e1#diff-1695122ff2b5844b625f6d05c9274ce0a8b75b9b7cde84386df07e24ae98181b). This project later became part of the [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) framework as the (no longer supported) [PowerView.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) AD recon tool. The Kerberoasting attack was first presented at a conference by [Tim Medin](https://twitter.com/timmedin) at SANS Hackfest 2014.

### 2013

The [Responder](https://github.com/SpiderLabs/Responder/commits/master?after=c02c74853298ea52a2bfaa4d250c3898886a44ac+174\&branch=master) tool was released by Laurent Gaffie. Responder is a tool used for poisoning LLMNR, NBT-NS, and MDNS on an Active Directory network. It can be used to obtain password hashes and also perform SMB Relay attacks (when combined with other tools) to move laterally and vertically in an AD environment. It has evolved considerably over the years and is still actively supported (with new features added) as of January 2022.



Active Directory Structure

Active Directory flaws and misconfigurations can often be used to obtain a foothold (internal access), move laterally and vertically within a network, and gain unauthorized access to protected resources such as databases, file shares, source code, and more. AD is essentially a large database accessible to all users within the domain, regardless of their privilege level. A basic AD user account with no added privileges can be used to enumerate the majority of objects contained within AD, including but not limited to:

| Domain Computers         | Domain Users                |
| ------------------------ | --------------------------- |
| Domain Group Information | Organizational Units (OUs)  |
| Default Domain Policy    | Functional Domain Levels    |
| Password Policy          | Group Policy Objects (GPOs) |
| Domain Trusts            | Access Control Lists (ACLs) |

At a very (simplistic) high level, an AD structure may look as follows:

```shell-session
INLANEFREIGHT.LOCAL/
├── ADMIN.INLANEFREIGHT.LOCAL
│   ├── GPOs
│   └── OU
│       └── EMPLOYEES
│           ├── COMPUTERS
│           │   └── FILE01
│           ├── GROUPS
│           │   └── HQ Staff
│           └── USERS
│               └── barbara.jones
├── CORP.INLANEFREIGHT.LOCAL
└── DEV.INLANEFREIGHT.LOCAL
```



The graphic below shows two forests, `INLANEFREIGHT.LOCAL` and `FREIGHTLOGISTICS.LOCAL`. The two-way arrow represents a bidirectional trust between the two forests, meaning that users in `INLANEFREIGHT.LOCAL` can access resources in `FREIGHTLOGISTICS.LOCAL` and vice versa. We can also see multiple child domains under each root domain. In this example, we can see that the root domain trusts each of the child domains, but the child domains in forest A do not necessarily have trusts established with the child domains in forest B. This means that a user that is part of `admin.dev.freightlogistics.local` would NOT be able to authenticate to machines in the `wh.corp.inlanefreight.local` domain by default even though a bidirectional trust exists between the top-level `inlanefreight.local` and `freightlogistics.local` domains. To allow direct communication from `admin.dev.freightlogistics.local` and `wh.corp.inlanefreight.local`, another trust would need to be set up.

<figure><img src="../../.gitbook/assets/image (251).png" alt=""><figcaption></figcaption></figure>

Active Directory Terminology

**Object**

An object can be defined as ANY resource present within an Active Directory environment such as OUs, printers, users, domain controllers, etc.

**Attributes**

Every object in Active Directory has an associated set of [attributes](https://docs.microsoft.com/en-us/windows/win32/adschema/attributes-all) used to define characteristics of the given object. A computer object contains attributes such as the hostname and DNS name. All attributes in AD have an associated LDAP name that can be used when performing LDAP queries, such as `displayName` for `Full Name` and `given name` for `First Name`.

**Schema**

The Active Directory [schema](https://docs.microsoft.com/en-us/windows/win32/ad/schema) is essentially the blueprint of any enterprise environment. It defines what types of objects can exist in the AD database and their associated attributes. It lists definitions corresponding to AD objects and holds information about each object.

**Domain**

A domain is a logical group of objects such as computers, users, OUs, groups, etc. We can think of each domain as a different city within a state or country. Domains can operate entirely independently of one another or be connected via trust relationships.

**Forest**

A forest is a collection of Active Directory domains. It is the topmost container and contains all of the AD objects introduced below, including but not limited to domains, users, groups, computers, and Group Policy objects. A forest can contain one or multiple domains and be thought of as a state in the US or a country within the EU. Each forest operates independently but may have various trust relationships with other forests.

**Tree**

A tree is a collection of Active Directory domains that begins at a single root domain. A forest is a collection of AD trees. Each domain in a tree shares a boundary with the other domains. A parent-child trust relationship is formed when a domain is added under another domain in a tree. Two trees in the same forest cannot share a name (namespace). Let's say we have two trees in an AD forest: `inlanefreight.local` and `ilfreight.local`. A child domain of the first would be `corp.inlanefreight.local` while a child domain of the second could be `corp.ilfreight.local`. All domains in a tree share a standard Global Catalog which contains all information about objects that belong to the tree.

**Container**

Container objects hold other objects and have a defined place in the directory subtree hierarchy.

**Leaf**

Leaf objects do not contain other objects and are found at the end of the subtree hierarchy.



**Global Unique Identifier (GUID)**

A [GUID](https://docs.microsoft.com/en-us/windows/win32/adschema/a-objectguid) is a unique 128-bit value assigned when a domain user or group is created. This GUID value is unique across the enterprise, similar to a MAC address. Every single object created by Active Directory is assigned a GUID, not only user and group objects. The GUID is stored in the `ObjectGUID` attribute.

Searching in Active Directory by GUID value is probably the most accurate and reliable way to find the exact object you are looking for, especially if the global catalog may contain similar matches for an object name. Specifying the `ObjectGUID` value when performing AD enumeration will ensure that we get the most accurate results pertaining to the object we are searching for information about. The `ObjectGUID` property `never` changes and is associated with the object for as long as that object exists in the domain.



Security Principals

**Security principals**

[Security principals](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-principals) are anything that the operating system can authenticate, including users, computer accounts, or even threads/processes that run in the context of a user or computer account (i.e., an application such as Tomcat running in the context of a service account within the domain).

**Security Identifier (SID)**

A [security identifier](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-principals), or SID is used as a unique identifier for a security principal or security group. Every account, group, or process has its own unique SID, which, in an AD environment, is issued by the domain controller and stored in a secure database.

**Distinguished Name (DN)**

A [Distinguished Name (DN)](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ldap/distinguished-names) describes the full path to an object in AD (such as `cn=bjones, ou=IT, ou=Employees, dc=inlanefreight, dc=local`). In this example, the user `bjones` works in the IT department of the company Inlanefreight, and his account is created in an Organizational Unit (OU) that holds accounts for company employees. The Common Name (CN) `bjones` is just one way the user object could be searched for or accessed within the domain.

**Relative Distinguished Name (RDN)**

A [Relative Distinguished Name (RDN)](https://docs.microsoft.com/en-us/windows/win32/ad/object-names-and-identities) is a single component of the Distinguished Name that identifies the object as unique from other objects at the current level in the naming hierarchy. In our example, `bjones` is the Relative Distinguished Name of the object. AD does not allow two objects with the same name under the same parent container, but there can be two objects with the same RDNs that are still unique in the domain because they have different DNs. For example, the object `cn=bjones,dc=dev,dc=inlanefreight,dc=local` would be recognized as different from `cn=bjones,dc=inlanefreight,dc=local`.

<figure><img src="../../.gitbook/assets/image (252).png" alt=""><figcaption></figcaption></figure>

**sAMAccountName**

The [sAMAccountName](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#samaccountname) is the user's logon name. Here it would just be `bjones`. It must be a unique value and 20 or fewer characters.

**userPrincipalName**

The [userPrincipalName](https://social.technet.microsoft.com/wiki/contents/articles/52250.active-directory-user-principal-name.aspx) attribute is another way to identify users in AD. This attribute consists of a prefix (the user account name) and a suffix (the domain name) in the format of `bjones@inlanefreight.local`. This attribute is not mandatory.



**FSMO Roles**

[Flexible Single Master Operation (FSMO)](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/fsmo-roles) roles give Domain Controllers (DC) the ability to continue authenticating users and granting permissions without interruption (authorization and authentication).

There are five FSMO roles: `Schema Master` and `Domain Naming Master` (one of each per forest), `Relative ID (RID) Master` (one per domain), `Primary Domain Controller (PDC) Emulator` (one per domain), and `Infrastructure Master` (one per domain).

All five roles are assigned to the first DC in the forest root domain in a new AD forest. Each time a new domain is added to a forest, only the RID Master, PDC Emulator, and Infrastructure Master roles are assigned to the new domain. FSMO roles are typically set when domain controllers are created, but sysadmins can transfer these roles if needed. These roles help replication in AD to run smoothly and ensure that critical services are operating correctly. We will walk through each of these roles in detail later in this section.

**Global Catalog**

A [global catalog (GC)](https://docs.microsoft.com/en-us/windows/win32/ad/global-catalog) is a domain controller that stores copies of ALL objects in an Active Directory forest. The GC stores a full copy of all objects in the current domain and a partial copy of objects that belong to other domains in the forest.

GC is a feature that is enabled on a domain controller and performs the following functions:

* Authentication (provided authorization for all groups that a user account belongs to, which is included when an access token is generated)
* Object search (making the directory structure within a forest transparent, allowing a search to be carried out across all domains in a forest by providing just one attribute about an object.)

**Read-Only Domain Controller (RODC)**

A [Read-Only Domain Controller (RODC)](https://docs.microsoft.com/en-us/windows/win32/ad/rodc-and-active-directory-schema) has a read-only Active Directory database. No AD account passwords are cached on an RODC (other than the RODC computer account & RODC KRBTGT passwords.) No changes are pushed out via an RODC's AD database, SYSVOL, or DNS. RODCs also include a read-only DNS server, allow for administrator role separation, reduce replication traffic in the environment, and prevent SYSVOL modifications from being replicated to other DCs.

**Replication**

[Replication](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts) happens in AD when AD objects are updated and transferred from one Domain Controller to another. Whenever a DC is added, connection objects are created to manage replication between them. These connections are made by the Knowledge Consistency Checker (KCC) service, which is present on all DCs. Replication ensures that changes are synchronized with all other DCs in a forest, helping to create a backup in case one domain controller fails.

**Service Principal Name (SPN)**

A [Service Principal Name (SPN)](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names) uniquely identifies a service instance. They are used by Kerberos authentication to associate an instance of a service with a logon account, allowing a client application to request the service to authenticate an account without needing to know the account name.

**Group Policy Object (GPO)**

[Group Policy Objects (GPOs)](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects) are virtual collections of policy settings. Each GPO has a unique GUID. A GPO can contain local file system settings or Active Directory settings. GPO settings can be applied to both user and computer objects. They can be applied to all users and computers within the domain or defined more granularly at the OU level.\
**Access Control List (ACL)**

An [Access Control List (ACL)](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-lists) is the ordered collection of Access Control Entries (ACEs) that apply to an object.

**Access Control Entries (ACEs)**

Each [Access Control Entry (ACE)](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-entries) in an ACL identifies a trustee (user account, group account, or logon session) and lists the access rights that are allowed, denied, or audited for the given trustee.

**Discretionary Access Control List (DACL)**

DACLs define which security principles are granted or denied access to an object; it contains a list of ACEs. When a process tries to access a securable object, the system checks the ACEs in the object's DACL to determine whether or not to grant access. If an object does NOT have a DACL, then the system will grant full access to everyone, but if the DACL has no ACE entries, the system will deny all access attempts. ACEs in the DACL are checked in sequence until a match is found that allows the requested rights or until access is denied.

**System Access Control Lists (SACL)**

Allows for administrators to log access attempts that are made to secured objects. ACEs specify the types of access attempts that cause the system to generate a record in the security event log.

**Fully Qualified Domain Name (FQDN)**

An FQDN is the complete name for a specific computer or host. It is written with the hostname and domain name in the format \[host name].\[domain name].\[tld]. This is used to specify an object's location in the tree hierarchy of DNS. The FQDN can be used to locate hosts in an Active Directory without knowing the IP address, much like when browsing to a website such as google.com instead of typing in the associated IP address. An example would be the host `DC01` in the domain `INLANEFREIGHT.LOCAL`. The FQDN here would be `DC01.INLANEFREIGHT.LOCAL`.

**Tombstone**

A [tombstone](https://ldapwiki.com/wiki/Tombstone) is a container object in AD that holds deleted AD objects. When an object is deleted from AD, the object remains for a set period of time known as the `Tombstone Lifetime,` and the `isDeleted` attribute is set to `TRUE`. Once an object exceeds the `Tombstone Lifetime`, it will be entirely removed. Microsoft recommends a tombstone lifetime of 180 days to increase the usefulness of backups, but this value may differ across environments. Depending on the DC operating system version, this value will default to 60 or 180 days. If an object is deleted in a domain that does not have an AD Recycle Bin, it will become a tombstone object. When this happens, the object is stripped of most of its attributes and placed in the `Deleted Objects` container for the duration of the `tombstoneLifetime`. It can be recovered, but any attributes that were lost can no longer be recovered.

**AD Recycle Bin**

The [AD Recycle Bin](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/the-ad-recycle-bin-understanding-implementing-best-practices-and/ba-p/396944) was first introduced in Windows Server 2008 R2 to facilitate the recovery of deleted AD objects. This made it easier for sysadmins to restore objects, avoiding the need to restore from backups, restarting Active Directory Domain Services (AD DS), or rebooting a Domain Controller. When the AD Recycle Bin is enabled, any deleted objects are preserved for a period of time, facilitating restoration if needed. Sysadmins can set how long an object remains in a deleted, recoverable state. If this is not specified, the object will be restorable for a default value of 60 days. The biggest advantage of using the AD Recycle Bin is that most of a deleted object's attributes are preserved, which makes it far easier to fully restore a deleted object to its previous state.

**SYSVOL**

The [SYSVOL](https://social.technet.microsoft.com/wiki/contents/articles/8548.active-directory-sysvol-and-netlogon.aspx) folder, or share, stores copies of public files in the domain such as system policies, Group Policy settings, logon/logoff scripts, and often contains other types of scripts that are executed to perform various tasks in the AD environment. The contents of the SYSVOL folder are replicated to all DCs within the environment using File Replication Services (FRS). You can read more about the SYSVOL structure [here](https://networkencyclopedia.com/sysvol-share/#Components-and-Structure).

**AdminSDHolder**

The [AdminSDHolder](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory) object is used to manage ACLs for members of built-in groups in AD marked as privileged. It acts as a container that holds the Security Descriptor applied to members of protected groups. The SDProp (SD Propagator) process runs on a schedule on the PDC Emulator Domain Controller. When this process runs, it checks members of protected groups to ensure that the correct ACL is applied to them. It runs every hour by default. For example, suppose an attacker is able to create a malicious ACL entry to grant a user certain rights over a member of the Domain Admins group. In that case, unless they modify other settings in AD, these rights will be removed (and they will lose any persistence they were hoping to achieve) when the SDProp process runs on the set interval.

**adminCount**

The [adminCount](https://docs.microsoft.com/en-us/windows/win32/adschema/a-admincount) attribute determines whether or not the SDProp process protects a user. If the value is set to `0` or not specified, the user is not protected. If the attribute value is set to `value`, the user is protected. Attackers will often look for accounts with the `adminCount` attribute set to `1` to target in an internal environment. These are often privileged accounts and may lead to further access or full domain compromise.

**sIDHistory**

[This](https://docs.microsoft.com/en-us/defender-for-identity/cas-isp-unsecure-sid-history-attribute) attribute holds any SIDs that an object was assigned previously. It is usually used in migrations so a user can maintain the same level of access when migrated from one domain to another. This attribute can potentially be abused if set insecurely, allowing an attacker to gain prior elevated access that an account had before a migration if SID Filtering (or removing SIDs from another domain from a user's access token that could be used for elevated access) is not enabled.

**NTDS.DIT**

The NTDS.DIT file can be considered the heart of Active Directory. It is stored on a Domain Controller at `C:\Windows\NTDS\` and is a database that stores AD data such as information about user and group objects, group membership, and, most important to attackers and penetration testers, the password hashes for all users in the domain. Once full domain compromise is reached, an attacker can retrieve this file, extract the hashes, and either use them to perform a pass-the-hash attack or crack them offline using a tool such as Hashcat to access additional resources in the domain. If the setting [Store password with reversible encryption](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption) is enabled, then the NTDS.DIT will also store the cleartext passwords for all users created or who changed their password after this policy was set. While rare, some organizations may enable this setting if they use applications or protocols that need to use a user's existing password (and not Kerberos) for authentication.



Active Directory Objects

AD Objects

<figure><img src="../../.gitbook/assets/image (253).png" alt=""><figcaption></figcaption></figure>

Users

* Users are considered `leaf objects`, which means that they cannot contain any other objects within them.
* A user object is considered a security principal and has a security identifier (SID) and a global unique identifier (GUID).
* User objects have many possible [attributes](http://www.kouti.com/tables/userattributes.htm), such as their display name, last login time, date of last password change, email address, account description, manager, address, and more.
* They are a crucial target for attackers since gaining access to even a low privileged user can grant access to many objects and resources and allow for detailed enumeration of the entire domain (or forest).

**Computers**

* A computer object is any computer joined to the AD network (workstation or server).&#x20;
* Computers are `leaf objects` because they do not contain other objects. However, they are considered security principals and have a SID and a GUID.&#x20;
* Like users, they are prime targets for attackers since full administrative access to a computer (as the all-powerful `NT AUTHORITY\SYSTEM` account) grants similar rights to a standard domain user and can be used to perform the majority of the enumeration tasks that a user account can (save for a few exceptions across domain trusts.)



Active Directory Functionality

As mentioned before, there are five Flexible Single Master Operation (FSMO) roles. These roles can be defined as follows:

| **Roles**                  | **Description**                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Schema Master`            | This role manages the read/write copy of the AD schema, which defines all attributes that can apply to an object in AD.                                                                                                                                                                                            |
| `Domain Naming Master`     | Manages domain names and ensures that two domains of the same name are not created in the same forest.                                                                                                                                                                                                             |
| `Relative ID (RID) Master` | The RID Master assigns blocks of RIDs to other DCs within the domain that can be used for new objects. The RID Master helps ensure that multiple objects are not assigned the same SID. Domain object SIDs are the domain SID combined with the RID number assigned to the object to make the unique SID.          |
| `PDC Emulator`             | The host with this role would be the authoritative DC in the domain and respond to authentication requests, password changes, and manage Group Policy Objects (GPOs). The PDC Emulator also maintains time within the domain.                                                                                      |
| `Infrastructure Master`    | This role translates GUIDs, SIDs, and DNs between domains. This role is used in organizations with multiple domains in a single forest. The Infrastructure Master helps them to communicate. If this role is not functioning properly, Access Control Lists (ACLs) will show SIDs instead of fully resolved names. |

Depending on the organization, these roles may be assigned to specific DCs or as defaults each time a new DC is added. Issues with FSMO roles will lead to authentication and authorization difficulties within a domain.

### Domain and Forest Functional Levels

| Domain Functional Level | Features Available                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Supported Domain Controller Operating Systems                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Windows 2000 native     | Universal groups for distribution and security groups, group nesting, group conversion (between security and distribution and security groups), SID history.                                                                                                                                                                                                                                                                                                                               | Windows Server 2008 R2, Windows Server 2008, Windows Server 2003, Windows 2000                                |
| Windows Server 2003     | Netdom.exe domain management tool, lastLogonTimestamp attribute introduced, well-known users and computers containers, constrained delegation, selective authentication.                                                                                                                                                                                                                                                                                                                   | Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2, Windows Server 2008, Windows Server 2003 |
| Windows Server 2008     | Distributed File System (DFS) replication support, Advanced Encryption Standard (AES 128 and AES 256) support for the Kerberos protocol, Fine-grained password policies                                                                                                                                                                                                                                                                                                                    | Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2, Windows Server 2008                      |
| Windows Server 2008 R2  | Authentication mechanism assurance, Managed Service Accounts                                                                                                                                                                                                                                                                                                                                                                                                                               | Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2                                           |
| Windows Server 2012     | KDC support for claims, compound authentication, and Kerberos armoring                                                                                                                                                                                                                                                                                                                                                                                                                     | Windows Server 2012 R2, Windows Server 2012                                                                   |
| Windows Server 2012 R2  | Extra protections for members of the Protected Users group, Authentication Policies, Authentication Policy Silos                                                                                                                                                                                                                                                                                                                                                                           | Windows Server 2012 R2                                                                                        |
| Windows Server 2016     | [Smart card required for interactive logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/interactive-logon-require-smart-card) new [Kerberos](https://docs.microsoft.com/en-us/windows-server/security/kerberos/whats-new-in-kerberos-authentication) features and new [credential protection](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/whats-new-in-credential-protection) features | Windows Server 2019 and Windows Server 2016                                                                   |

A new functional level was not added with the release of Windows Server 2019. However, Windows Server 2008 functional level is the minimum requirement for adding Server 2019 Domain Controllers to an environment. Also, the target domain has to use [DFS-R](https://docs.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview) for SYSVOL replication.

Forest functional levels have introduced a few key capabilities over the years:

| **Version**              | **Capabilities**                                                                                                                                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Windows Server 2003`    | saw the introduction of the forest trust, domain renaming, read-only domain controllers (RODC), and more.                                                                                                      |
| `Windows Server 2008`    | All new domains added to the forest default to the Server 2008 domain functional level. No additional new features.                                                                                            |
| `Windows Server 2008 R2` | Active Directory Recycle Bin provides the ability to restore deleted objects when AD DS is running.                                                                                                            |
| `Windows Server 2012`    | All new domains added to the forest default to the Server 2012 domain functional level. No additional new features.                                                                                            |
| `Windows Server 2012 R2` | All new domains added to the forest default to the Server 2012 R2 domain functional level. No additional new features.                                                                                         |
| `Windows Server 2016`    | [Privileged access management (PAM) using Microsoft Identity Manager (MIM).](https://docs.microsoft.com/en-us/windows-server/identity/whats-new-active-directory-domain-services#privileged-access-management) |

Trusts

A trust is used to establish `forest-forest` or `domain-domain` authentication, allowing users to access resources in (or administer) another domain outside of the domain their account resides in. A trust creates a link between the authentication systems of two domains.

There are several trust types.

| **Trust Type** | **Description**                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Parent-child` | Domains within the same forest. The child domain has a two-way transitive trust with the parent domain.                                                                |
| `Cross-link`   | a trust between child domains to speed up authentication.                                                                                                              |
| `External`     | A non-transitive trust between two separate domains in separate forests which are not already joined by a forest trust. This type of trust utilizes SID filtering.     |
| `Tree-root`    | a two-way transitive trust between a forest root domain and a new tree root domain. They are created by design when you set up a new tree root domain within a forest. |
| `Forest`       | a transitive trust between two forest root domains.                                                                                                                    |

<figure><img src="../../.gitbook/assets/image (255).png" alt=""><figcaption></figcaption></figure>

Trusts can be transitive or non-transitive.

* A transitive trust means that trust is extended to objects that the child domain trusts.
* In a non-transitive trust, only the child domain itself is trusted.

Trusts can be set up to be one-way or two-way (bidirectional).

* In bidirectional trusts, users from both trusting domains can access resources.
* In a one-way trust, only users in a trusted domain can access resources in a trusting domain, not vice-versa. The direction of trust is opposite to the direction of access.



Kerberos, DNS, LDAP, MSRPC

While Windows operating systems use a variety of protocols to communicate, Active Directory specifically requires [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight\_Directory\_Access\_Protocol), Microsoft's version of [Kerberos](https://en.wikipedia.org/wiki/Kerberos\_\(protocol\)), [DNS](https://en.wikipedia.org/wiki/Domain\_Name\_System) for authentication and communication, and [MSRPC](https://ldapwiki.com/wiki/MSRPC) which is the Microsoft implementation of [Remote Procedure Call (RPC)](https://en.wikipedia.org/wiki/Remote\_procedure\_call), an interprocess communication technique used for client-server model-based applications.



Kerberos

* When a user logs into their PC, Kerberos is used to authenticate them via mutual authentication, or both the user and the server verify their identity.
* Kerberos is a stateless authentication protocol based on tickets instead of transmitting user passwords over the network.
* Kerberos uses port 88 (both TCP and UDP).
* When enumerating an Active Directory environment, we can often locate Domain Controllers by performing port scans looking for open port 88 using a tool such as Nmap.

When a user initiates a login request to a system, the client they are using to authenticate requests a ticket from the KDC, encrypting the request with the user's password. If the KDC can decrypt the request (AS-REQ) using their password, it will create a Ticket Granting Ticket (TGT) and transmit it to the user. The user then presents its TGT to a Domain Controller to request a Ticket Granting Service (TGS) ticket, encrypted with the associated service's NTLM password hash. Finally, the client requests access to the required service by presenting the TGS to the application or service, which decrypts it with its password hash. If the entire process completes appropriately, the user will be permitted to access the requested service or application.

**Kerberos Authentication Process**

|                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. The user logs on, and their password is converted to an NTLM hash, which is used to encrypt the TGT ticket. This decouples the user's credentials from requests to resources.                                        |
| 2. The KDC service on the DC checks the authentication service request (AS-REQ), verifies the user information, and creates a Ticket Granting Ticket (TGT), which is delivered to the user.                             |
| 3. The user presents the TGT to the DC, requesting a Ticket Granting Service (TGS) ticket for a specific service. This is the TGS-REQ. If the TGT is successfully validated, its data is copied to create a TGS ticket. |
| 4. The TGS is encrypted with the NTLM password hash of the service or computer account in whose context the service instance is running and is delivered to the user in the TGS\_REP.                                   |
| 5. The user presents the TGS to the service, and if it is valid, the user is permitted to connect to the resource (AP\_REQ).                                                                                            |

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

DNS

* DNS uses TCP and UDP port 53. (UDP being the default)

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

**Forward DNS Lookup**

We can perform a `nslookup` for the domain name and retrieve all Domain Controllers' IP addresses in a domain.

```powershell-session
PS C:\htb> nslookup INLANEFREIGHT.LOCAL

Server:  172.16.6.5
Address:  172.16.6.5

Name:    INLANEFREIGHT.LOCAL
Address:  172.16.6.5
```

**Reverse DNS Lookup**

If we would like to obtain the DNS name of a single host using the IP address, we can do this as follows:

```powershell-session
PS C:\htb> nslookup 172.16.6.5

Server:  172.16.6.5
Address:  172.16.6.5

Name:    ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
Address:  172.16.6.5
```

**Finding IP Address of a Host**

If we would like to find the IP address of a single host, we can do this in reverse. We can do this with or without specifying the FQDN.

```powershell-session
PS C:\htb> nslookup ACADEMY-EA-DC01

Server:   172.16.6.5
Address:  172.16.6.5

Name:    ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
Address:  172.16.6.5
```



### LDAP

* Active Directory supports [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight\_Directory\_Access\_Protocol) for directory lookups.
* LDAP is an open-source and cross-platform protocol used for authentication against various directory services (such as AD).
* LDAP uses port 389, and LDAP over SSL (LDAPS) communicates over port 636.
* LDAP is the language that applications use to communicate with other servers that provide directory services.

An LDAP session begins by first connecting to an LDAP server, also known as a Directory System Agent. The Domain Controller in AD actively listens for LDAP requests, such as security authentication requests.

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

The relationship between AD and LDAP can be compared to Apache and HTTP. The same way Apache is a web server that uses the HTTP protocol, Active Directory is a directory server that uses the LDAP protocol.



**AD LDAP Authentication**

LDAP is set up to authenticate credentials against AD using a "BIND" operation to set the authentication state for an LDAP session. There are two types of LDAP authentication.

1. `Simple Authentication`: This includes anonymous authentication, unauthenticated authentication, and username/password authentication. Simple authentication means that a `username` and `password` create a BIND request to authenticate to the LDAP server.
2. `SASL Authentication`: [The Simple Authentication and Security Layer (SASL)](https://en.wikipedia.org/wiki/Simple\_Authentication\_and\_Security\_Layer) framework uses other authentication services, such as Kerberos, to bind to the LDAP server and then uses this authentication service (Kerberos in this example) to authenticate to LDAP. The LDAP server uses the LDAP protocol to send an LDAP message to the authorization service, which initiates a series of challenge/response messages resulting in either successful or unsuccessful authentication. SASL can provide additional security due to the separation of authentication methods from application protocols.

<mark style="color:red;">NOTE:</mark>LDAP authentication messages are sent in cleartext by default so anyone can sniff out LDAP messages on the internal network. It is recommended to use TLS encryption or similar to safeguard this information in transit.



### MSRPC

* Windows systems use MSRPC to access systems in Active Directory using four key RPC interfaces.

| Interface Name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lsarpc`       | A set of RPC calls to the [Local Security Authority (LSA)](https://networkencyclopedia.com/local-security-authority-lsa/) system which manages the local security policy on a computer, controls the audit policy, and provides interactive authentication services. LSARPC is used to perform management on domain security policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `netlogon`     | Netlogon is a Windows process used to authenticate users and other services in the domain environment. It is a service that continuously runs in the background.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `samr`         | Remote SAM (samr) provides management functionality for the domain account database, storing information about users and groups. IT administrators use the protocol to manage users, groups, and computers by enabling admins to create, read, update, and delete information about security principles. Attackers (and pentesters) can use the samr protocol to perform reconnaissance about the internal domain using tools such as [BloodHound](https://github.com/BloodHoundAD/) to visually map out the AD network and create "attack paths" to illustrate visually how administrative access or full domain compromise could be achieved. Organizations can [protect](https://stealthbits.com/blog/making-internal-reconnaissance-harder-using-netcease-and-samri1o/) against this type of reconnaissance by changing a Windows registry key to only allow administrators to perform remote SAM queries since, by default, all authenticated domain users can make these queries to gather a considerable amount of information about the AD domain. |
| `drsuapi`      | drsuapi is the Microsoft API that implements the Directory Replication Service (DRS) Remote Protocol which is used to perform replication-related tasks across Domain Controllers in a multi-DC environment. Attackers can utilize drsuapi to [create a copy of the Active Directory domain database](https://attack.mitre.org/techniques/T1003/003/) (NTDS.dit) file to retrieve password hashes for all accounts in the domain, which can then be used to perform Pass-the-Hash attacks to access more systems or cracked offline using a tool such as Hashcat to obtain the cleartext password to log in to systems using remote management protocols such as Remote Desktop (RDP) and WinRM.                                                                                                                                                                                                                                                                                                                                                           |



NTLM Authentication

Active Directory uses several other authentication methods which can be used (and abused) by applications and services in AD. These include:

* LM (Hash)
* NTLM (Hash)
* NTLMv1 (Authentication Protocol)
* &#x20;NTLMv2 (Authentication Protocol)

**Hash Protocol Comparison**

| **Hash/Protocol** | **Cryptographic technique**                          | **Mutual Authentication** | **Message Type**                | **Trusted Third Party**                         |
| ----------------- | ---------------------------------------------------- | ------------------------- | ------------------------------- | ----------------------------------------------- |
| `NTLM`            | Symmetric key cryptography                           | No                        | Random number                   | Domain Controller                               |
| `NTLMv1`          | Symmetric key cryptography                           | No                        | MD4 hash, random number         | Domain Controller                               |
| `NTLMv2`          | Symmetric key cryptography                           | No                        | MD4 hash, random number         | Domain Controller                               |
| `Kerberos`        | Symmetric key cryptography & asymmetric cryptography | Yes                       | Encrypted ticket using DES, MD5 | Domain Controller/Key Distribution Center (KDC) |

LM

* `LAN Manager` (LM or LANMAN) hashes are the oldest password storage mechanism used by the Windows operating system.
* If in use, they are stored in the SAM database on a Windows host and the NTDS.DIT database on a Domain Controller.
* Passwords using LM are limited to a maximum of `14` characters. Passwords are not case sensitive and are converted to uppercase before generating the hashed value, limiting the keyspace to a total of 69 characters making it relatively easy to crack these hashes using a tool such as Hashcat.
* Due to significant security weaknesses in the hashing algorithm used for LM hashes, it has been turned off by defautl since Windows Vista/Server 2008.
* An LM hash takes the form of `299bd128c1101fd6`.

<mark style="color:red;">NOTE:</mark> Windows operating systems prior to Windows Vista and Windows Server 2008 (Windows NT4, Windows 2000, Windows 2003, Windows XP) stored both the LM hash and the NTLM hash of a user's password by default.



### NTHash (NTLM)

* `NT LAN Manager` (NTLM) hashes are used on modern Windows systems.
* It is a challenge-response authentication protocol and uses three messages to authenticate:
  * &#x20;a client first sends a `NEGOTIATE_MESSAGE` to the server
  * The server response  is a `CHALLENGE_MESSAGE` to verify the client's identity.
  * Lastly, the client responds with an `AUTHENTICATE_MESSAGE`.
* These hashes are stored locally in the SAM database or the NTDS.DIT database file on a Domain Controller.
* The algorithm can be visualized as: `MD4(UTF-16-LE(password))`.

**NTLM Authentication Request**

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Even though they are considerably stronger than LM hashes (supporting the entire Unicode character set of 65,536 characters), they can still be brute-forced offline relatively quickly using a tool such as Hashcat.

An NT hash takes the form of `b4b9b02e6f09a9bd760f388b67351e2b`, which is the second half of the full NTLM hash. An NTLM hash looks like this:

&#x20; NTLM Authentication

```shell-session
Rachel:500:aad3c435b514a4eeaad3b935b51304fe:e46b9e548fa0d122de7f59fb6d48eaa2:::
```

Looking at the hash above, we can break the NTLM hash down into its individual parts:

* `Rachel` is the username
* `500` is the Relative Identifier (RID). 500 is the known RID for the `administrator` account
* `aad3c435b514a4eeaad3b935b51304fe` is the LM hash and, if LM hashes are disabled on the system, can not be used for anything
* `e46b9e548fa0d122de7f59fb6d48eaa2` is the NT hash. This hash can either be cracked offline to reveal the cleartext value (depending on the length/strength of the password) or used for a pass-the-hash attack. Below is an example of a successful pass-the-hash attack using the [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) tool:

```shell-session
TomasFerreira@htb[/htb]$ crackmapexec smb 10.129.41.19 -u rachel -H e46b9e548fa0d122de7f59fb6d48eaa2

SMB         10.129.43.9     445    DC01      [*] Windows 10.0 Build 17763 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.43.9     445    DC01      [+] INLANEFREIGHT.LOCAL\rachel:e46b9e548fa0d122de7f59fb6d48eaa2 (Pwn3d!)
```

<mark style="color:red;">NOTE:</mark> Neither LANMAN nor NTLM uses a salt.



### NTLMv1 (Net-NTLMv1)

* NTLMv1 uses both the NT and the LM hash, which can make it easier to "crack" offline after capturing a hash using a tool such as [Responder](https://github.com/lgandx/Responder) or via an [NTLM relay attack](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html).
* The protocol is used for network authentication, and the Net-NTLMv1 hash itself is created from a challenge/response algorithm.
* The server sends the client an 8-byte random number (challenge), and the client returns a 24-byte response.
* These hashes can <mark style="color:red;">NOT</mark> be used for pass-the-hash attacks.

The algorithm looks as follows:

**V1 Challenge & Response Algorithm**

&#x20; NTLM Authentication

```shell-session
C = 8-byte server challenge, random
K1 | K2 | K3 = LM/NT-hash | 5-bytes-0
response = DES(K1,C) | DES(K2,C) | DES(K3,C)
```

**NTLMv1 Hash Example**

&#x20; NTLM Authentication

```shell-session
u4-netntlm::kNS:338d08f8e26de93300000000000000000000000000000000:9526fb8c23a90751cdd619b6cea564742e1e4bf33006ba41:cb8086049ec4736c
```

NTLMv1 was the building block for modern NTLM authentication.



### NTLMv2 (Net-NTLMv2)

* The NTLMv2 protocol was first introduced in Windows NT 4.0 SP4 and was created as a stronger alternative to NTLMv1.
* It works as follows.
  * NTLMv2 sends two responses to the 8-byte challenge received by the server.&#x20;
  * These responses contain a 16-byte HMAC-MD5 hash of the challenge, a randomly generated challenge from the client, and an HMAC-MD5 hash of the user's credentials.
  * A second response is sent, using a variable-length client challenge including the current time, an 8-byte random value, and the domain name.

The algorithm is as follows:

**V2 Challenge & Response Algorithm**

&#x20; NTLM Authentication

```shell-session
SC = 8-byte server challenge, random
CC = 8-byte client challenge, random
CC* = (X, time, CC2, domain name)
v2-Hash = HMAC-MD5(NT-Hash, user name, domain name)
LMv2 = HMAC-MD5(v2-Hash, SC, CC)
NTv2 = HMAC-MD5(v2-Hash, SC, CC*)
response = LMv2 | CC | NTv2 | CC*
```

An example of an NTLMv2 hash is:

**NTLMv2 Hash Example**

&#x20; NTLM Authentication

```shell-session
admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030
```

We can see that developers improved upon v1 by making NTLMv2 harder to crack and giving it a more robust algorithm made up of multiple stages.



### Domain Cached Credentials (MSCache2)

* &#x20;Microsoft developed the [MS Cache v1 and v2](https://webstersprodigy.net/2014/02/03/mscash-hash-primer-for-pentesters/) algorithm (also known as `Domain Cached Credentials` (DCC) to solve the potential issue of a domain-joined host being unable to communicate with a domain controller (i.e., due to a network outage or other technical issue) and, hence, NTLM/Kerberos authentication not working to access the host in question.

How it Works:

* Hosts save the last `ten` hashes for any domain users that successfully log into the machine in the `HKEY_LOCAL_MACHINE\SECURITY\Cache` registry key.
* These hashes cannot be used in pass-the-hash attacks.&#x20;
* Furthermore, the hash is very slow to crack with a tool such as Hashcat, even when using an extremely powerful GPU cracking rig, so attempts to crack these hashes typically need to be extremely targeted or rely on a very weak password in use.
* These hashes can be obtained by an attacker or pentester after gaining local admin access to a host and have the following format: `$DCC2$10240#bjones#e4e938d12fe5974dc42a90120bd9c90f`.



User and Machine Accounts

Local Accounts

There are several default local user accounts that are created on a Windows system:

* `Administrator`: this account has the SID `S-1-5-domain-500` and is the first account created with a new Windows installation. It has full control over almost every resource on the system. It cannot be deleted or locked, but it can be disabled or renamed. Windows 10 and Server 2016 hosts disable the built-in administrator account by default and create another local account in the local administrator's group during setup.
* `Guest`: this account is disabled by default. The purpose of this account is to allow users without an account on the computer to log in temporarily with limited access rights. By default, it has a blank password and is generally recommended to be left disabled because of the security risk of allowing anonymous access to a host.
* `SYSTEM`: The SYSTEM (or `NT AUTHORITY\SYSTEM`) account on a Windows host is the default account installed and used by the operating system to perform many of its internal functions. Unlike the Root account on Linux, `SYSTEM` is a service account and does not run entirely in the same context as a regular user. Many of the processes and services running on a host are run under the SYSTEM context. One thing to note with this account is that a profile for it does not exist, but it will have permissions over almost everything on the host. It does not appear in User Manager and cannot be added to any groups. A `SYSTEM` account is the highest permission level one can achieve on a Windows host and, by default, is granted Full Control permissions to all files on a Windows system.
* `Network Service`: This is a predefined local account used by the Service Control Manager (SCM) for running Windows services. When a service runs in the context of this particular account, it will present credentials to remote services.
* `Local Service`: This is another predefined local account used by the Service Control Manager (SCM) for running Windows services. It is configured with minimal privileges on the computer and presents anonymous credentials to the network.



### Domain Users

* Domain user accounts can log in to any host in the domain, unlike local users.
* One account to keep in mind is the `KRBTGT` account. This account acts as a service account for the Key Distribution service providing authentication and access for domain resources. It can be leveraged for privilege escalation and persistence in a domain through attacks such as the [Golden Ticket](https://attack.mitre.org/techniques/T1558/001/) attack.



### User Naming Attributes

Security in Active Directory can be improved using a set of user naming attributes to help identify user objects like logon name or ID. The following are a few important Naming Attributes in AD:

| `UserPrincipalName` (UPN) | This is the primary logon name for the user. By convention, the UPN uses the email address of the user.                                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ObjectGUID`              | This is a unique identifier of the user. In AD, the ObjectGUID attribute name never changes and remains unique even if the user is removed.                                                                                                                                      |
| `SAMAccountName`          | This is a logon name that supports the previous version of Windows clients and servers.                                                                                                                                                                                          |
| `objectSID`               | The user's Security Identifier (SID). This attribute identifies a user and its group memberships during security interactions with the server.                                                                                                                                   |
| `sIDHistory`              | This contains previous SIDs for the user object if moved from another domain and is typically seen in migration scenarios from domain to domain. After a migration occurs, the last SID will be added to the `sIDHistory` property, and the new SID will become its `objectSID`. |

**Common User Attributes**

```powershell-session
PS C:\htb Get-ADUser -Identity htb-student

DistinguishedName : CN=htb student,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
Enabled           : True
GivenName         : htb
Name              : htb student
ObjectClass       : user
ObjectGUID        : aa799587-c641-4c23-a2f7-75850b4dd7e3
SamAccountName    : htb-student
SID               : S-1-5-21-3842939050-3880317879-2865463114-1111
Surname           : student
UserPrincipalName : htb-student@INLANEFREIGHT.LOCAL
```

For a deeper look at user object attributes, check out this [page](https://docs.microsoft.com/en-us/windows/win32/ad/user-object-attributes).&#x20;



### Domain-joined vs. Non-Domain-joined Machines

When it comes to computer resources, there are several ways they are typically managed. Below we will discuss the differences between a host joined to a domain versus a host that is only in a workgroup.



**`Domain joined`**

Hosts joined to a domain have greater ease of information sharing within the enterprise and a central management point (the DC) to gather resources, policies, and updates from. A host joined to a domain will acquire any configurations or changes necessary through the domain's Group Policy. The benefit here is that a user in the domain can log in and access resources from any host joined to the domain, not just the one they work on. This is the typical setup you will see in enterprise environments.



**`Non-domain joined`**

Non-domain joined computers or computers in a `workgroup` are not managed by domain policy. With that in mind, sharing resources outside your local network is much more complicated than it would be on a domain. This is fine for computers meant for home use or small business clusters on the same LAN. The advantage of this setup is that the individual users are in charge of any changes they wish to make to their host. Any user accounts on a workgroup computer only exist on that host, and profiles are not migrated to other hosts within the workgroup.

It is important to note that a machine account (`NT AUTHORITY\SYSTEM` level access) in an AD environment will have most of the same rights as a standard domain user account. This is important because we do not always need to obtain a set of valid credentials for an individual user's account to begin enumerating and attacking a domain (as we will see in later modules). We may obtain `SYSTEM` level access to a domain-joined Windows host through a successful remote code execution exploit or by escalating privileges on a host. This access is often overlooked as only useful for pillaging sensitive data (i.e., passwords, SSH keys, sensitive files, etc.) on a particular host. In reality, access in the context of the `SYSTEM` account will allow us read access to much of the data within the domain and is a great launching point for gathering as much information about the domain as possible before proceeding with applicable AD-related attacks.



Active Directory Groups

One question that comes up often is the difference between Groups and Organizational Units (OUs). As discussed earlier in the module, OUs are useful for grouping users, groups, and computers to ease management and deploying Group Policy settings to specific objects in the domain. Groups are primarily used to assign permissions to access resources. OUs can also be used to delegate administrative tasks to a user, such as resetting passwords or unlocking user accounts without giving them additional admin rights that they may inherit through group membership.



### Types of Groups

* In simpler terms, groups are used to place users, computers, and contact objects into management units that provide ease of administration over permissions and facilitate the assignment of resources such as printers and file share access.

Groups in Active Directory have two fundamental characteristics: `type` and `scope`. The `group type` defines the group's purpose, while the `group scope` shows how the group can be used within the domain or forest. When creating a new group, we must select a group type. There are two main types: `security` and `distribution` groups.



**Group Type And Scope**

![](<../../.gitbook/assets/image (82).png>)\
The `Security groups` type is primarily for ease of assigning permissions and rights to a collection of users instead of one at a time. They simplify management and reduce overhead when assigning permissions and rights for a given resource. All users added to a security group will inherit any permissions assigned to the group, making it easier to move users in and out of groups while leaving the group's permissions unchanged.

The `Distribution groups` type is used by email applications such as Microsoft Exchange to distribute messages to group members. They function much like mailing lists and allow for auto-adding emails in the "To" field when creating an email in Microsoft Outlook. This type of group cannot be used to assign permissions to resources in a domain environment.



### Group Scopes

There are three different `group scopes` that can be assigned when creating a new group.

1. Domain Local Group
2. Global Group
3. Universal Group

**Domain Local Group**

Domain local groups can only be used to manage permissions to domain resources in the domain where it was created. Local groups cannot be used in other domains but `CAN` contain users from `OTHER` domains. Local groups can be nested into (contained within) other local groups but `NOT` within global groups.

**Global Group**

Global groups can be used to grant access to resources in `another domain`. A global group can only contain accounts from the domain where it was created. Global groups can be added to both other global groups and local groups.

**Universal Group**

The universal group scope can be used to manage resources distributed across multiple domains and can be given permissions to any object within the same `forest`.

They are available to all domains within an organization and can contain users from any domain. Unlike domain local and global groups, universal groups are stored in the Global Catalog (GC), and adding or removing objects from a universal group triggers forest-wide replication.

It is recommended that administrators maintain other groups (such as global groups) as members of universal groups because global group membership within universal groups is less likely to change than individual user membership in global groups. Replication is only triggered at the individual domain level when a user is removed from a global group. If individual users and computers (instead of global groups) are maintained within universal groups, it will trigger forest-wide replication each time a change is made. This can create a lot of network overhead and potential for issues. Below is an example of the groups in AD and their scope settings. Please pay attention to some of the critical groups and their scope. ( Enterprise and Schema admins compared to Domain admins, for example.)

**AD Group Scope Examples**

```powershell-session
PS C:\htb> Get-ADGroup  -Filter * |select samaccountname,groupscope

samaccountname                           groupscope
--------------                           ----------
Administrators                          DomainLocal
Users                                   DomainLocal
Guests                                  DomainLocal
Print Operators                         DomainLocal
Backup Operators                        DomainLocal
Replicator                              DomainLocal
Remote Desktop Users                    DomainLocal
Network Configuration Operators         DomainLocal
Distributed COM Users                   DomainLocal
IIS_IUSRS                               DomainLocal
Cryptographic Operators                 DomainLocal
Event Log Readers                       DomainLocal
Certificate Service DCOM Access         DomainLocal
RDS Remote Access Servers               DomainLocal
RDS Endpoint Servers                    DomainLocal
RDS Management Servers                  DomainLocal
Hyper-V Administrators                  DomainLocal
Access Control Assistance Operators     DomainLocal
Remote Management Users                 DomainLocal
Storage Replica Administrators          DomainLocal
Domain Computers                             Global
Domain Controllers                           Global
Schema Admins                             Universal
Enterprise Admins                         Universal
Cert Publishers                         DomainLocal
Domain Admins                                Global
Domain Users                                 Global
Domain Guests                                Global

<SNIP>
```

Group scopes can be changed, but there are a few caveats:

* A Global Group can only be converted to a Universal Group if it is NOT part of another Global Group.
* A Domain Local Group can only be converted to a Universal Group if the Domain Local Group does NOT contain any other Domain Local Groups as members.
* A Universal Group can be converted to a Domain Local Group without any restrictions.
* A Universal Group can only be converted to a Global Group if it does NOT contain any other Universal Groups as members.



### Nested Group Membership

Nested group membership is an important concept in AD. As mentioned previously, a Domain Local Group can be a member of another Domain Local Group in the same domain. Through this membership, a user may inherit privileges not assigned directly to their account or even the group they are directly a member of, but rather the group that their group is a member of.

Below is an example of privileges inherited through nested group membership. Though `DCorner` is not a direct member of `Helpdesk Level 1`, their membership in `Help Desk` grants them the same privileges that any member of `Helpdesk Level 1` has. In this case, the privilege would allow them to add a member to the `Tier 1 Admins` group (`GenericWrite`). If this group confers any elevated privileges in the domain, it would likely be a key target for a penetration tester. Here, we could add our user to the group and obtain privileges that members of the `Tier 1 Admins` group are granted, such as local administrator access to one or more hosts that could be used to further access.

**Examining Nested Groups via BloodHound**

<figure><img src="../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

### Important Group Attributes

Like users, groups have many [attributes](http://www.selfadsi.org/group-attributes.htm). Some of the most [important group attributes](https://docs.microsoft.com/en-us/windows/win32/ad/group-objects) include:

* `cn`: The `cn` or Common-Name is the name of the group in Active Directory Domain Services.
* `member`: Which user, group, and contact objects are members of the group.
* `groupType`: An integer that specifies the group type and scope.
* `memberOf`: A listing of any groups that contain the group as a member (nested group membership).
* `objectSid`: This is the security identifier or SID of the group, which is the unique value used to identify the group as a security principal.



Active Directory Rights and Privileges

&#x20;`Rights` are typically assigned to users or groups and deal with permissions to `access` an object such as a file, while `privileges` grant a user permission to `perform an action` such as run a program, shut down a system, reset passwords, etc.

Privileges can be assigned individually to users or conferred upon them via built-in or custom group membership. Windows computers have a concept called `User Rights Assignment`, which, while referred to as rights, are actually types of privileges granted to a user. We will discuss these later in this section. We must have a firm grasp of the differences between rights and privileges in a broader sense and precisely how they apply to an AD environment.



### Built-in AD Groups

Some of the most common built-in groups are listed below.

| Group Name                           | Description                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Account Operators`                  | Members can create and modify most types of accounts, including those of users, local groups, and global groups, and members can log in locally to domain controllers. They cannot manage the Administrator account, administrative user accounts, or members of the Administrators, Server Operators, Account Operators, Backup Operators, or Print Operators groups.            |
| `Administrators`                     | Members have full and unrestricted access to a computer or an entire domain if they are in this group on a Domain Controller.                                                                                                                                                                                                                                                     |
| `Backup Operators`                   | Members can back up and restore all files on a computer, regardless of the permissions set on the files. Backup Operators can also log on to and shut down the computer. Members can log onto DCs locally and should be considered Domain Admins. They can make shadow copies of the SAM/NTDS database, which, if taken, can be used to extract credentials and other juicy info. |
| `DnsAdmins`                          | Members have access to network DNS information. The group will only be created if the DNS server role is or was at one time installed on a domain controller in the domain.                                                                                                                                                                                                       |
| `Domain Admins`                      | Members have full access to administer the domain and are members of the local administrator's group on all domain-joined machines.                                                                                                                                                                                                                                               |
| `Domain Computers`                   | Any computers created in the domain (aside from domain controllers) are added to this group.                                                                                                                                                                                                                                                                                      |
| `Domain Controllers`                 | Contains all DCs within a domain. New DCs are added to this group automatically.                                                                                                                                                                                                                                                                                                  |
| `Domain Guests`                      | This group includes the domain's built-in Guest account. Members of this group have a domain profile created when signing onto a domain-joined computer as a local guest.                                                                                                                                                                                                         |
| `Domain Users`                       | This group contains all user accounts in a domain. A new user account created in the domain is automatically added to this group.                                                                                                                                                                                                                                                 |
| `Enterprise Admins`                  | Membership in this group provides complete configuration access within the domain. The group only exists in the root domain of an AD forest. Members in this group are granted the ability to make forest-wide changes such as adding a child domain or creating a trust. The Administrator account for the forest root domain is the only member of this group by default.       |
| `Event Log Readers`                  | Members can read event logs on local computers. The group is only created when a host is promoted to a domain controller.                                                                                                                                                                                                                                                         |
| `Group Policy Creator Owners`        | Members create, edit, or delete Group Policy Objects in the domain.                                                                                                                                                                                                                                                                                                               |
| `Hyper-V Administrators`             | Members have complete and unrestricted access to all the features in Hyper-V. If there are virtual DCs in the domain, any virtualization admins, such as members of Hyper-V Administrators, should be considered Domain Admins.                                                                                                                                                   |
| `IIS_IUSRS`                          | This is a built-in group used by Internet Information Services (IIS), beginning with IIS 7.0.                                                                                                                                                                                                                                                                                     |
| `Pre–Windows 2000 Compatible Access` | This group exists for backward compatibility for computers running Windows NT 4.0 and earlier. Membership in this group is often a leftover legacy configuration. It can lead to flaws where anyone on the network can read information from AD without requiring a valid AD username and password.                                                                               |
| `Print Operators`                    | Members can manage, create, share, and delete printers that are connected to domain controllers in the domain along with any printer objects in AD. Members are allowed to log on to DCs locally and may be used to load a malicious printer driver and escalate privileges within the domain.                                                                                    |
| `Protected Users`                    | Members of this [group](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#protected-users) are provided additional protections against credential theft and tactics such as Kerberos abuse.                                                                                                                   |
| `Read-only Domain Controllers`       | Contains all Read-only domain controllers in the domain.                                                                                                                                                                                                                                                                                                                          |
| `Remote Desktop Users`               | This group is used to grant users and groups permission to connect to a host via Remote Desktop (RDP). This group cannot be renamed, deleted, or moved.                                                                                                                                                                                                                           |
| `Remote Management Users`            | This group can be used to grant users remote access to computers via [Windows Remote Management (WinRM)](https://docs.microsoft.com/en-us/windows/win32/winrm/portal)                                                                                                                                                                                                             |
| `Schema Admins`                      | Members can modify the Active Directory schema, which is the way all objects with AD are defined. This group only exists in the root domain of an AD forest. The Administrator account for the forest root domain is the only member of this group by default.                                                                                                                    |
| `Server Operators`                   | This group only exists on domain controllers. Members can modify services, access SMB shares, and backup files on domain controllers. By default, this group has no members.                                                                                                                                                                                                      |

```powershell-session
PS C:\htb>  Get-ADGroup -Identity "Server Operators" -Properties *

adminCount                      : 1
CanonicalName                   : INLANEFREIGHT.LOCAL/Builtin/Server Operators
CN                              : Server Operators
Created                         : 10/27/2021 8:14:34 AM
createTimeStamp                 : 10/27/2021 8:14:34 AM
Deleted                         : 
Description                     : Members can administer domain servers
DisplayName                     : 
DistinguishedName               : CN=Server Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL
dSCorePropagationData           : {10/28/2021 1:47:52 PM, 10/28/2021 1:44:12 PM, 10/28/2021 1:44:11 PM, 10/27/2021 
                                  8:50:25 AM...}
GroupCategory                   : Security
GroupScope                      : DomainLocal
groupType                       : -2147483643
HomePage                        : 
instanceType                    : 4
isCriticalSystemObject          : True
isDeleted                       : 
LastKnownParent                 : 
ManagedBy                       : 
MemberOf                        : {}
Members                         : {}
Modified                        : 10/28/2021 1:47:52 PM
modifyTimeStamp                 : 10/28/2021 1:47:52 PM
Name                            : Server Operators
nTSecurityDescriptor            : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                  : CN=Group,CN=Schema,CN=Configuration,DC=INLANEFREIGHT,DC=LOCAL
ObjectClass                     : group
ObjectGUID                      : 0887487b-7b07-4d85-82aa-40d25526ec17
objectSid                       : S-1-5-32-549
ProtectedFromAccidentalDeletion : False
SamAccountName                  : Server Operators
sAMAccountType                  : 536870912
sDRightsEffective               : 0
SID                             : S-1-5-32-549
SIDHistory                      : {}
systemFlags                     : -1946157056
uSNChanged                      : 228556
uSNCreated                      : 12360
whenChanged                     : 10/28/2021 1:47:52 PM
whenCreated                     : 10/27/2021 8:14:34 AM
```



User Rights Assignment

This Microsoft article on [User Rights Assignment](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment) provides a detailed explanation of each of the user rights that can be set in Windows.&#x20;

A few examples include:

| **Privilege**                   | **Description**                                                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SeRemoteInteractiveLogonRight` | This privilege could give our target user the right to log onto a host via Remote Desktop (RDP), which could potentially be used to obtain sensitive data or escalate privileges.                                                                                                                 |
| `SeBackupPrivilege`             | This grants a user the ability to create system backups and could be used to obtain copies of sensitive system files that can be used to retrieve passwords such as the SAM and SYSTEM Registry hives and the NTDS.dit Active Directory database file.                                            |
| `SeDebugPrivilege`              | This allows a user to debug and adjust the memory of a process. With this privilege, attackers could utilize a tool such as [Mimikatz](https://github.com/ParrotSec/mimikatz) to read the memory space of the Local System Authority (LSASS) process and obtain any credentials stored in memory. |
| `SeImpersonatePrivilege`        | This privilege allows us to impersonate a token of a privileged account such as `NT AUTHORITY\SYSTEM`. This could be leveraged with a tool such as JuicyPotato, RogueWinRM, PrintSpoofer, etc., to escalate privileges on a target system.                                                        |
| `SeLoadDriverPrivilege`         | A user with this privilege can load and unload device drivers that could potentially be used to escalate privileges or compromise a system.                                                                                                                                                       |
| `SeTakeOwnershipPrivilege`      | This allows a process to take ownership of an object. At its most basic level, we could use this privilege to gain access to a file share or a file on a share that was otherwise not accessible to us.                                                                                           |



### Viewing a User's Privileges

After logging into a host, typing the command `whoami /priv` will give us a listing of all user rights assigned to the current user.

Some rights are only available to administrative users and can only be listed/leveraged when running an elevated CMD or PowerShell session. These concepts of elevated rights and [User Account Control (UAC)](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) are security features introduced with Windows Vista that default to restricting applications from running with full permissions unless absolutely necessary.

First, let's look at the rights available to a standard Active Directory user.



**Standard Domain User's Rights**

```powershell-session
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```



**Domain Admin Rights Non-Elevated**

We can see the following in a `non-elevated` console which does not appear to be anything more than available to the standard domain user. This is because, by default, Windows systems do not enable all rights to us unless we run the CMD or PowerShell console in an elevated context. This is to prevent every application from running with the highest possible privileges. This is controlled by something called [User Account Control (UAC)](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) which is covered in-depth in the [Windows Privilege Escalation](https://academy.hackthebox.com/course/preview/windows-privilege-escalation) module.

```powershell-session
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled
```



**Domain Admin Rights Elevated**

If we enter the same command from an elevated PowerShell console, we can see the complete listing of rights available to us:

```powershell-session
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State
========================================= ================================================================== ========
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeMachineAccountPrivilege                 Add workstations to domain                                         Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled
SeBackupPrivilege                         Back up files and directories                                      Disabled
SeRestorePrivilege                        Restore files and directories                                      Disabled
SeShutdownPrivilege                       Shut down the system                                               Disabled
SeDebugPrivilege                          Debug programs                                                     Enabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Disabled
SeUndockPrivilege                         Remove computer from docking station                               Disabled
SeEnableDelegationPrivilege               Enable computer and user accounts to be trusted for delegation     Disabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Disabled
SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled
SeCreateGlobalPrivilege                   Create global objects                                              Enabled
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
SeTimeZonePrivilege                       Change the time zone                                               Disabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Disabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Disabled
```



**Backup Operator Rights**

&#x20; Active Directory Rights and Privileges

```powershell-session
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```



Security in Active Directory

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### General Active Directory Hardening Measures

The [Microsoft Local Administrator Password Solution (LAPS)](https://www.microsoft.com/en-us/download/details.aspx?id=46899) is used to randomize and rotate local administrator passwords on Windows hosts and prevent lateral movement.



**LAPS**

Accounts can be set up to have their password rotated on a fixed interval (i.e., 12 hours, 24 hours, etc.). This free tool can be beneficial in reducing the impact of an individual compromised host in an AD environment. Organizations should not rely on tools like this alone. Still, when combined with other hardening measures and security best practices, it can be a very effective tool for local administrator account password management.



**Audit Policy Settings (Logging and Monitoring)**

Every organization needs to have logging and monitoring setup to detect and react to unexpected changes or activities that may indicate an attack. Effective logging and monitoring can be used to detect an attacker or unauthorized employee adding a user or computer, modifying an object in AD, changing an account password, accessing a system in an unauthorized or non-standard manner, performing an attack such as password spraying, or more advanced attacks such as modern Kerberos attacks.



**Group Policy Security Settings**

The following is a non-exhaustive list of the types of security policies that can be applied:

* [Account Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-policies) - Manage how user accounts interact with the domain. These include the password policy, account lockout policy, and Kerberos-related settings such as the lifetime of Kerberos tickets
* [Local Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/security-options) - These apply to a specific computer and include the security event audit policy, user rights assignments (user privileges on a host), and specific security settings such as the ability to install drivers, whether the administrator and guest accounts are enabled, renaming the guest and administrator accounts, preventing users from installing printers or using removable media, and a variety of network access and network security controls.
* [Software Restriction Policies](https://docs.microsoft.com/en-us/windows-server/identity/software-restriction-policies/software-restriction-policies) - Settings to control what software can be run on a host.
* [Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control) - Settings to control which applications can be run by certain users/groups. This may include blocking certain users from running all executables, Windows Installer files, scripts, etc. Administrators use [AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) to restrict access to certain types of applications and files. It is not uncommon to see organizations block access to CMD and PowerShell (among other executables) for users that do not require them for their day-to-day job. These policies are imperfect and can often be bypassed but necessary for a defense-in-depth strategy.
* [Advanced Audit Policy Configuration](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/secpol-advanced-security-audit-policy-settings) - A variety of settings that can be adjusted to audit activities such as file access or modification, account logon/logoff, policy changes, privilege usage, and more.



**Update Management (SCCM/WSUS)**

Proper patch management is critical for any organization, especially those running Windows/Active Directory systems. The [Windows Server Update Service (WSUS)](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus) can be installed as a role on a Windows Server and can be used to minimize the manual task of patching Windows systems. `System Center Configuration Manager` (SCCM) is a paid solution that relies on the WSUS Windows Server role being installed and offers more features than WSUS on its own. A patch management solution can help ensure timely deployment of patches and maximize coverage, making sure that no hosts miss critical security patches. If an organization relies on a manual method for applying patches, it could take a very long time depending on the size of the environment and also could result in systems being missed and left vulnerable.



**Group Managed Service Accounts (gMSA)**

A gMSA is an account managed by the domain that offers a higher level of security than other types of service accounts for use with non-interactive applications, services, processes, and tasks that are run automatically but require credentials to run. They provide automatic password management with a 120 character password generated by the domain controller. The password is changed at a regular interval and does not need to be known by any user. It allows for credentials to be used across multiple hosts.



**Security Groups**

Security groups offer an easy way to assign access to network resources. They can be used to assign specific rights to the group (instead of directly to the user) to determine what members of the group can do within the AD environment. Active Directory automatically creates some [default security groups](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#active-directory-default-security-groups-by-operating-system-version) during installation. Some examples are Account Operators, Administrators, Backup Operators, Domain Admins, and Domain Users. These groups can also be used to assign permission to access resources (i.e., a file share, folder, printer, or a document). Security groups help ensure you can assign granular permissions to users en masse instead of individually managing each user.



**Account Separation**

Administrators must have two separate accounts. One for their day-to-day work and a second for any administrative tasks they must perform.

It is also essential for the individual to use different passwords for each account to mitigate the risk of password reuse attacks if their non-admin account is compromised.



**Password Complexity Policies + Passphrases + 2FA**

An organization should also consider implementing a password filter to disallow passwords containing the months or seasons of the year, the company name, and common words such as `password` and `welcome`. The minimum password length for standard users should be at least 12 characters and ideally longer for administrators/service accounts. Another important security measure is the implementation of multi-factor authentication (MFA) for Remote Desktop Access to any host. This can help to limit lateral movement attempts that may rely on GUI access to a host.



**Limiting Domain Admin Account Usage**

All-powerful Domain Admin accounts should only be used to log in to Domain Controllers, not personal workstations, jump hosts, web servers, etc. This can significantly reduce the impact of an attack and cut down potential attack paths should a host be compromised. This would ensure that Domain Admin account passwords are not left in memory on hosts throughout the environment.



**Periodically Auditing and Removing Stale Users and Objects**

It is important for an organization to periodically audit Active Directory and remove or disable any unused accounts.



**Auditing Permissions and Access**

Organizations should also periodically perform access control audits to ensure that users only have the level of access required for their day-to-day work.\


**Audit Policies & Logging**

Visibility into the domain is a must. An organization can achieve this through robust logging and then using rules to detect anomalous activity (such as many failed login attempts that could be indicative of a password spraying attack) or indicators that a Kerberoasting attack is being attempted.

It is worth familiarizing ourselves with Microsoft's [Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations) to help detect compromise.



**Using Restricted Groups**

[Restricted Groups](https://social.technet.microsoft.com/wiki/contents/articles/20402.active-directory-group-policy-restricted-groups.aspx) allow for administrators to configure group membership via Group Policy. They can be used for a number of reasons, such as controlling membership in the local administrator's group on all hosts in the domain by restricting it to just the local Administrator account and Domain Admins and controlling membership in the highly privileged Enterprise Admins and Schema Admins groups and other key administrative groups.



**Limiting Server Roles**

It is important not to install additional roles on sensitive hosts, such as installing the `Internet Information Server` (IIS) role on a Domain Controller. This would increase the attack surface of the Domain Controller, and this type of role should be installed on a separate standalone web server.



**Limiting Local Admin and RDP Rights**

Organizations should tightly control which users have local admin rights on which computers. As stated above, this can be achieved using Restricted Groups.



Examining Group Policy

Group Policy Objects (GPOs)

* A [Group Policy Object (GPO)](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects) is a virtual collection of policy settings that can be applied to `user(s)` or `computer(s)`.
* GPOs include policies such as screen lock timeout, disabling USB ports, enforcing a custom domain password policy, installing software, managing applications, customizing remote access settings, and much more.
* Every GPO has a unique name and is assigned a unique identifier (a GUID).
* Every GPO contains one or more Group Policy settings that may apply at the local machine level or within the Active Directory context.
* We can manage Group Policy from the Group Policy Management Console or using the PowerShell [GroupPolicy](https://docs.microsoft.com/en-us/powershell/module/grouppolicy/?view=windowsserver2022-ps) module via command line.

### Example GPOs

Some examples of things we can do with GPOs may include:

* Establishing different password policies for service accounts, admin accounts, and standard user accounts using separate GPOs
* Preventing the use of removable media devices (such as USB devices)
* Enforcing a screensaver with a password
* Restricting access to applications that a standard user may not need, such as cmd.exe and PowerShell
* Enforcing audit and logging policies
* Blocking users from running certain types of programs and scripts
* Deploying software across a domain
* Blocking users from installing unapproved software
* Displaying a logon banner whenever a user logs into a system
* Disallowing LM hash usage in the domain
* Running scripts when computers start/shutdown or when a user logs in/out of their machine



GPO settings are processed using the hierarchical structure of AD and are applied using the `Order of Precedence` rule as seen in the table below:

**Order of Precedence**

| **Level**                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Local Group Policy`                       | The policies are defined directly to the host locally outside the domain. Any setting here will be overwritten if a similar setting is defined at a higher level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `Site Policy`                              | Any policies specific to the Enterprise Site that the host resides in. Remember that enterprise environments can span large campuses and even across countries. So it stands to reason that a site might have its own policies to follow that could differentiate it from the rest of the organization. Access Control policies are a great example of this. Say a specific building or `site` performs secret or restricted research and requires a higher level of authentication for access to resources. You could specify those settings at the site level and ensure they are linked so as not to be overwritten by domain policy. This is also a great way to perform actions like printer and share mapping for users in specific sites. |
| `Domain-wide Policy`                       | Any settings you wish to have applied across the domain as a whole. For example, setting the password policy complexity level, configuring a Desktop background for all users, and setting a Notice of Use and Consent to Monitor banner at the login screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Organizational Unit` (OU)                 | These settings would affect users and computers who belong to specific OUs. You would want to place any unique settings here that are role-specific. For example, the mapping of a particular share drive that can only be accessed by HR, access to specific resources like printers, or the ability for IT admins to utilize PowerShell and command-prompt.                                                                                                                                                                                                                                                                                                                                                                                    |
| `Any OU Policies nested within other OU's` | Settings at this level would reflect special permissions for objects within nested OUs. For example, providing Security Analysts a specific set of Applocker policy settings that differ from the standard IT Applocker settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### GPO Order of Precedence

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

This image also shows an example of several GPOs being linked to the `Corp` OU. When more than one GPO is linked to an OU, they are processed based on the `Link Order`. The GPO with the lowest Link Order is processed last, or the GPO with link order 1 has the highest precedence, then 2, and 3, and so on. So in our example above, the `Disallow LM Hash` GPO will have precedence over the `Block Removable Media` and `Disable Guest Account` GPOs, meaning it will be processed first.

It is possible to specify the `Enforced` option to enforce settings in a specific GPO. If this option is set, policy settings in GPOs linked to lower OUs `CANNOT` override the settings. If a GPO is set at the domain level with the `Enforced` option selected, the settings contained in that GPO will be applied to all OUs in the domain and cannot be overridden by lower-level OU policies. In the past, this setting was called `No Override` and was set on the container in question under Active Directory Users and Computers. Below we can see an example of an `Enforced` GPO, where the `Logon Banner` GPO is taking precedence over GPOs linked to lower OUs and therefore will not be overridden.



Regardless of which GPO is set to enforced, if the `Default Domain Policy` GPO is enforced, it will take precedence over all GPOs at all levels.



**Default Domain Policy Override**

It is also possible to set the `Block inheritance` option on an OU. If this is specified for a particular OU, then policies higher up (such as at the domain level) will NOT be applied to this OU. If both options are set, the `No Override` option has precedence over the `Block inheritance` option. Here is a quick example. The `Computers` OU is inheriting GPOs set on the `Corp` OU in the below image.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

If the `Block Inheritance` option is chosen, we can see that the 3 GPOs applied higher up to the `Corp` OU are no longer enforced on the `Computers` OU.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### Group Policy Refresh Frequency

When a new GPO is created, the settings are not automatically applied right away. Windows performs periodic Group Policy updates, which by default is done every 90 minutes with a randomized offset of +/- 30 minutes for users and computers.

The period is only 5 minutes for domain controllers to update by default.&#x20;

When a new GPO is created and linked, it could take up to 2 hours (120 minutes) until the settings take effect.&#x20;

This random offset of +/- 30 minutes is set to avoid overwhelming domain controllers by having all clients request Group Policy from the domain controller simultaneously.

We can issue the command `gpupdate /force` to kick off the update process.



### Security Considerations of GPOs

Below is an example of a GPO attack path identified using the [BloodHound](https://github.com/BloodHoundAD/BloodHound) tool. This example shows that the `Domain Users` group can modify the `Disconnect Idle RDP` GPO due to nested group membership. In this case, we would next look to see which OUs this GPO applies to and if we can leverage these rights to gain control over a high-value user (administrator or Domain Admin) or computer (server, DC, or critical host) and move laterally to escalate privileges within the domain.

























































