# Pivoting

* Pivoting is a <mark style="color:red;">post exploitation technique</mark> that involves utilizing a compromised host to attack other systems on the compromised host's private internal network.
* After gaining access to one host, we can use the compromised host to exploit other hosts on the same internal network to which we could not access previously.
* Meterpreter provides us with the ability to add a network route to the internal network's subnet and consequently scan and exploit other systems on the network.

## Pivoting Visualized

<figure><img src="../../.gitbook/assets/image (234).png" alt=""><figcaption></figcaption></figure>

## Practical Demo

Enumerate the target, in this case it is running <mark style="color:red;">HFS(rejetto)</mark>

After gaining access to the first target, we need to add a route to the second target:

* <mark style="color:yellow;">run autoroute -s 'targetsubnet/24'</mark>

<mark style="color:purple;">NOTE:</mark> Take note of the subnet's netmask, because of the CIDR Notation

<mark style="color:purple;">NOTE:</mark> The route to the second target's subnet is only applicable inside msf as it is

### Scanning for open ports in the second target

* <mark style="color:yellow;">auxilary/scanner/portscan/tcp</mark>

Set required options

the <mark style="color:red;">RHOSTS</mark> if the second target's IP

#### IP Forwarding

Here we will forward <mark style="color:red;">port 80</mark> on the second target to our local port, in this case, 1234 (we can define any port). This way we can perform an nmap scan on it.

* <mark style="color:yellow;">portfwd add -l 1234 -p 80 -r 'secondtargertIP'</mark>

Now we can use nmap to scan the second target:

* <mark style="color:yellow;">db\_nmap -sS -sV -p 1234 localhost</mark>

<mark style="color:blue;">WHY DO THIS? BECAUSE THE TCP SCANNER MODULE ONLY GIVES US OPEN PORTS, THIS WAY WE CAN ENUMERATE FURTHER</mark>

### Exploiting the enumerated badblue in the second target

* <mark style="color:yellow;">exploit/windows/http/badblue\_passthru</mark>

In this case a reverse connection is not possible, so we change the payload to:

* <mark style="color:yellow;">windows/meterpreter/bind\_tcp</mark>

set <mark style="color:red;">RHOSTS</mark> to second target's IP

