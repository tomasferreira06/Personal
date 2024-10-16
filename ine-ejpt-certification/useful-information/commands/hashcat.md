# HashCat

#### Cracking hashes with Hashcat

In the case of Hashcat, when specifying the <mark style="color:red;">hash-type</mark> you need to specify the <mark style="color:red;">Hash ID</mark> (which can be found in the help page).

<mark style="color:blue;">When using hackcat see the help first.</mark>

* <mark style="color:yellow;">hashcat -a3 -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt</mark>

#### Cracking the SHA512 hash with hashcat

* <mark style="color:yellow;">hashcat -a3 -m 1800 pathtohashfile /usr/share/wordlists/rockyou.txt</mark>
