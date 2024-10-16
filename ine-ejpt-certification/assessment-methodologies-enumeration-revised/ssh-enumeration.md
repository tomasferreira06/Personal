# SSH Enumeration

## SSH Enumeration

* SSH is a remote administration protocol that offers encryption and is the successor to Telnet.
* It is typically used for remote access  to servers and systems.
* SSH uses  TCP port 22 by default, however, like other services, it can be configured to use any other open TCP port.

## Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_version`**</mark>: Retrieves the SSH server version and banner information.
* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_login`**</mark>: Attempts to brute force SSH login credentials.
* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_login_pubkey`**</mark>: Attempts to log in to the SSH server using public/private key pairs.
* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_enumusers`**</mark>: Enumerates valid SSH usernames by sending authentication requests.
* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_identify_pubkeys`**</mark>: Attempts to identify if specific public keys are accepted by the SSH server.
* <mark style="color:yellow;">**`auxiliary/scanner/ssh/ssh_auth_methods`**</mark>: Enumerates the available authentication methods supported by the SSH server.

