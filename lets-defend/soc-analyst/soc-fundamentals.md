# SOC Fundamentals

## What is a SOC?

A Security Operation Center (SOC) is a facility where the information security team continuously monitors and analyzes the security of an organization. The primary purpose of the SOC team is to detect, analyze, and respond to cybersecurity incidents using technology, people, and processes.

### Types of SOC Models

Depending on your security needs and budget, there are several types of SOCs:

<figure><img src="../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

#### In-house SOC

This team is formed when an organization builds its cybersecurity team. Organizations considering an internal SOC should have a budget to support its continuity.

#### Virtual SOC

This type of SOC team does not have a permanent facility and often works remotely in various locations.

#### Co-Managed SOC

The Co-Managed SOC consists of internal SOC staff working with an external Managed Security Service Provider (MSSP). Coordination is key in this type of model.

#### Command SOC

This SOC team oversees smaller SOCs across a large region. Organizations using this model include large telecommunications providers and defense agencies.

### People, Process, and Technology

Building a successful SOC requires serious coordination. Most importantly, there should be a strong relationship between people, processes, and technology.

Simply put, we will discuss the people, processes, and technologies required for SOC.

#### People

A strong SOC team requires highly trained personnel who are familiar with security alerts and attack scenarios. Because attack types are constantly changing, you need team members who can easily adapt to new attack types and are willing to conduct research.

#### Processes

To further develop your SOC structure, you need to align it with many different types of security requirements, such as NIST, PCI, and HIPAA. All processes require extreme standardization of actions to ensure nothing is left out.

#### Technology

The team needs to have different products for many tasks, such as penetration testing, detection, prevention, and analysis, and they need to follow the market and technology closely to find the best solution for the organization. Sometimes the best product on the market may not be the best product for your team. Remember to consider other factors such as the organization's budget.



### SOC Roles

#### SOC Analyst

This role can be categorized as Level 1, 2, and 3 according to the SOC structure. A security analyst classifies the alert, looks for the cause, and advises on remediation.

#### Incident Responder

An Incident Response Officer is an individual responsible for threat detection. This role performs the initial assessment of security breaches.

#### Threat Hunter

A Threat Hunter is a cybersecurity professional who proactively seeks out and investigates potential threats and vulnerabilities within an organization's network or system. They use a combination of manual and automated techniques to detect, isolate, and mitigate advanced persistent threats (APTs) and other sophisticated attacks that may evade traditional security measures. Threat hunters typically have a deep understanding of the organization's IT infrastructure and security posture, as well as knowledge of emerging threats and attack tactics. They aim to find and eliminate threats before they can damage or disrupt the business.

#### Security Engineer

Security engineers are responsible for maintaining the security infrastructure of Security Information and Event Management (SIEM) solutions and security operations center (SOC) products. For example, a security engineer builds the connection between SIEM and Security Orchestration, Automation, and Response (SOAR) products.

#### SOC Manager

A SOC manager takes on management responsibilities such as budgeting, strategizing, managing staff, and coordinating operations. They deal with operational rather than technical issues.



### The Advantages of Being a SOC Analyst

There are many various techniques for attack vectors and malicious software and they increase more and more every day. As an analyst you will get greater enjoyment from investigating these varying types of incidents. Even though the operating systems, security products, etc. that you use will be the same the job will feel less monotonous because you will be analyzing different incidents. Also, you may not encounter such techniques (not every week or every day).

### A Day in the Life of a SOC Analyst

Throughout the day, a SOC analyst typically reviews alerts in the SIEM and determines which ones are real threats. To reach a conclusion, they use various security and protection products such as Endpoint Detection and Response (EDR), Log Management, and SOAR. We will explain in detail why and how these products are used later in the training program.

To be a successful SOC analyst who is not dependent on security products and can correctly analyze SIEM alerts, you must have the following skills and abilities.

#### Operating Systems

To determine what is abnormal in a system, you first need to know what is accepted as normal. For example, there are many services within the Windows operating system, and it is difficult to know which ones are suspicious without knowing which ones are or could be considered normal Windows services. Therefore, you should be familiar with how Windows/Linux operating systems work.

#### Network

First and foremost, in this role, you will be dealing with a lot of malicious IPs and URLs, so you need to confirm that there are no devices on the network trying to connect to those addresses. Once you accomplish that, it will set the direction of the analysis.

This step is a bit more complicated because you may have to find a potential data leak on the network. To perform all of these functions, you need to understand the basics of networking.

#### Malware Analysis

When dealing with most threats, you are likely to encounter some type of malicious software. To understand the real purpose of these malicious programs (they sometimes display different behaviors to fool analysts), you need to have malware analysis skills.

It is important to at least determine what the command and control center of the malicious file is and whether or not there is a device communicating with that address.

In general, we have discussed what a SOC analyst is, what the responsibilities of the role are, and what skills a SOC Analyst needs to have. As the course progresses, it will also cover technical areas, starting with SIEM.



## SIEM and Analyst Relationship

### What is SIEM?

SIEM is a security solution that combines security information and event management, which involves real-time logging of events in an environment. The ultimate purpose of event logging is to detect security threats.

Overall, SIEM products have a lot of features. The ones that interest us most as SOC analysts are those that collect and filter data and provide alerts for suspicious events.

Example alert: If someone on a Windows operating system tries to enter 20 incorrect passwords in 10 seconds, this is suspicious activity. It is unlikely that someone who has forgotten their password would try to re-enter it that many times in such a short period of time. So we create a SIEM rule/filter to detect such activity that exceeds the threshold. Based on this SIEM rule, an alert will be generated when such a situation occurs.



### What is Log Management?

As the name implies, Log Management provides access to all logs in an environment (web logs, OS logs, firewall, proxy, EDR, etc.) and allows you to manage them in one place. This increases efficiency and saves time.

If you can't access the logs from one place, then the same request (e.g., the goal is to determine all users on letsdefend.io) would have to be sent to different devices. This would increase your margin for error and the amount of time you would need to spend.



## EDR - Endpoint Detection and Response

### What is EDR?

Endpoint Detection and Response (EDR), also known as Endpoint Threat Detection and Response (ETDR), is an integrated endpoint security solution that combines continuous, real-time monitoring and collection of endpoint data with rules-based automated response and analysis capabilities. (Definition source: mcafee.com)



## SOAR (Security Orchestration Automation and Response)

SOAR stands for Security Orchestration Automation and Response. It enables security products and tools in an environment to work together, streamlining the tasks of SOC team members. For example, it will automatically search VirusTotal for the source IP of a SIEM alert, reducing the workload of the SOC analyst.

Some SOAR products commonly used in the industry:

* Splunk Phantom
* IBM Resilient
* Logsign
* Demisto

<figure><img src="../../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

### Saves You Time

SOAR saves time with workflows that automate processes. Some common workflows are:

* IP address reputation control
* Hash query
* Scanning an acquired file in a sandbox environment
* …



### Centralization (A single platform for everything you need)

It allows you to use different security tools in your environment (sandbox, log management, 3rd party tools, etc.) by providing an all-in-one software. These tools are integrated into the SOAR solution and can be used on the same platform.

<figure><img src="../../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>



## Threat Intelligence Feed

A Threat Intelligence Feed is data (such as malware hashes, C2 (Command\&Control) domain/IP addresses etc.) provided by a third party company.

\
The data here consists of artifacts from previous malicious activity. It could be the hash of malware or the IP address of a command and control center. As a SOC analyst, you need to search threat intelligence feeds to determine if a hash file at hand has ever been used in a malicious scenario in the past.

Here are some free and popular sources you can use:

* [VirusTotal](https://www.virustotal.com/)
* [Talos Intelligence](https://talosintelligence.com/)























































