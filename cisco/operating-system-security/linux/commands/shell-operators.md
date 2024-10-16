# Shell Operators

<mark style="color:red;">**Redirection Operators:**</mark>

* <mark style="color:blue;">`<`</mark>: Redirects standard input from a file.
  * Example: <mark style="color:blue;">`command < inputfile`</mark>
* <mark style="color:blue;">`>`</mark>: Redirects standard output to a file, overwriting its contents.
  * Example: <mark style="color:blue;">`command > outputfile`</mark>
* <mark style="color:blue;">`>>`</mark>: Redirects standard output to a file, appending to its contents.
  * Example: <mark style="color:blue;">`command >> outputfile`</mark>
* <mark style="color:blue;">`2>`</mark>: Redirects standard error to a file.
  * Example: <mark style="color:blue;">`command 2> errorfile`</mark>
* <mark style="color:blue;">`2>>`</mark>: Redirects standard error to a file, appending to its contents.
  * Example: <mark style="color:blue;">`command 2>> errorfile`</mark>
* <mark style="color:blue;">`|`</mark>: Connects the output of one command as the input to another command (pipe).
  * Example: <mark style="color:blue;">`command1 | command2`</mark>

<mark style="color:red;">**Background and Foreground Execution:**</mark>

* <mark style="color:blue;">`&`</mark>: Executes a command in the background.
  * Example: <mark style="color:blue;">`command &`</mark>
* <mark style="color:blue;">`fg`</mark>: Brings a background process to the foreground.
  * Example: <mark style="color:blue;">`fg %1`</mark> (brings the job with job <mark style="color:yellow;">ID 1</mark> to the foreground)

<mark style="color:red;">**Command Separator:**</mark>

* <mark style="color:blue;">`;`</mark>: Separates multiple commands on a single line.
  * Example: <mark style="color:blue;">`command1 ; command2`</mark>

<mark style="color:red;">**Logical Operators:**</mark>

* <mark style="color:blue;">`&&`</mark>: Executes the second command only if the first command succeeds.
  * Example: <mark style="color:blue;">`command1 && command2`</mark>
* <mark style="color:blue;">`||`</mark>: Executes the second command only if the first command fails.
  * Example: <mark style="color:blue;">`command1 || command2`</mark>

<mark style="color:red;">**Job Control:**</mark>

* <mark style="color:blue;">`Ctrl+C`</mark>: Interrupts the currently running foreground process.
* <mark style="color:blue;">`Ctrl+Z`</mark>: Suspends the currently running foreground process.

<mark style="color:red;">**Quoting and Escape Characters:**</mark>

* <mark style="color:blue;">`"`</mark> and <mark style="color:blue;">`'`</mark>: Used for quoting strings.
  * Example: <mark style="color:blue;">`echo "Hello"`</mark> or <mark style="color:blue;">`echo 'Hello'`</mark>
* <mark style="color:blue;">`\`</mark>: Escapes a special character to be treated as a literal character.
  * Example: <mark style="color:blue;">`echo \$HOME`</mark> (prints the literal string <mark style="color:yellow;">$HOME</mark>)

<mark style="color:red;">**Wildcard Characters:**</mark>

* <mark style="color:blue;">`*`</mark>: Matches any sequence of characters.
  * Example: <mark style="color:blue;">`ls *.txt`</mark> (lists all files with a <mark style="color:yellow;">.txt</mark> extension)
* <mark style="color:blue;">`?`</mark>: Matches any single character.
  * Example: <mark style="color:blue;">`ls file?.txt`</mark> (lists files like <mark style="color:yellow;">file1.txt</mark>, <mark style="color:yellow;">file2.txt</mark>)

<mark style="color:red;">**Command Substitution:**</mark>

* <mark style="color:blue;">`` `command` ``</mark> or <mark style="color:blue;">`$(command)`</mark>: Executes the command and replaces it with its output.
  * Example: <mark style="color:blue;">`echo Today is $(date)`</mark>

These operators and symbols provide powerful ways to control and manipulate commands and processes in the Linux shell.

\
