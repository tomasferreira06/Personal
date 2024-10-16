# Port Scanning with Nmap

## Practical Demo

#### Commands/Flags:

* Running a default nmap scan, you perform a SYN scan on the 1000 most known ports
  * "<mark style="color:yellow;">nmap 10.0.0.1</mark>"
* "<mark style="color:yellow;">-Pn</mark>": Skips host discovery (no ping), 1000 most common used ports
  * <mark style="color:purple;">NOTE:</mark> If you are a privileged user it runs the SYN port scan, otherwise it uses the TCP Connect scan
* "<mark style="color:yellow;">-p</mark>": Define ports
  * "<mark style="color:yellow;">-p-</mark>": Scan all 65535 TCP ports
  * "<mark style="color:yellow;">--top-ports</mark>": Define a number of the top used ports to scan
* "<mark style="color:yellow;">-sS</mark>": SYN Port Scan (Stealth Scan)
* "<mark style="color:yellow;">-sT</mark>": TCP Connect Scan
* "<mark style="color:yellow;">-F</mark>": Scans the 100 most commonly used ports
* "<mark style="color:yellow;">-sU</mark>": Executed a UDP scan
* "<mark style="color:yellow;">-v</mark>": Turns on <mark style="color:green;">verbose</mark> mode
* "<mark style="color:yellow;">-sV</mark>": Service version scan
  * "<mark style="color:yellow;">--version-intensity X</mark>": Intensity for Service Detection
* "<mark style="color:yellow;">-O</mark>": Operating System scan
* "<mark style="color:yellow;">-sC</mark>": Runs a list of default nmap scripts
* "<mark style="color:yellow;">-A</mark>": Agressive scan combines "-sV", "-O" and "-sC"&#x20;
* <mark style="color:yellow;">"-T0-5</mark>": Sets different speeds for the scan
  * "<mark style="color:yellow;">-T0</mark>": Paranoid
  * "<mark style="color:yellow;">-T1</mark>": Sneaky
  * "<mark style="color:yellow;">-T2</mark>": Polite
  * "<mark style="color:yellow;">-T3</mark>": Normal
  * "<mark style="color:yellow;">-T4</mark>": Aggressive
  * "<mark style="color:yellow;">-T5</mark>": Insane
  * "<mark style="color:yellow;">-oA</mark>": Outputs the content of the scan in all 3 formats: XML,normal and grepable
    * "<mark style="color:yellow;">-oN</mark>": Output normal mode
    * "<mark style="color:yellow;">-oX</mark>": Outputs into XML
    * "<mark style="color:yellow;">-oG</mark>": Outputs into grepable format
    * "<mark style="color:yellow;">-oS</mark>":  Script Kiddie format
  * "<mark style="color:yellow;">--reason</mark>": Tells you the reason a port is in a particular state

<mark style="color:purple;">NOTE:</mark> Windows machines normally block ping probes use "-<mark style="color:yellow;">Pn</mark>" to turn them off

<mark style="color:purple;">NOTE:</mark> When dealing with Windows machines, if a port is "<mark style="color:red;">FILTERED</mark>" it means that the firewall is active, if it is closed it means that either the firewall is off or doesn't have any rules set for that port
