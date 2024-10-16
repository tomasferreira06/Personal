# Interact with the File System



For more commands see: [_<mark style="color:blue;">https://www.die.net/</mark>_](https://www.die.net/)

<mark style="color:red;">**`ls`**</mark><mark style="color:red;">**:**</mark>

* Lists files and directories in the current directory.

<mark style="color:red;">**`cd`**</mark><mark style="color:red;">**:**</mark>

* Changes the current working directory.
* Example: <mark style="color:blue;">`cd /path/to/directory`</mark>

<mark style="color:red;">**`pwd`**</mark><mark style="color:red;">**:**</mark>

* Prints the current working directory.

<mark style="color:red;">**`mkdir`**</mark><mark style="color:red;">**:**</mark>

* Creates a new directory.
* Example: <mark style="color:blue;">`mkdir new_directory`</mark>

<mark style="color:red;">**`rm`**</mark><mark style="color:red;">**:**</mark>

* Removes (deletes) files or directories.
* Example: <mark style="color:blue;">`rm filename`</mark> or <mark style="color:blue;">`rm -r directory`</mark>

<mark style="color:red;">**`cp`**</mark><mark style="color:red;">**:**</mark>

* Copies files or directories.
* Example: <mark style="color:blue;">`cp file1 file2`</mark> or <mark style="color:blue;">`cp -r dir1 dir2`</mark>

<mark style="color:red;">**`mv`**</mark><mark style="color:red;">**:**</mark>

* Moves or renames files or directories.
* Example: <mark style="color:blue;">`mv oldname newname`</mark> or <mark style="color:blue;">`mv file /path/to/newlocation`</mark>

<mark style="color:red;">**`touch`**</mark><mark style="color:red;">**:**</mark>

* Creates an empty file or updates a file's timestamp.
* Example: <mark style="color:blue;">`touch filename`</mark>

<mark style="color:red;">**`cat`**</mark><mark style="color:red;">**:**</mark>

* Displays the content of a file.
* Example: <mark style="color:blue;">`cat filename`</mark>

<mark style="color:red;">**`more`**</mark><mark style="color:red;">** **</mark><mark style="color:red;">**/**</mark><mark style="color:red;">** **</mark><mark style="color:red;">**`less`**</mark><mark style="color:red;">**:**</mark>

* Paginates through the content of a file.
* Example: <mark style="color:blue;">`more filename`</mark> or <mark style="color:blue;">`less filename`</mark>

<mark style="color:red;">**`nano`**</mark><mark style="color:red;">** **</mark><mark style="color:red;">**/**</mark><mark style="color:red;">** **</mark><mark style="color:red;">**`vim`**</mark><mark style="color:red;">**:**</mark>

* Opens a text editor to create or edit files.
* Example: <mark style="color:blue;">`nano filename`</mark> or <mark style="color:blue;">`vim filename`</mark>

{% content-ref url="../text-editors/vim.md" %}
[vim.md](../text-editors/vim.md)
{% endcontent-ref %}

{% content-ref url="../text-editors/nano.md" %}
[nano.md](../text-editors/nano.md)
{% endcontent-ref %}

<mark style="color:red;">**`find`**</mark><mark style="color:red;">**:**</mark>

* Searches for files and directories in a directory hierarchy.
* Example: <mark style="color:blue;">`find /path/to/search -name "filename"`</mark>

<mark style="color:red;">**`grep`**</mark><mark style="color:red;">**:**</mark>

* Searches for a specific pattern in files.
* Example: <mark style="color:blue;">`grep "pattern" filename`</mark>

<mark style="color:red;">**`chmod`**</mark><mark style="color:red;">**:**</mark>

* Changes file permissions.
* Example: <mark style="color:blue;">`chmod 755 filename`</mark>

<mark style="color:red;">**`chown`**</mark><mark style="color:red;">**:**</mark>

* Changes file ownership.
* Example: <mark style="color:blue;">`chown user:group filename`</mark>

<mark style="color:red;">**`df`**</mark><mark style="color:red;">**:**</mark>

* Displays information about disk space usage.

<mark style="color:red;">**`du`**</mark><mark style="color:red;">**:**</mark>

* Shows the disk usage of files and directories.

<mark style="color:red;">**`ln`**</mark><mark style="color:red;">**:**</mark>

* Creates hard or symbolic links.
* Example: <mark style="color:blue;">`ln -s target linkname`</mark>

