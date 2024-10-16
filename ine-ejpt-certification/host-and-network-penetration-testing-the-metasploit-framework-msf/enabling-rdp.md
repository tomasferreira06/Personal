# Enabling RDP

* The Remote Desktop Protocol is a proprietary GUI remote access protocol developed by Microsoft and is used to remotely connect and interact with a Windows system.
* RDP uses <mark style="color:red;">TCP port 3389</mark> by default.
* RDP is disabled by default, however, we can utilize an MSF exploit module to enable RDP on the Windows target and consequently utilize RDP to remotely access the target system.
* RDP authentication requires a legitimate user account on the target system as well as the user's password in clear-text.

## Practice Demo

Enumerate the target

In this target <mark style="color:red;">BadBlue</mark> is running

Set the required options including the <mark style="color:red;">TARGET</mark>

### Enable RDP  module

* <mark style="color:yellow;">post/windows/manage/enable\_rdp</mark>: Enables RDP and opens firewall on port 3389

<mark style="color:purple;">NOTE:</mark> You can also create a new account with the <mark style="color:red;">enable\_rdp</mark> module

Now we change the existing Administrator account password:

* <mark style="color:yellow;">net user administrator 'newpassword'</mark>

To connect to rdp run:

* <mark style="color:yellow;">xfreerdp /u:administrator /p:'password' /v:targetIP</mark>





