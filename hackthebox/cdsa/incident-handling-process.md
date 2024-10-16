# Incident Handling Process

### Incident Handling Definition & Scope

\
While protective measures are constantly being implemented to prevent or lower the amount of security incidents, an incident handling capability is undeniably a necessity for any organization that cannot afford a compromise of its data confidentiality, integrity, or availability.\


An `event` is an action occurring in a system or network. Examples of events are:

* A user sending an email
* A mouse click
* A firewall allowing a connection request

An `incident` is an event with a negative consequence. One example of an incident is a system crash.

We define an IT security incident as an event with a clear intent to cause harm that is performed against a computer system. Examples of incidents are:

* Data theft
* Funds theft
* Unauthorized access to data
* Installation and usage of malware and remote access tools

### Incident Handling's Value & Generic Notes

One of the most widely used resources on incident handling is [NIST's Computer Security Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf). The document aims to assist organizations in mitigating the risks from computer security incidents by providing practical guidelines on responding to incidents effectively and efficiently.



## Cyber Kill Chain

### What Is The Cyber Kill Chain?

The cyber kill chain consists of seven (7) different stages, as depicted in the image below:

<figure><img src="../../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>

### Recon Stage

* **Target Selection**: Attacker chooses the target.
* **Information Gathering**:
  * Passive: Uses web sources like LinkedIn, Instagram, company websites.
  * Sources: Job ads, company partners reveal technologies used (e.g., antivirus, OS, networking).
  * Active: Scans external web applications and IP addresses.

### Weaponization Stage

* **Malware Development**:
  * Craft lightweight, undetectable malware.
  * Embed malware into an exploit or deliverable payload.
* **Objective**:
  * Provide remote access to the compromised machine.
  * Ensure persistence through reboots.
  * Enable deployment of additional tools.

### Delivery Stage

* **Payload Delivery Methods**:
  * **Phishing Emails**: Contain malicious attachments or links to exploit-hosting web pages.
  * **Web Pages**: Mimic legitimate sites to collect credentials or host payloads.
  * **Social Engineering**: Convince victims to execute the payload.
  * **Physical Interaction**: Use USB tokens or similar tools for payload delivery.

### Exploitation Stage

* **Triggering Exploit**:
  * Payload or exploit is triggered to execute code on the target system.
  * Goal: Gain access or control.

### Installation Stage

* **Executing Initial Stager**:
  * **Droppers**: Deliver and execute malware.
  * **Backdoors**: Provide ongoing access to the compromised system.
  * **Rootkits**: Hide presence and evade detection.

### Command and Control Stage

* **Establish Remote Access**:
  * Use modular stagers to load additional scripts.
  * Deploy separate tools to ensure persistence in the compromised network.

### Action/Objective Stage

* **Attack Objectives**:
  * Data exfiltration.
  * Gaining highest-level access to deploy ransomware.
  * Ransomware: Encrypts data, demanding ransom for decryption.

### Key Points

* **Non-linear Progression**:
  * Stages can be repeated (e.g., recon stage after a successful compromise).
  * Adversaries may reinitiate recon to find additional vulnerabilities.
* **Defense Goal**: Stop attackers early in the kill chain.

## Incident Handling Process Overview

### 1. Preparation

* **Objective**: Prepare for potential incidents by establishing capabilities and resources.
* **Activities**:
  * Develop incident response plans and policies.
  * Train staff and establish communication channels.
  * Implement preventive measures and tools.

### 2. Detection & Analysis

* **Objective**: Identify and analyze potential security incidents.
* **Activities**:
  * Monitor systems and networks for signs of malicious activity.
  * Analyze alerts and logs to confirm incidents.
  * Classify the incident type and determine the scope.

### 3. Containment, Eradication, & Recovery

* **Objective**: Control the impact of the incident, remove the threat, and restore normal operations.
* **Containment**:
  * Isolate affected systems to prevent further damage.
  * Implement short-term and long-term containment strategies.
* **Eradication**:
  * Identify and remove malware or compromised components.
  * Patch vulnerabilities and close security gaps.
* **Recovery**:
  * Develop and execute a recovery plan.
  * Restore systems and data to a secure state.
  * Monitor for signs of continued compromise.

### 4. Post-Incident Activity

* **Objective**: Learn from the incident and improve future responses.
* **Activities**:
  * Issue a detailed incident report (cause, impact, and cost).
  * Conduct "lessons learned" sessions to identify improvement areas.
  * Update incident response plans and preventive measures.

### Key Points

* **Cyclic Process**: Incident handling is not linear; new evidence can alter next steps.
* **Complete Each Step**: Avoid skipping steps to ensure thorough incident resolution.
* **Investigation**:
  * Identify the initial compromise ("patient zero").
  * Document tools, malware, and affected systems.
* **Recovery**:
  * Implement a recovery plan to resume normal operations.
  * Ensure no infected systems are left unaddressed.

## Preparation Stage in Incident Handling Stage 1

### Objectives

1. **Establish Incident Handling Capability**:
   * Build and maintain a skilled incident handling team.
   * Develop clear policies and documentation.
   * Equip the team with necessary tools and resources.
2. **Protect Against and Prevent IT Security Incidents**:
   * Implement protective measures (e.g., endpoint hardening, MFA, privileged access management).
   * Note: While protection isn't the incident handling team's responsibility, it is crucial for their success.

### Preparation Prerequisites

* **Skilled Incident Handling Team**:
  * Ensure in-house capability, even if outsourcing is involved.
* **Trained Workforce**:
  * Conduct security awareness training and other relevant educational activities.
* **Clear Policies & Documentation**:
  * Maintain up-to-date contact information for all relevant teams and external parties.
  * Develop and regularly update incident response policies, plans, and procedures.
  * Keep baselines, network diagrams, and asset management databases current.
  * Prepare on-demand user accounts with excessive privileges for incident response.
  * Establish procedures for quick procurement of tools and resources.
  * Create forensic/investigative cheat sheets for quick reference.

### Documentation Essentials

* **Contact Information**:
  * Incident handling team, legal/compliance, IT support, media relations, law enforcement, ISPs, facility management.
* **Incident Response Policy & Procedures**:
  * Incident response policy, plan, information sharing procedures.
* **System & Network Baselines**:
  * Golden images, clean state environment baselines, network diagrams.
* **Asset Management Database**:
  * Organization-wide asset tracking.
* **User Accounts**:
  * Privileged accounts enabled during incidents, disabled afterward with mandatory password resets.
* **Quick Procurement**:
  * Ability to acquire resources without delays (urgent purchases).
* **Forensic/Investigative Cheat Sheets**:
  * Ready-to-use guidelines for various incident types.

### Tools (Software & Hardware)

* **Forensic Workstations**:
  * Laptops or forensic workstations for each team member (for disk imaging, log analysis, etc.).
* **Digital Forensic Tools**:
  * Tools for image acquisition, memory capture, live response, and log analysis.
* **Network Tools**:
  * Network capture and analysis tools, cables, switches.
* **Hardware Tools**:
  * Write blockers, hard drives, power cables, screwdrivers, and other repair tools.
* **Indicator of Compromise (IOC) Tools**:
  * Ability to create and search for IOCs across the organization.
* **Chain of Custody Forms**:
  * Forms for tracking evidence handling.
* **Encryption Software**:
  * For securing data and communications.
* **Ticket Tracking System**:
  * System for tracking incident response activities.
* **Secure Facility**:
  * Independent, secure location for storage and investigation.
* **Jump Bag**:
  * A pre-packed bag with all necessary tools for immediate response.

### Communication & Documentation Independence

* **Independent Documentation System**:
  * Ensure the incident handling documentation system is separate from the organization’s infrastructure.
  * Assume the organization's domain could be compromised.
* **Secure Communication Channels**:
  * Use communication channels outside of the organization’s systems for discussing incidents.
  * Avoid using internal email or other compromised channels for incident-related communications.

## Protective Measures in the Preparation Stage

### Overview

* **Protection-related Activities**: Though not the primary responsibility of the incident handling team, understanding protective measures aids in investigating incidents and identifying artifacts/evidence.\


## Stage 2

### Recommended Protective Measures

#### DMARC (Domain-based Message Authentication, Reporting, and Conformance)

* **Purpose**: Protects against email phishing by rejecting spoofed emails pretending to originate from your organization.
* **Implementation**: Built on SPF and DKIM; requires thorough testing to avoid blocking legitimate emails.
* **Advanced Protection**: Implement email filtering rules to reject emails failing DMARC from domains you don't own.

#### Endpoint Hardening & Endpoint Detection and Response (EDR)

* **Importance**: Most attacks originate from endpoint devices.
* **Standards**: Follow CIS and Microsoft baselines.
* **Key Actions**:
  * Disable LLMNR/NetBIOS.
  * Implement LAPS and remove admin privileges from regular users.
  * Configure PowerShell in "ConstrainedLanguage" mode.
  * Enable Attack Surface Reduction (ASR) rules with Microsoft Defender.
  * Implement application whitelisting, especially in user-writable folders.
  * Utilize host-based firewalls (e.g., block workstation-to-workstation communication).
  * Deploy an EDR product, preferably one that integrates with AMSI for script analysis.

#### Network Protection

* **Network Segmentation**: Isolate business-critical systems; allow connections only as required by the business.
* **IDS/IPS Systems**: Optimize effectiveness with SSL/TLS interception.
* **Access Control**:
  * Use 802.1x to control network access and reduce BYOD risks.
  * For cloud environments (e.g., Azure AD), use Conditional Access policies for device management.

#### Privilege Identity Management / MFA / Passwords

* **Password Hygiene**:
  * Avoid weak but complex passwords (e.g., "Password1!").
  * Promote the use of pass phrases (e.g., "i LIK3 my coffeE warm").
  * Use multi-language phrases for added security.
* **Multi-Factor Authentication (MFA)**:
  * Implement MFA for all administrative access across applications and devices.

#### Vulnerability Scanning

* **Continuous Scanning**: Regularly scan the environment for vulnerabilities.
* **Remediation**: Prioritize fixing "high" and "critical" vulnerabilities.
* **Segmentation**: Isolate unpatched systems to mitigate risk.

#### User Awareness Training

* **Purpose**: Educate users to recognize and report suspicious activities.
* **Training Methods**:
  * Conduct periodic training sessions.
  * Implement surprise tests (e.g., phishing emails, USB drop tests).

#### Active Directory Security Assessment

* **Importance**: Identify security misconfigurations and critical vulnerabilities.
* **Approach**:
  * Conduct regular assessments from an attacker's perspective.
  * Hire third-party experts if internal skills are lacking.
* **Focus Areas**:
  * Address unique AD escalation paths and newly discovered bugs.
  * Eliminate low-hanging fruits to make it harder for attackers to escalate privileges.

#### Purple Team Exercises

* **Purpose**: Train and engage incident handlers in the organization's environment.
* **Exercise Structure**:
  * Red team conducts assessments and shares findings with the blue team.
  * Evaluate the blue team's logging, monitoring, detection, and responsiveness.
  * Use these exercises to improve incident handling procedures and playbooks.

## Detection and Analysis Stage (Part 1)

### Overview

* **Focus**: Detecting incidents using sensors, logs, trained personnel, and context-based threat intelligence.
* **Key Components**:
  * Information and knowledge sharing.
  * Network segmentation and visibility.

### Sources of Incident Detection

* Employee reports of abnormal behavior.
* Alerts from tools (EDR, IDS, Firewall, SIEM, etc.).
* Threat hunting activities.
* Third-party notifications of compromise.

### Levels of Detection

1. **Network Perimeter**:
   * Tools: Firewalls, internet-facing IDS/IPS, DMZ, etc.
2. **Internal Network**:
   * Tools: Local firewalls, host-based IDS/IPS.
3. **Endpoint Level**:
   * Tools: Antivirus, EDR systems.
4. **Application Level**:
   * Tools: Application logs, service logs.

### Initial Investigation

* **Purpose**: Gather context before assembling the incident response team.
* **Key Information to Collect**:
  * Date/Time of incident report.
  * How the incident was detected.
  * Type of incident (e.g., phishing, system unavailability).
  * List of impacted systems (if relevant).
  * Documentation of who accessed impacted systems and actions taken.
  * Physical location, OS, IP addresses, hostnames, system owner, and current state.
  * (If malware involved) IP addresses, detection details, malware type, impacted systems, forensic data (hashes, file copies, etc.).

### Building an Incident Timeline

* **Purpose**: Organize events in chronological order to provide a clear overview of the incident.
* **Timeline Structure**:
  * **Columns**: Date, Time of event, Hostname, Event description, Data source.
  * **Focus**: Attacker behavior and system interactions.

#### Example Timeline Entry

* **Date**: 09/09/2021
* **Time of Event**: 13:31 CET
* **Hostname**: SQLServer01
* **Event Description**: Hacker tool 'Mimikatz' detected.
* **Data Source**: Antivirus Software

### Assessing Incident Severity & Extent

* **Questions to Consider**:
  * What is the exploitation impact?
  * What are the exploitation requirements?
  * Are business-critical systems affected?
  * What are the suggested remediation steps?
  * How many systems are impacted?
  * Is the exploit used in the wild?
  * Does the exploit have worm-like capabilities?
* **Outcome**: Determine incident severity and escalate as needed.

### Incident Confidentiality & Communication

* **Confidentiality**:
  * Restrict information on a need-to-know basis.
  * Consider the possibility of internal threats.
  * Handle internal and external communications per legal guidance.
* **Setting Expectations**:
  * Define goals, evidence sources, and timeframes for the investigation.
  * Keep stakeholders informed of progress and changes.



## Detection and Analysis Stage (Part 2)

### Purpose of the Investigation

* **Objective**: Understand what happened and how it happened.
* **Importance**:
  * Prevent attackers from repeating their actions.
  * Ensure thorough remediation by understanding the attack path.

### Investigation Process

* **Initial Data**: Investigation starts with limited information.
* **3-Step Cyclic Process**:
  1. **Creation & Usage of Indicators of Compromise (IOC)**.
  2. **Identification of New Leads & Impacted Systems**.
  3. **Data Collection & Analysis from New Leads & Impacted Systems**.

### Initial Investigation Data

* **Ongoing Discovery**:
  * New leads should be constantly identified throughout the investigation.
  * Avoid narrowing the investigation too early to ensure comprehensive findings.

### Creation & Usage of IOCs

* **Definition**: IOCs are signs of an incident, representing artifacts of the compromise (e.g., IP addresses, hash values, file names).
* **IOC Standards**:
  * **OpenIOC**: Structured language for documenting IOCs.
  * **Yara**: Widely used for defining and sharing IOCs.
  * **Tools**: Mandiant's IOC Editor, WMI, PowerShell (caution with credential caching).
* **Best Practices**:
  * Avoid using tools that cache credentials (e.g., careful use of PsExec).
  * Utilize tools that don't cache credentials (e.g., WinRM).

### Identification of New Leads & Impacted Systems

* **IOC Search Results**:
  * May reveal new systems showing signs of compromise.
  * Important to filter out false positives and prioritize relevant leads.

### Data Collection & Analysis from New Leads & Impacted Systems

* **Collection Approach**:
  * **Live Response**: Most common, collecting data while the system is running.
  * **Shutdown & Analysis**: Used cautiously, as it may lead to loss of volatile data in RAM.
* **Data Analysis**:
  * **Types**: Malware analysis, disk forensics, memory forensics.
  * **Timeline Update**: Constantly add new validated leads to the incident timeline.
* **Chain of Custody**:
  * Maintain to ensure data is court-admissible if legal action is pursued.

### Summary

* **Ongoing Process**: The investigation evolves as new data is collected and analyzed.
* **Objective**: Fully understand the incident to prevent recurrence and ensure comprehensive remediation.

## Containment, Eradication, & Recovery Stage

### Containment

#### Objective

* **Purpose**: Prevent the incident from causing further damage.
* **Types**:
  1. **Short-Term Containment**:
     * Minimal impact on systems.
     * Examples:
       * Isolating systems in a separate VLAN.
       * Disconnecting network cables.
       * Redirecting attacker's C2 DNS.
     * **Goal**: Contain damage while preserving evidence for forensic analysis.
     * **Communication**: Obtain business approval if shutting down systems is required.
  2. **Long-Term Containment**:
     * Persistent actions and system changes.
     * Examples:
       * Changing passwords.
       * Applying firewall rules.
       * Installing host intrusion detection systems.
       * Patching systems.
     * **Goal**: Ensure long-term stability while keeping stakeholders informed.
     * **Note**: Incident is not considered over at this stage.

### Eradication

#### Objective

* **Purpose**: Eliminate the root cause of the incident and any remaining traces of it.
* **Actions**:
  * Remove malware from systems.
  * Rebuild compromised systems.
  * Restore systems from backups.
  * Apply additional patches.
  * Perform system-hardening activities across the network.

### Recovery

#### Objective

* **Purpose**: Restore systems to normal operation and ensure they function as expected.
* **Process**:
  * Verify that restored systems are fully operational.
  * Reintroduce systems into the production environment.
  * Implement heavy logging and monitoring.
    * Monitor for:
      * Unusual logons.
      * Unusual processes.
      * Registry changes typically associated with malware.
  * **Phased Approach**:
    * Early Phases: Focus on quick wins and addressing immediate vulnerabilities.
    * Later Phases: Implement long-term changes to enhance overall security.
  * **Duration**: Recovery may take months, depending on the incident's scale.



## Post-Incident Activity Stage

### Objective

* **Purpose**: Document the incident, learn from it, and improve future incident response capabilities.
* **Goal**: Reflect on the incident, understand what occurred, evaluate actions taken, and enhance processes.

### Incident Review Meeting

#### Timing

* Held within a few days after the incident.
* Occurs after the final incident report is completed.

#### Participants

* All stakeholders involved during the incident.

#### Focus

* **Reflection**:
  * What occurred during the incident?
  * What actions were taken?
  * How effective were the actions?

### Reporting

#### Importance

* **Purpose**: A final report is a critical part of the incident response process.
* **Content**:
  * **Incident Summary**:
    * What happened and when?
  * **Team Performance**:
    * How well did the team follow plans, playbooks, policies, and procedures?
  * **Business Response**:
    * Did the business provide necessary information and respond promptly?
    * What improvements can be made?
  * **Incident Actions**:
    * What actions were taken to contain and eradicate the incident?
  * **Preventive Measures**:
    * What measures should be implemented to prevent future incidents?
  * **Tools and Resources**:
    * What tools and resources are needed to detect and analyze similar incidents in the future?

#### Benefits

* Provides measurable results:
  * Number of incidents handled.
  * Time spent per incident.
  * Actions performed during incident handling.
* Serves as a reference for handling similar future incidents.
* Used in legal proceedings to identify costs and impacts of incidents.

#### Training

* **New Team Members**:
  * Use the incident report as a training tool to show how experienced colleagues handled the incident.

#### Continuous Improvement

* **Evaluation**:
  * Assess if plans, playbooks, policies, and procedures need updating.
* **Reevaluation**:
  * Focus on tools, training, and readiness of the team.
  * Consider the overall team structure and not just documentation and processes.

#### Next Steps

* Further exploration of the reporting part of the Incident Handling Process in the Security Incident Reporting module.

























































































