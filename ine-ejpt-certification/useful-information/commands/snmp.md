# SNMP

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
