# SMTP Enumeration

## SMTP Enumeration

* SMTP is a communication protocol that is used for the transmission of email.
* SMTP uses TCP port 25 by  default. It can also be configured to run on TCP port 465 and 587.

## Auxiliary Modules

* <mark style="color:yellow;">**auxiliary/scanner/smtp/smtp\_enum**</mark>
  * Enumerates valid email addresses using VRFY, EXPN, and RCPT TO commands.
* <mark style="color:yellow;">**auxiliary/scanner/smtp/smtp\_version**</mark>
  * Scans and identifies the SMTP server version by connecting to port 25 and parsing the banner.
* <mark style="color:yellow;">**auxiliary/scanner/smtp/smtp\_relay**</mark>
  * Tests SMTP relay functionality by sending an email through the server. This helps in identifying open relay vulnerabilities.
* <mark style="color:yellow;">**auxiliary/scanner/smtp/smtp\_ntlm\_domain**</mark>
  * Identifies NTLM authentication domains supported by an SMTP server. This is useful for targeting NTLM-based authentication systems.
* <mark style="color:yellow;">**auxiliary/server/capture/smtp**</mark>
  * Sets up a fake SMTP server to capture SMTP credentials. This is useful for phishing or MITM-style attacks.

### Netcat Commands

#### Connect to mail server

* "<mark style="color:yellow;">nc demo.ine.local 25</mark>"

#### Identify yourself

* "<mark style="color:yellow;">HELO placeholder</mark>"

#### Check if user exists

* "<mark style="color:yellow;">VRFY user</mark>"

### Possible Code Responses

* <mark style="color:blue;">250</mark>: User exists
* <mark style="color:blue;">550</mark>: User doesn't exist
* <mark style="color:blue;">252</mark>: Cannot verify the user but will accept the message.

#### Quit the session

* "<mark style="color:yellow;">QUIT</mark>"
