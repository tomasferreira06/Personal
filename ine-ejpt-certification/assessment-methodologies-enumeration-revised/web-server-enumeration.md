# Web Server Enumeration

## Web Server Enumeration

* A web server is software that is used to serve website data on the web.
* Web  servers utilize HTTP to facilitate the communication between clients and the web server.
* HTTP is an application layer protocol that utilizes TCP port 80 for communication.

## Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/http/apache_userdir_enum`**</mark>: Enumerates Apache web server user directories based on mod\_userdir.
* <mark style="color:yellow;">**`auxiliary/scanner/http/brute_dirs`**</mark>: Brute forces directory names on the target web server.
* <mark style="color:yellow;">**`auxiliary/scanner/http/dir_scanner`**</mark>: Scans for common directories on the web server.
* <mark style="color:yellow;">**`auxiliary/scanner/http/dir_listing`**</mark>: Detects directory listing vulnerabilities on the target web server.
* <mark style="color:yellow;">**`auxiliary/scanner/http/http_put`**</mark>: Tests if the HTTP PUT method is enabled (can allow file uploads).
* <mark style="color:yellow;">**`auxiliary/scanner/http/files_dir`**</mark>: Searches for sensitive files in specific directories on the web server.
* <mark style="color:yellow;">**`auxiliary/scanner/http/http_login`**</mark>: Brute forces HTTP authentication login credentials.
* <mark style="color:yellow;">**`auxiliary/scanner/http/http_header`**</mark>: Retrieves and analyzes HTTP headers for potential information leakage.
* <mark style="color:yellow;">**`auxiliary/scanner/http/http_version`**</mark>: Identifies the HTTP server version.
* <mark style="color:yellow;">**`auxiliary/scanner/http/robots_txt`**</mark>: Scans for and retrieves the <mark style="color:green;">`robots.txt`</mark> file, which can reveal directories that should be restricted.
