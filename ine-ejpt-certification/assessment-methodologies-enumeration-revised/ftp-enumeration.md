# FTP Enumeration

## FTP Enumeration

* FTP is a protocol that uses <mark style="color:red;">TCP port 21</mark> and is used to facilitate file sharing between a server and client/clients.
* FTP authentication utilizes a username and password combination, however, in some cases an improperly configured FTP server can be logged into anonymously.
* We can use multiple auxiliary modules to enumerate information as well as perform brute-foce attacks on targets running an FTP server.

## Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_version`**</mark>: Identifies the FTP server version.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/anonymous`**</mark>: Checks if anonymous login is allowed on the FTP server.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_login`**</mark>: Attempts to brute force FTP login credentials.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_banner`**</mark>: Retrieves the banner of the FTP server for fingerprinting.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_enum`**</mark>: Enumerates FTP users by checking for specific usernames.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_passwd`**</mark>: Attempts to gather FTP user password hashes (for certain FTP servers).
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_ls`**</mark>: Lists files and directories on the FTP server.
* <mark style="color:yellow;">**`auxiliary/scanner/ftp/ftp_bruteforce_dirs`**</mark>: Attempts to brute force the names of directories on the FTP server.
