# Importing Nmap Scan Results into MSF

In order to optimize your workflow on Metasploit you can even upload the saved nmap scans into the Metasploit Framework.

#### To achieve this run:

* <mark style="color:yellow;">service postgresql start</mark>
* Inside Metasploit run:
  * <mark style="color:yellow;">workspace -a pentest1</mark>: Adds a new workspace called <mark style="color:green;">pentest1</mark>
  * <mark style="color:yellow;">db\_status</mark>: To confirm Metasploit is connected to the database
  * <mark style="color:yellow;">db\_import specifyfile</mark>: Import nmap scan file
  * <mark style="color:yellow;">hosts</mark>: To see the imported nmap results
  * <mark style="color:yellow;">services</mark>: To display open ports and services related to the imported results&#x20;
  * <mark style="color:yellow;">db\_nmap</mark>: Allows you to run nmap from inside the metasploit framework saving the results automatically to the database and updating the information related to that specific host. You can add whatever flags you like.

<mark style="color:purple;">NOTE:</mark> The nmap results have to be in <mark style="color:red;">XML</mark> format to be saved in the metasploit framework.
