# Processes

<mark style="color:red;">**Definition:**</mark>

* A process is a running instance of a program in the Linux operating system.

<mark style="color:red;">**Characteristics:**</mark>

* Each process has a unique Process ID (<mark style="color:yellow;">PID</mark>) assigned to it.
* Processes run independently and have their own memory space.
* Processes can run in the background (<mark style="color:yellow;">daemon</mark>) or the foreground.

<mark style="color:red;">**Creation:**</mark>

* Processes are created by the execution of a program or command.

<mark style="color:red;">**Parent and Child Processes:**</mark>

* Processes are organized in a hierarchical structure.
* A parent process can spawn child processes.
* Parent processes may wait for their child processes to complete.

<mark style="color:red;">**Process States:**</mark>

* <mark style="color:green;">Processes can be in different states:</mark>
  * Running: Actively executing and using CPU.
  * Sleeping: Waiting for an event to proceed.
  * Stopped: Suspended or paused.
  * Zombie: Completed but not yet removed from the process table.

<mark style="color:red;">**Process Control:**</mark>

* <mark style="color:yellow;">**ps**</mark>**:** Command to display information about active processes.
  * Example: <mark style="color:blue;">`ps aux`</mark>
* <mark style="color:yellow;">**top**</mark>**:** Dynamic command-line utility to monitor processes.
  * Example: <mark style="color:blue;">`top`</mark>
* <mark style="color:yellow;">**kill**</mark>**:** Terminates a process by sending a signal.
  * Example: <mark style="color:blue;">`kill -9 PID`</mark>

<mark style="color:red;">**Foreground and Background:**</mark>

* Processes can run in the foreground (interactively) or in the background (without user interaction).
* Use <mark style="color:blue;">`&`</mark> to run a command in the background.
  * Example: <mark style="color:blue;">`command &`</mark>

<mark style="color:red;">**Job Control:**</mark>

* <mark style="color:yellow;">**fg**</mark>**:** Brings a background process to the foreground.
  * Example: <mark style="color:blue;">`fg %1`</mark> (brings the job with job <mark style="color:yellow;">ID 1</mark> to the foreground)
* <mark style="color:yellow;">**bg**</mark>**:** Sends a process to the background.
  * Example: <mark style="color:blue;">`bg %1`</mark> (sends the job with job <mark style="color:yellow;">ID 1</mark> to the background)

<mark style="color:red;">**Monitoring and Debugging:**</mark>

* <mark style="color:yellow;">**pstree**</mark>**:** Displays a tree diagram of processes.
  * Example: <mark style="color:blue;">`pstree`</mark>
* <mark style="color:yellow;">**strace**</mark>**:** Traces system calls and signals.
  * Example: <mark style="color:blue;">`strace -p PID`</mark>

Understanding processes is essential for managing system resources and troubleshooting performance issues in a Linux environment.

\
