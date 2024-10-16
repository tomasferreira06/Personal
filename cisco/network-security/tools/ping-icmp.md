# Ping(ICMP)

Ping is one of the most fundamental network tools available to us.&#x20;

<mark style="color:yellow;">ICMP (Internet Control Message Protocol)</mark> uses packets to determine the performance of a connection between devices, if the connection exists or is reliable.

Ping measures the time taken for packets to travel between devices. This measuring is done using ICMP's echo packet and then ICMP's echo reply from the target device.

Pings can be performed against devices on a network.

The syntax to ping is; <mark style="background-color:red;">ping IP address or website URL.</mark>

<figure><img src="../../../.gitbook/assets/Capture (5).PNG" alt=""><figcaption></figcaption></figure>

In the above example we are pinging a device that has the private addres of _192.168.1.254._

Ping informs us that we have sent six ICMP packets, all of which were received with an average time of 4.16 seconds.
