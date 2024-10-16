# Linux

* <mark style="color:yellow;">post/linux/manage/sshkey\_persistence:</mark>
* <mark style="color:yellow;">exploit/linux/at\_package\_manager\_persistence</mark>: Will run a payload everytime the package manager is used. <mark style="color:red;">NOT GREAT</mark>
* <mark style="color:yellow;">exploit/linux/local/cron\_persistence</mark>: Creates a cron job that connects to your handler
  * Default timing is 60 seconds
  * Make sure LPORT is not conflicting
* <mark style="color:yellow;">exploit/linux/local/service\_persistence:</mark> Creates a service on the target, marks it for auto-restart. Enough access is needed to write services files and potentially restart them
  * Set the payload
* <mark style="color:yellow;">exploit/linux/manage/sshkey\_persistence</mark>: Sets up a key pair and adds the public key to the home directories of a specified user or all users on the target system. <mark style="color:red;">GREAT MODULE</mark>
  * set CREATESSHFOLDER true
  * set SESSION

