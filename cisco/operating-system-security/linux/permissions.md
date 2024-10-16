# Permissions

<mark style="color:red;">**Three Permission Categories:**</mark>

* Permissions are categorized for <mark style="color:yellow;">Owner</mark>, <mark style="color:yellow;">Group</mark>, and <mark style="color:yellow;">Others</mark>.

<mark style="color:red;">**Three Permission Types:**</mark>

* Each category has three permission types: <mark style="color:yellow;">Read</mark>, <mark style="color:yellow;">Write</mark>, and <mark style="color:yellow;">Execute</mark>.

<mark style="color:red;">**Symbolic Representation:**</mark>

* Permissions are symbolically represented as three characters: r (read), w (write), and x (execute).

<mark style="color:red;">**Numeric Representation:**</mark>

* Numeric representation uses a three-digit code: <mark style="color:purple;">4</mark> (read), <mark style="color:purple;">2</mark> (write), <mark style="color:purple;">1</mark> (execute).
* Summing these values assigns a unique code to each permission set.

<mark style="color:red;">**Example:**</mark>

* Permission set <mark style="color:blue;">"rwxr--r--"</mark> means the Owner has read, write, and execute; the Group has read-only, and Others have read-only.

<mark style="color:red;">**Changing Permissions:**</mark>

* Permissions can be modified using the <mark style="color:blue;">`chmod`</mark> command.
* For example, <mark style="color:blue;">`chmod 755 filename`</mark> grants read, write, and execute to the Owner, and read and execute to Group and Others.

<mark style="color:red;">**Ownership:**</mark>

* Files and directories have an Owner and a Group assigned.
* Owners can modify permissions, and some operations require appropriate ownership.

<mark style="color:red;">**Special Permissions:**</mark>

* Setuid, setgid, and sticky bit are special permissions providing additional functionality.

<mark style="color:red;">**Viewing Permissions:**</mark>

* Use the <mark style="color:blue;">`ls -l`</mark> command to view detailed file and directory permissions.

<mark style="color:red;">**Security Implications:**</mark>

* Proper permission management enhances system security by controlling access to files and directories.

<mark style="color:red;">**Common Commands:**</mark>

* <mark style="color:blue;">`chmod`</mark>: Changes file permissions.
* <mark style="color:blue;">`chown`</mark>: Changes file ownership.
* <mark style="color:blue;">`chgrp`</mark>: Changes file group ownership.

<mark style="color:red;">**In Summary:**</mark>

* Permissions are categorized for Owner, Group, and Others.
* Three permission types: Read, Write, and Execute.
* Represented symbolically or numerically.
* Owners can modify permissions.
* Special permissions provide additional functionality.
* Vital for controlling access and ensuring system security.

\
