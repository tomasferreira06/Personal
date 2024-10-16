# Download/Serving Files

<mark style="color:red;">**Downloading Files:**</mark>

* <mark style="color:green;">**wget:**</mark>
  * Command for downloading files from the web via HTTP.
  * Example: <mark style="color:blue;">`wget https://example.com/file.zip`</mark>

<figure><img src="../../../../.gitbook/assets/Capture (41).PNG" alt=""><figcaption></figcaption></figure>

* <mark style="color:green;">**curl:**</mark>
  * Tool for transferring data with URLs.
  * Example: <mark style="color:blue;">`curl -O https://example.com/file.tar.gz`</mark>
* <mark style="color:green;">**scp:**</mark>
  * Securely copy files between different hosts.
  * Example: <mark style="color:blue;">`scp username@remote:/path/to/file.txt`</mark>&#x20;
* <mark style="color:green;">**rsync:**</mark>
  * Syncs files and directories between two locations.
  * Example: <mark style="color:blue;">`rsync -avz username@remote:/path/to/files/`</mark>

<mark style="color:red;">**Serving Files:**</mark>

* <mark style="color:green;">**python -m SimpleHTTPServer (Python 2) / python -m http.server (Python 3):**</mark>
  * Launches a simple HTTP server in the current directory.
  * Example: <mark style="color:blue;">`python -m SimpleHTTPServer 8000`</mark>

<figure><img src="../../../../.gitbook/assets/Capture (42).PNG" alt=""><figcaption></figcaption></figure>

* <mark style="color:green;">**nginx:**</mark>
  * A high-performance HTTP server and reverse proxy server.
  * Example: <mark style="color:blue;">`sudo apt-get install nginx`</mark> (<mark style="color:yellow;">Install</mark>) / <mark style="color:blue;">`sudo service nginx start`</mark> (<mark style="color:yellow;">Start</mark>)
* <mark style="color:green;">**Apache HTTP Server:**</mark>
  * A widely used web server.
  * Example: <mark style="color:blue;">`sudo apt-get install apache2`</mark> (<mark style="color:yellow;">Install</mark>) / <mark style="color:blue;">`sudo service apache2 start`</mark> (<mark style="color:yellow;">Start</mark>)
* <mark style="color:green;">**Node.js (http-server):**</mark>
  * A simple, zero-configuration command-line HTTP server.
  * Example: <mark style="color:blue;">`npm install -g http-server`</mark> (<mark style="color:yellow;">Install</mark>) / <mark style="color:blue;">`http-server`</mark> (<mark style="color:yellow;">Start</mark>)
* <mark style="color:green;">**netcat (nc):**</mark>
  * Simple tool for reading and writing data across network connections.
  * Example for serving a file: <mark style="color:blue;">`nc -l -p 8080 < file.txt`</mark>

These commands provide various options for downloading files from the web or serving files from your host.&#x20;

\
