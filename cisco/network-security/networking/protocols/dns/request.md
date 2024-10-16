# Request

* When you want to visit a website (like [www.tryhackme.com](http://www.tryhackme.com/)), your computer checks if it knows the website's address from before. If not, it asks your ISP's server (Recursive DNS Server).
* The Recursive DNS Server also has a memory of recently visited websites. If it knows the address, it tells your computer, and you're good (this happens a lot for popular sites).
* If the Recursive DNS Server doesn't know, it starts a journey. It begins with the root DNS servers, the backbone of the internet.
* The root servers guide your request to the right Top Level Domain (TLD) Server. For example, for [www.tryhackme.com](http://www.tryhackme.com/), it goes to the .com TLD server.
* The TLD server knows where to find the authoritative server (nameserver) for the specific domain (like tryhackme.com). For tryhackme.com, it's kip.ns.cloudflare.com and uma.ns.cloudflare.com.
* The authoritative server holds the official records for the domain. If you need an address, it gives the answer.
* This answer goes back to the Recursive DNS Server, which keeps a copy for a while (this is caching), making future requests faster.
* The final answer reaches your computer, and you can now access the website.
* DNS records have a TTL (Time To Live) value, which is like an expiration date for the answer. This helps in not asking for the same thing too often.

<figure><img src="../../../../../.gitbook/assets/Capture (22).PNG" alt=""><figcaption></figcaption></figure>

\
