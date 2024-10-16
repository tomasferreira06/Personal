# Web Application Firewall (WAF)

A WAF sits between your web request and the web server; its primary purpose is to protect the webserver from hacking or denial of service attacks.&#x20;

It analyses the web requests for common attack techniques, whether the request is from a real browser rather than a bot.

&#x20;It also checks if an excessive amount of web requests are being sent by utilising something called rate limiting, which will only allow a certain amount of requests from an IP per second.

If a request is deemed a potential attack, it will be dropped and never sent to the webserver.

<figure><img src="../../../../.gitbook/assets/Capture (35).PNG" alt=""><figcaption></figcaption></figure>

