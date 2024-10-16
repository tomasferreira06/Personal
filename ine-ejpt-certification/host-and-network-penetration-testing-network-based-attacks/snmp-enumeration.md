# SNMP Enumeration

## Simple Network Management Protocol (SNMP)

* SNMP is a widely used protocol for monitoring and managing devices, such as routers, switches, printers, servers and more.
* It allows network administrators to query devices for status information, configure certain settings, and receive alerts or traps when specific events occur.

SNMP is an application layer protocol that typically uses UDP fo transport. It involves three primary components:

* <mark style="color:blue;">SNMP Manager</mark>: The system responsible for querying and interacting with SNMP agents on network devices.
* <mark style="color:blue;">SNMP agent</mark>: Software running on network devices that responds to SNMP queries and sends traps.
* <mark style="color:blue;">Management Information Base (MIB)</mark>: A hierarchical database that defines the structure of data available through SNMP. Each piece of data has a unique <mark style="color:red;">Object Identifier</mark> (<mark style="color:red;">OID</mark>).

#### Versions of SNMP:

* <mark style="color:blue;">SNMPv1:</mark> The earliest version, using community strings (essentially passwords) for authentication.
* <mark style="color:blue;">SNMPv2c:</mark> An improved version with support for bulk transfers but still relying on community string for authentication.
* <mark style="color:blue;">SNMPv3:</mark> Introduced security featured, including encryption, message integrity and user-based authentication.

#### Ports:

* <mark style="color:red;">Port 161 (UDP)</mark>: Used for SNMP queries
* <mark style="color:red;">Port 162 (UDP)</mark>: Used for SNMP traps (notifications)

## SNMP Enumeration

* SNMP enumeration in pentesting involves querying SNMP-enabled devices to gather inforamation useful for identifying potential vulnerabilities, misconigurations or points of attack.

#### Key objectives and outcomes of SNMP enumeration during a pentest:

* <mark style="color:blue;">Identify SNMP-Enabled Devices:</mark> Determine which devices on the network have SNMP enabled and whether they are vulnerable to information leakage or attacks.
* <mark style="color:blue;">Extract System Information:</mark> Collect system-related data like device names, OS, software versions, network interfaces and more.
* <mark style="color:blue;">Identify SNMP Community Strings:</mark> Test for default or weak community strings, which can grant unauthorized access to device information.
* <mark style="color:blue;">Retrieve Network Configurations:</mark> Gather information about routing tables, network interfaces, IP addresses and other network-specific details.
* <mark style="color:blue;">Collect User and Group Information:</mark> In some cases, SNMP can reveal user account information and access permissions.
* <mark style="color:blue;">Identify Services and Applications:</mark> Find out which services and applications are running on the target devices potentially leading to further attack vectors.

### Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/snmp/snmp_enum`**</mark>: Enumerates information from SNMP services, such as community strings, system details, and network configurations.
* <mark style="color:yellow;">**`auxiliary/scanner/snmp/snmp_login`**</mark>: Attempts to brute force SNMP community strings.
* <mark style="color:yellow;">**`auxiliary/scanner/snmp/snmp_version`**</mark>: Identifies the SNMP version in use.
* <mark style="color:yellow;">**`auxiliary/scanner/snmp/snmp_discovery`**</mark>: Performs discovery to gather basic information about SNMP devices on the network.
* <mark style="color:yellow;">**`auxiliary/scanner/snmp/snmp_tftp`**</mark>: Exploits SNMP to retrieve files from a TFTP server if configured.

## Practice Demo

We can check the IPs  of our targets by:

* <mark style="color:yellow;">cat /etc/hosts</mark>

### Finding the SNMP enabled devices

* <mark style="color:yellow;">nmap -sU -p 161 demo.ine.local</mark>

### Find community strings

We will a nmap script located at <mark style="color:red;">/usr/share/nmap/nselib/data/snmp-brute.nse</mark> to find community strings

* <mark style="color:yellow;">nmap -sU -p 161 --script=snmp-brute demo.ine.local</mark>

Now we can use "<mark style="color:red;">snmpwalk</mark>" to extract more info from SNMP

### SNMPwalk

`SNMPwalk` is a command-line tool used to retrieve a large amount of information from a device (like a router, switch, or server) that uses the **Simple Network Management Protocol (SNMP)**. It "walks" through the SNMP tree of the device, gathering details such as system information, network interface statistics, or other device data.

* <mark style="color:yellow;">snmpwalk -v 1 -c public demo.ine.local</mark>
  * <mark style="color:yellow;">"-v":</mark> Defines the version, this should be found by using the "<mark style="color:red;">-sV</mark>" flag in nmap
  * "<mark style="color:yellow;">-c</mark>": Define the community string to use, this were enumerated above with the script "snmp-brute"

This displays the info in a not very readable form, so we run:

* <mark style="color:yellow;">nmap -sU -p 161 --script snmp-\* demo.ine.local > snmp\_info</mark>
  * This will run all snmp nmap scripts and display it in a more readable  way in the specifiedfile "<mark style="color:red;">snmp\_info</mark>"

This scripts enumerate several information like network interfaces, community strings, and even user accounts on the target machine.

With that we can run hydra as usual to brute force the passwords for the enumerated users.























