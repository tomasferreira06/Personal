# Alternate Data Streams

## Alternate Data Streams (ADS)

* ADS is an NFTS  (New Technology File System) file attribute and was designed to provide compatibility with the MacOS HFS (Hierarchical File System).
*   Any file created on an NFTS formatted drive will have two different forks/streams.

    * <mark style="color:red;">Data stream</mark> - Default stream that contains the data of the file.
    * <mark style="color:red;">Resource stream</mark> - Typically contains the metadata of the file.


* Attacker can use ADS to hide malicious code or executables in legitimate files in order to evade detection.
* This can be done by storing the malicious code or exectuables in the file attribute resource stream (Metadata) of a legitimate file.&#x20;
* This technique is usually used to evade signature based AVs and static scanning tools.

<mark style="color:purple;">NOTE:</mark> To get to the metadata of a file do:

* Right click file
* Properties
* Details

## Practice Demo

Create <mark style="color:red;">secret.txt</mark> in the resource stream of <mark style="color:red;">test.txt</mark>:

* <mark style="color:yellow;">notepad test.txt:secret.txt</mark>

<mark style="color:purple;">NOTE:</mark> When executing the file that will be opened for us to write in will be <mark style="color:red;">secret.txt</mark>..when saved it wont be anywhere, but in the resource stream of <mark style="color:red;">test.txt</mark>.

#### Inserting Winpeas into the resource stream of a file

* <mark style="color:yellow;">type winpeas.exe > windowslog.txt:winpeas.exe</mark>

Now you would enter normal data into the windowslog.txt to not be suspicious.

#### Navigate to discreet windows directory and create a symbolic link to be able to execute the payload:

* <mark style="color:yellow;">mklink 'nameoflink.exe abspathtopayload</mark>

<mark style="color:purple;">NOTE</mark>: Has to be run as Administrator

Now to execute the payload just run:

* <mark style="color:yellow;">nameoflink</mark>
