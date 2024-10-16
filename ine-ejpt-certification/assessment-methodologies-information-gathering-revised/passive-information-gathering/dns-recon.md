# DNS Recon

## What is DNS Recon?

<mark style="color:red;">DNS Recon</mark> is a python script that provides the ability to:

* Check all DNS Records for Zone Transfers
* Enumerate General DNS Records for a given Domain (MX, SOA, NS, A, AAAA, SPF, and TXT)
  * <mark style="color:blue;">MX</mark>: Mail server
  * <mark style="color:blue;">SOA (Start of Authority)</mark>: Helps manage zone updates and synchronization between DNS servers.
  * <mark style="color:blue;">NS</mark>: Name Server
  * <mark style="color:blue;">A</mark>: IPv4 Addresses
  * <mark style="color:blue;">AAAA</mark>: IPv6 Addresses
  * <mark style="color:blue;">SPF (Sender Policy Framework)</mark>: Is an email authentication method designed to prevent email spoofing.
  * <mark style="color:blue;">TXT</mark>: TXT Records
* Perform common SRV Record Enumeration Top Level Domain  (TLD) Expansion

The command to run DNS Recon is the following:

* <mark style="color:yellow;">dnsrescon -d hackersploit.org</mark>
  * <mark style="color:red;">"-d"</mark> is for the domain name

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

Another great website is "<mark style="color:red;">dnsdumspter</mark>"([https://dnsdumpster.com](https://dnsdumpster.com)).
