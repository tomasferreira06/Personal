# Cookies

Cookies are saved when you receive a "Set-Cookie" header from a web server. Then every further request you make, you'll send the cookie data back to the web server.&#x20;

Because HTTP is stateless (doesn't keep track of your previous requests), cookies can be used to remind the web server who you are, some personal settings for the website or whether you've been to the website before.

&#x20;<mark style="color:red;">Let's take a look at this as an example HTTP request:</mark>

<figure><img src="../../../../../.gitbook/assets/Capture (30).PNG" alt=""><figcaption></figcaption></figure>

Cookies can be used for many purposes but are most commonly used for website authentication.&#x20;

The cookie value won't usually be a clear-text string where you can see the password, but a token (unique secret code that isn't easily humanly guessable).
