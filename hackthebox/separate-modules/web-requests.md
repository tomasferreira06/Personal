# Web Requests

## URL

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

## **HTTP Flow**

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

**Note:** All browser usually first look up record in the local ‘etc/hosts’ file, and if the requested domain does not exist within it, then they contact other DNS servers. You can manually add records in this file for DNS resolution.

### **cURL**

* Is a command line tool and library that primarily supports HTTP along with many other protocols.

#### **cURL Commands**

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

**Note:** We can specify a file name to save as when downloading a file using the -o flag, example: “curl -o examplefile.txt [inlanefreight.com/index.html](http://inlanefreight.com/index.html)”

## **HTTPS Flow**

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

#### Example of contacting a website with an invalid SSL certificate:

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

We can skip the certification check by using the <mark style="color:red;">-k</mark> flag

### **HTTP Requests**

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

The first line of any HTTP request contains three main fields 'separated by spaces':

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

**Note:** HTTP version 1.X sends request in clear-text, and uses a new-line character to separate different fields and different requests. HTTP version 2.X, on the other hand, sends requests as binary data in a dictionary form.

### **HTTP Response**

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

### **API**

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

* In general, APIs perform 4 main operations on the requested database entity:

#### **API Commands**

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
