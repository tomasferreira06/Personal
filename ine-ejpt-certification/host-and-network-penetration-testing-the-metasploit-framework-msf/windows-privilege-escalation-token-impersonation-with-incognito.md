# Windows Privilege Escalation: Token Impersonation With Incognito

## Practice Demo

Obtain initial access to the target

In this case we used again the <mark style="color:red;">rejetto\_http\_file\_server</mark> module.

#### Load Incognito

* <mark style="color:yellow;">load incognito</mark>

#### List  User account tokens

* <mark style="color:yellow;">list\_tokens -u</mark>

#### Impersonate Access token

* <mark style="color:yellow;">impersonate\_token 'NAMEOFTOKEN'</mark>

After getting the Administrator token impersonated, we still have to migrate a process under the Administrator account to get the privs.

After impersonating the <mark style="color:red;">Administrator</mark> access token, we gain access to more access tokens for example <mark style="color:red;">NT AUTHORITY\SYSTEM</mark>

If after initial access we dont have any delegation Tokens available, we have to execute a <mark style="color:green;">potato</mark> attack, which will generate an <mark style="color:red;">NT AUTHORITY\SYSTEM</mark> and then you can impersonate it.
