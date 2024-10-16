# Firewall Detection & IDS Evasion

## Practice Demo

Commands:

* "<mark style="color:yellow;">-sA</mark>": Performs an ACK scan, based on the response determines if a firewall is active or not
* "<mark style="color:yellow;">-f</mark>": Fragments packets
  * "<mark style="color:yellow;">f --mtu</mark>": Sets the maximum transmission unit for each fragmented packet (minimum is 8)
* "<mark style="color:yellow;">--data-length</mark>": Append random data to sent packets
* "<mark style="color:yellow;">-D</mark>": Set a decoy IP, spoofs your IP to the defined one
  * Good decoy is using the default gateway IP
* "<mark style="color:yellow;">-g</mark>": Set a source port for our scan
