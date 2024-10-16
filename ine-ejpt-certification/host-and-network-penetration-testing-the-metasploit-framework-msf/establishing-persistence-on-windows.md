# Establishing Persistence On Windows

* Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access.
* Gaining an initial foothold is not enough, you need to setup and maintain persistent access to your targets.
* We can utilize various post exploitation persistence modules to ensure that we always have access to the target system.

## Practice Demo

Enumerate the target.

We have the rejetto HFS service

### Achieving persistence

* <mark style="color:yellow;">exploit/windows/local/persistence\_service</mark>

Set payload to 32-bit

* <mark style="color:yellow;">windows/meterpreter/reverse\_tcp</mark>

<mark style="color:purple;">NOTE:</mark> This module only supports staged payload

Give the <mark style="color:red;">SERVICE\_NAME</mark> a very sneaky name

To regain access to the target, we have to setup a multi/handler

* <mark style="color:yellow;">exploit/multi/handler</mark>: Set the options to the same as the persistence service
