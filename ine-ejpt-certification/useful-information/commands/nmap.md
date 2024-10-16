# Nmap

### <mark style="color:purple;">**NOTE:**</mark>** Windows machines normally block ping probes use "-**<mark style="color:yellow;">**Pn**</mark>**" to turn them off**

### <mark style="color:purple;">**NOTE:**</mark>** When dealing with Windows machines, if a port is "**<mark style="color:red;">**FILTERED**</mark>**" it means that the firewall is active, if it is closed it means that either the firewall is off or doesn't have any rules set for that port**



Running a default nmap scan, you perform a SYN scan on the 1000 most known ports

* <mark style="color:yellow;">nmap 10.0.0.1</mark>
* <mark style="color:yellow;">-Pn</mark>: Skips host discovery (no ping), 1000 most common used ports
  * <mark style="color:purple;">NOTE:</mark> If you are a privileged user it runs the SYN port scan, otherwise it uses the TCP Connect scan
* <mark style="color:yellow;">-p</mark>: Define ports
  * <mark style="color:yellow;">-p-</mark>: Scan all 65535 TCP ports
  * <mark style="color:yellow;">--top-ports</mark>: Define a number of the top used ports to scan
  * <mark style="color:yellow;">--reason</mark>: Tells you the reason a port is in a particular state

### Types of Scans

* <mark style="color:yellow;">sudo nmap -sn 192.168.2.0/24</mark>
  * <mark style="color:blue;">-sn</mark>: This flag turns off the port scanning probes, making it so that the scan only sends ping requests to identify devices in a given network
    * <mark style="color:purple;">NOTE:</mark> Always use this option when discovering hosts.
* <mark style="color:yellow;">-sS</mark>: SYN Port Scan (Stealth Scan)
* <mark style="color:yellow;">-sT</mark>: TCP Connect Scan
* <mark style="color:yellow;">-PS</mark>: SYN Ping overrides the <mark style="color:yellow;">-sn</mark> ping
  * If used with <mark style="color:yellow;">-sn</mark>, it will only do host discovery using the SYN Ping.
  * If used alone will do the SYN Ping and port scanning for services
* <mark style="color:yellow;">-PA</mark>: ACK Ping&#x20;
  * Usually not very reliable, because normally hosts are configured to block ACK pings, or block RST packets out
* <mark style="color:yellow;">-PE</mark>: ICMP Echo request scan
* <mark style="color:yellow;">-F</mark>: Scans the 100 most commonly used ports
* <mark style="color:yellow;">-sU</mark>: ExecuteS a UDP scan
* <mark style="color:yellow;">-sV</mark>: Service version scan
  * <mark style="color:yellow;">--version-intensity X</mark>: Intensity for Service Detection
* <mark style="color:yellow;">-O</mark>: Operating System scan
* <mark style="color:yellow;">-sC</mark>: Runs a list of default nmap scripts
* <mark style="color:yellow;">-A</mark>: Agressive scan combines <mark style="color:yellow;">-sV, -O and -sC</mark>

### Speeds for the scan

* <mark style="color:yellow;">-T0-5</mark>: Sets different speeds for the scan
  * <mark style="color:yellow;">-T0</mark>: Paranoid
  * <mark style="color:yellow;">-T1</mark>: Sneaky
  * <mark style="color:yellow;">-T2</mark>: Polite
  * <mark style="color:yellow;">-T3</mark>: Normal
  * <mark style="color:yellow;">-T4</mark>: Aggressive
  * <mark style="color:yellow;">-T5</mark>: Insane

#### Optimizing Nmap Scans Commands:

* <mark style="color:yellow;">--host-timeout</mark>: Time to give up on target if state is now known
* <mark style="color:yellow;">--scan-delay</mark>: Set time delay between probes

### Outputs for the scan

* <mark style="color:yellow;">-oA</mark>: Outputs the content of the scan in all 3 formats: XML,normal and grepable
  * <mark style="color:yellow;">-oN</mark>: Output normal mode
  * <mark style="color:yellow;">-oX</mark>: Outputs into XML
  * <mark style="color:yellow;">-oG</mark>: Outputs into grepable format
  * <mark style="color:yellow;">-oS</mark>:  Script Kiddie format

### NSE

#### To learn more about a specific script:

* <mark style="color:yellow;">nmap --script-help=nameofscript</mark>

#### To run a particular script run:

* <mark style="color:yellow;">nmap --script=nameofscript</mark>

### Firewall Detection & IDS Evasion:

* <mark style="color:yellow;">-sA</mark>: Performs an ACK scan, based on the response determines if a firewall is active or not
* <mark style="color:yellow;">-f</mark>: Fragments packets
  * <mark style="color:yellow;">f --mtu</mark>: Sets the maximum transmission unit for each fragmented packet (minimum is 8)
* <mark style="color:yellow;">--data-length</mark>: Append random data to set packets
* <mark style="color:yellow;">-D</mark>: Set a decoy IP, spoofs your IP to the defined one
* <mark style="color:yellow;">-g</mark>: Set a source port for our scan
