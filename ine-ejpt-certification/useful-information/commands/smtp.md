# SMTP

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
