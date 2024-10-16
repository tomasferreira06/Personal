# Port Scanning with Auxiliary Modules

## Auxiliary Modules

This modules are used to perform functionality like scanning, discovery and fuzzing.

Auxiliary modules can be used during the information gathering phase of a pentest as well as the post exploitation phase.

They can also be used to discover hosts  and perform port scanning on a different network subnet aafter we have obtained initial access on a target system.

## Lab Infrastructure

* Our objective is to utilize auxiliary modules to discover open ports on our first target.
* The next step will involve exploiting the service running on the target in order to obtain a foothold.
* We will then utilize our foothold to access other systems on a different network subnet (pivoting)
* We will then utilize auxiliary modules to scan for open ports on the second target.
