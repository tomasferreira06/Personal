# Information Gathering

This is the phase in which we gather all available information about the company, its employees and infrastructure, and how they are organized.

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

All the steps we take to exploit the vulnerabilities are based on the information we enumerate about our targets.

We can obtain the necessary information relevant to us in many different ways. However, we can divide them into the following categories:

* Open-Source Intelligence
* Infrastructure Enumeration
* Service Enumeration
* Host Enumeration

All four categories should and must be performed by us for each penetration test. This is because the `information` is the main component that leads us to successful penetration testing and identifying security vulnerabilities.



### Open-Source Intelligence

OSINT is a process for finding publicly available information on a target company or individuals that allows the identification of events (i.e., public and private meetings), external and internal dependencies, and connections. OSINT uses public (Open-Source) information from freely available sources to obtain the desired results.

&#x20;Repositories on sites like [Github](https://github.com/) or other development platforms are often not set up correctly, and external viewers can see this information. If this type of sensitive information is found at the onset of testing, the Incident Handling and Report section of the RoE should describe the procedure for reporting these types of critical security vulnerabilities.

Publicly published passwords or SSH keys represent a critical security gap if they have not already been removed or changed. Therefore, our client's administrator must review this information before we proceed.



### Infrastructure Enumeration

During the infrastructure enumeration, we try to overview the company's position on the internet and intranet. For this, we use OSINT and the first active scans.

We use services such as DNS to create a map of the client's servers and hosts and develop an understanding of how their `infrastructure` is structured. This includes name servers, mail servers, web servers, cloud instances, and more.

In this phase, we also try to determine the company's security measures. The more precise this information is, the easier it will be to disguise our attacks (`Evasive Testing`). But identifying firewalls, such as web application firewalls, also gives us an excellent understanding of what techniques could trigger an alarm for our customer and what methods can be used to avoid that alarm.

Here, it also does not matter "where" we are positioned, whether we are trying to gain an overview of the infrastructure from the outside (`external`) or examining the infrastructure from the inside (`internal`) of the network. Enumeration from inside the network gives us a good overview of the hosts and servers that we can use as targets for a `Password Spraying` attack, in which we use one password to attempt to authenticate with as many different user names as possible, hoping for one successful authentication attempt to grant us a foothold in the network. All these methods and techniques used for this purpose will be looked at in more detail in the individual modules.



### Service Enumeration

In service enumeration, we identify services that allow us to interact with the host or server over the network (or locally, from an internal perspective). Therefore, it is crucial to find out about the service, what `version` it is, what `information` it provides us, and the `reason` it can be used.

Many services have a version history that allows us to identify whether the installed version on the host or server is actually up to date or not. This will also help us find security vulnerabilities that remain with older versions in most cases. Many administrators are afraid to change applications that work, as it could harm the entire infrastructure.



### Host Enumeration

Once we have a detailed list of the customer's infrastructure, we examine every single host listed in the scoping document. We try to identify which `operating system` is running on the host or server, which `services` it uses, which `versions` of the services, and much more.

Again, apart from the active scans, we can also use various OSINT methods to tell us how this host or server may be configured.

It does not matter here whether we examine each host or server externally or internally. However, from the internal perspective, we will find services that are often not accessible from the outside. Therefore, many administrators become careless and often consider these services "secure" because they are not directly accessible from the internet. Thus, many misconfigurations are often discovered here due to these assumptions or lax practices.

During host enumeration, we try to determine what role this host or server plays and what network components it communicates with. In addition, we must also identify which `services` it uses for this purpose and on which `ports` they are located.

During internal host enumeration, which in most cases comes after the successful `Exploitation` of one or more vulnerabilities, we also examine the host or server from the inside. This means we look for sensitive `files`, local `services`, `scripts`, `applications`, `information`, and other things that could be stored on the host. This is also an essential part of the `Post-Exploitation` phase, where we try to exploit and elevate privileges.



### Pillaging

After hitting the `Post-Exploitation` stage, pillaging is performed to collect sensitive information locally on the already exploited host, such as employee names, customer data, and much more. However, this information gathering only occurs after exploiting the target host and gaining access to it.

Pillaging alone is not a stage or a subcategory as many often describe but an integral part of the information gathering and privilege escalation stages that is inevitably performed locally on target systems.















