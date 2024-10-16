# Record Types

DNS isn't just for websites though, and multiple types of DNS record exist. We'll go over some of the most common ones that you're likely to come across.\


<mark style="color:red;">A Record:</mark>

* These records resolve to IPv4 addresses, for example <mark style="color:blue;">104.26.10.229</mark>

<mark style="color:red;">AAAA Record:</mark>

* These records resolve to IPv6 addresses, for example <mark style="color:blue;">2606:4700:20::681a:be5</mark>

<mark style="color:red;">CNAME Record:</mark>

* These records resolve to another domain name, for example, TryHackMe's online shop has the subdomain name <mark style="color:blue;">store.tryhackme.com</mark> which returns a CNAME record <mark style="color:blue;">shops.shopify.com</mark>. Another DNS request would then be made to <mark style="color:blue;">shops.shopify.com</mark> to work out the IP address.

<mark style="color:red;">MX Record:</mark>

* These records resolve to the address of the servers that handle the email for the domain you are querying, for example an MX record response for tryhackme.com would look something like alt1.aspmx.l.google.com. These records also come with a priority flag. This tells the client in which order to try the servers, this is perfect for if the main server goes down and email needs to be sent to a backup server.

<mark style="color:red;">TXT Record:</mark>

* TXT records are free text fields where any text-based data can be stored. TXT records have multiple uses, but some common ones can be to list servers that have the authority to send an email on behalf of the domain (this can help in the battle against spam and spoofed email). They can also be used to verify ownership of the domain name when signing up for third party services.
