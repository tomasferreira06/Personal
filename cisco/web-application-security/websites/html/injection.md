# Injection

<mark style="color:red;">**Definition:**</mark>

* HTML injection is a type of web security vulnerability where an attacker injects malicious HTML code into a webpage to manipulate its content or execute harmful actions.

<mark style="color:red;">**Input Fields Targeted:**</mark>

* Attackers typically exploit input fields, such as text boxes or form fields, where user input is not properly validated or sanitized.

<mark style="color:red;">**Injection Types:**</mark>

* <mark style="color:green;">**Stored (Persistent):**</mark>
  * Malicious code is permanently stored on the server and served to multiple users when they access the affected page.
* <mark style="color:green;">**Reflected (Non-Persistent):**</mark>
  * Malicious code is included in a URL, and users are tricked into clicking the manipulated link, causing the code to be executed for that user.

<mark style="color:red;">**Objective:**</mark>

* Injected code can alter the appearance of the webpage, steal sensitive information, redirect users to malicious sites, or perform actions on behalf of the user.

<mark style="color:red;">**Common Attack Vectors:**</mark>

* Exploiting comment sections, input forms, or any user-controlled input areas on a website.

<mark style="color:red;">**Mitigation Strategies:**</mark>

* <mark style="color:green;">**Input Validation:**</mark>
  * Validate and sanitize user inputs to ensure they do not contain malicious code.
* <mark style="color:green;">**Content Security Policy (CSP):**</mark>
  * Implement CSP headers to control which resources are allowed to be loaded, reducing the risk of code injection.
* <mark style="color:green;">**Escaping Characters**</mark>**:**
  * Convert special characters in user input to their HTML entity equivalents to prevent code execution.

<mark style="color:red;">**Examples:**</mark>

* Injecting script tags to execute JavaScript code.
* Modifying form fields to capture sensitive information.
* Embedding iframes to redirect users to phishing sites.

<mark style="color:red;">**Impact:**</mark>

* Can lead to the theft of user credentials, spreading malware, defacement of websites, or other malicious activities.

<mark style="color:red;">**User Awareness:**</mark>

* Users should be cautious about clicking on untrusted links and providing sensitive information on websites.

<mark style="color:red;">**In Summary:**</mark>

* HTML injection involves inserting malicious code into webpages.
* Exploits vulnerabilities in input fields.
* Can be persistent or non-persistent.
* Mitigated through input validation, Content Security Policy, and character escaping.

<figure><img src="../../../../.gitbook/assets/Capture (33).PNG" alt=""><figcaption></figcaption></figure>

\
