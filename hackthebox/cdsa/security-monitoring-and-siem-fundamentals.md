# Security Monitoring & SIEM Fundamentals

## What Is SIEM?

### Overview

* **Definition**: Security Information and Event Management (SIEM) involves software tools and solutions that combine security data management with security event monitoring.
* **Functions**:
  * Real-time evaluation of security alerts from network hardware and applications.
  * Core features include log event collection, management, analysis, incident handling, visual summaries, and documentation.

### Importance

* **Detection & Response**:
  * Enables IT teams to detect cyberattacks in real-time or even before they occur.
  * Enhances the speed and effectiveness of incident response.
* **Role in Security**: SIEM is fundamental to an organization's security strategy, offering a comprehensive approach to threat detection and management.

## Evolution of SIEM Technology

### Origin

* **Concept**: SIEM emerged from combining two technologies—Security Information Management (SIM) and Security Event Management (SEM)—as proposed by Gartner analysts in 2005.

### Generations

* **First-Generation SIM**:
  * Built on traditional log collection management systems.
  * Enabled extended storage, examination, and reporting of log data.
* **Second-Generation SEM**:
  * Focused on security events by consolidating, correlating, and notifying events from various security devices.

### Development

* **Integration**: Vendors combined SIM and SEM capabilities to create SIEM, offering a holistic approach to threat detection and management.

## How Does a SIEM Solution Work?

### Data Collection

* **Sources**: Gathers data from PCs, network devices, servers, etc.
* **Standardization**: Data is standardized and consolidated for easier analysis.

### Threat Detection

* **Role of Analysts**: Security experts analyze the data to identify potential threats.
* **Alerts**: Alerts notify Security Operations/Monitoring personnel of possible security incidents.
  * Alerts are concise and can be delivered via emails, console pop-ups, text messages, or phone calls.

### Fine-Tuning

* **Volume of Alerts**: SIEM systems generate numerous alerts; fine-tuning is essential to focus on high-risk events.
* **Differentiation**: SIEM stands out by accurately identifying high-risk events, unlike other network monitoring tools.

## SIEM Business Requirements & Use Cases

### Log Aggregation & Normalization

* **Threat Visibility**: Log consolidation is critical for threat visibility.
  * **Function**: Gathers and examines security data, allowing SOC teams to identify and analyze security incidents across IT infrastructure.

### Threat Alerting

* **Identification**: SIEM solutions detect potential threats within the vast volume of event data.
* **Timely Response**: Real-time alerts enable IT security teams to investigate and mitigate risks promptly.

### Contextualization & Response

* **Importance**: Contextualization is crucial for filtering alerts, identifying genuine threats, and enabling swift action.
* **Automation**: Automated processes filter contextualized threats, reducing alert fatigue.

### Compliance

* **Role in Compliance**: Helps organizations meet regulatory requirements (e.g., PCI DSS, HIPAA, GDPR).
* **Reporting & Auditing**: Provides automated reporting and auditing capabilities essential for compliance.

## Data Flows Within a SIEM

### Data Ingestion

* **Collection**: SIEM tools collect logs from various data sources (data ingestion).
* **Normalization**: Raw data is processed and normalized to be understood by the SIEM correlation engine.

### Analysis

* **SOC Team Role**: SOC teams use normalized data to create detection rules, dashboards, alerts, and incidents.

## Benefits of Using a SIEM Solution

### Centralized Monitoring

* **Advantage**: A properly calibrated SIEM enhances incident response and offers a centralized dashboard for notifications.
* **Example**: Correlating logs from various sources to monitor and respond to security incidents effectively.

### Advanced Capabilities

* **Built-in Intelligence**: Modern SIEMs include intelligence for detecting threshold limits and events within timeframes.
* **AI Integration**: Advanced SIEMs use AI for behavioral and pattern analysis.

### Compliance and Reporting

* **Mandates**: Many regulated industries (e.g., Banking, Healthcare) require managed SIEM systems for compliance.
* **Evidence**: SIEM systems provide evidence of monitoring, logging, and adherence to retention policies, fulfilling standards like ISO and HIPAA.



## Introduction to the Elastic Stack

<figure><img src="../../.gitbook/assets/image (243).png" alt=""><figcaption></figcaption></figure>

#### The Elastic Stack Overview

* **Elastic Stack**: An open-source collection created by Elastic, comprising three primary applications:
  * **Elasticsearch**
  * **Logstash**
  * **Kibana**
* **Purpose**: Provides comprehensive search and visualization capabilities for real-time log file analysis.

#### High-Level Architecture

* **Core Components**:
  * **Elasticsearch**: Distributed, JSON-based search engine with RESTful APIs. Handles indexing, storing, and querying of data.
  * **Logstash**: Collects, transforms, and transports log file records. Works in three main areas:
    * **Process Input**: Ingests log records from various sources.
    * **Transform & Enrich**: Modifies log record format/content using filter plugins.
    * **Send to Elasticsearch**: Transmits processed records to Elasticsearch.
  * **Kibana**: Visualization tool for Elasticsearch documents. Allows users to view, query, and visualize data with tables, charts, and dashboards.

#### Additional Components

* **Beats**: Lightweight, single-purpose data shippers installed on remote machines to forward logs and metrics to Logstash or Elasticsearch.

#### Integration Example

* **Data Flow**:
  * **Beats -> Logstash -> Elasticsearch -> Kibana**
  * **Beats -> Logstash**
  * **Beats -> Elasticsearch -> Kibana**
  * **Beats -> Elasticsearch**

#### Elastic Stack as a SIEM Solution

* **Functionality**: Collects, stores, analyzes, and visualizes security-related data from various sources (firewalls, IDS/IPS, endpoints).
* **Implementation**:
  * Use Logstash to ingest security data.
  * Store and index data in Elasticsearch.
  * Use Kibana for creating custom dashboards and visualizations.
  * Perform searches and correlations in Elasticsearch to detect security incidents.

#### Kibana Query Language (KQL)

* **Purpose**: Simplifies searching and analyzing data in Kibana.
* **Key Components**:
  * **Basic Structure**: Queries are composed of `field:value` pairs.
    * Example: `event.code:4625` (Filters data to show events with Windows event code 4625, related to failed login attempts).
  * **Free Text Search**: Allows searching for specific terms across multiple fields.
  * **Logical Operators**: Supports AND, OR, and NOT for complex queries.
    * Example: `event.code:4625 AND winlog.event_data.SubStatus:0xC0000072` (Filters events with specific event code and SubStatus).
  * **Comparison Operators**: Supports various comparison operators (e.g., `:`, `:>`, `:>=`).
  * **Wildcards & Regular Expressions**: Used for pattern matching in field values.

#### Identifying Available Data

* **Methods**:
  * **KQL Free Text Search**: Use the Discover feature in Kibana to explore and identify available fields and values.
  * **Elastic Documentation**: Familiarize yourself with ECS, Winlogbeat fields, and other relevant documentation.

#### Elastic Common Schema (ECS)

* **Purpose**: Provides a shared and extensible vocabulary for events/logs across the Elastic Stack.
* **Advantages**:
  * **Unified Data View**: Standardizes field names for consistent data views.
  * **Improved Search Efficiency**: Simplifies query writing in KQL.
  * **Enhanced Correlation**: Facilitates easier event correlation across data sources.
  * **Better Visualizations**: Supports consistent and effective visualizations in Kibana.
  * **Interoperability**: Ensures compatibility with Elastic Stack features (e.g., Elastic Security, Elastic Observability).
  * **Future-proofing**: Adopting ECS ensures compatibility with future Elastic Stack enhancements.

## SOC Definition & Fundamentals

#### What Is A SOC?

* **Security Operations Center (SOC)**: A facility that houses a team of information security experts focused on continuous monitoring and assessment of an organization's security status.
* **Main Objective**: Identify, examine, and address cybersecurity incidents using a mix of technology solutions and established procedures.
* **Team Composition**:
  * **Security Analysts**
  * **Engineers**
  * **Managers**
* **Collaboration**: SOC teams work closely with incident response teams to ensure prompt detection and resolution of security concerns.

#### SOC Technology Solutions

* **Tools Utilized**:
  * **Security Information and Event Management (SIEM) systems**
  * **Intrusion Detection and Prevention Systems (IDS/IPS)**
  * **Endpoint Detection and Response (EDR) tools**
  * **Threat Intelligence** and **Threat Hunting** initiatives

#### SOC Processes

* **Incident Handling Processes**:
  * **Incident Triage**
  * **Containment**
  * **Elimination**
  * **Recovery**
* **Collaboration**: SOC teams work with incident response teams to maintain the organization’s security posture.

#### How Does A SOC Work?

* **Primary Function**: Focuses on the ongoing operational aspect of enterprise information security, rather than strategy development, architecture design, or protective measure implementation.
* **Main Tasks**:
  * Detect, assess, respond to, report on, and prevent cybersecurity incidents.
  * Some SOCs may have advanced capabilities like forensic analysis and malware analysis for in-depth investigations.

#### Roles Within A SOC

* **SOC Team Roles**:
  * **SOC Director**: Oversees management, strategic planning, budgeting, and alignment with security objectives.
  * **SOC Manager**: Manages daily operations, coordinates incident response, and ensures collaboration with other departments.
  * **Tier 1 Analyst**: Monitors security alerts, performs initial triage, and escalates incidents to higher tiers.
  * **Tier 2 Analyst**: Conducts in-depth analysis of escalated incidents, identifies trends, and develops mitigation strategies.
  * **Tier 3 Analyst**: Handles complex incidents, engages in threat hunting, and collaborates on improving security posture.
  * **Detection Engineer**: Develops and maintains detection rules for SIEM, IDS/IPS, and EDR tools.
  * **Incident Responder**: Leads active incident response, conducts forensics, and collaborates on system recovery.
  * **Threat Intelligence Analyst**: Gathers and analyzes threat intelligence to inform proactive defense measures.
  * **Security Engineer**: Develops and maintains security tools and infrastructure, providing technical support to the SOC team.
  * **Compliance and Governance Specialist**: Ensures adherence to industry standards, regulations, and assists with audits.
  * **Security Awareness and Training Coordinator**: Develops and implements cybersecurity training and awareness programs.

#### SOC Tier Structure

* **Tier 1 Analysts**: "First responders" who monitor events, perform triage, and escalate incidents.
* **Tier 2 Analysts**: More experienced analysts who perform deeper analysis and develop mitigation strategies.
* **Tier 3 Analysts**: Handle the most complex incidents, engage in threat hunting, and improve security posture.

#### SOC Stages of Evolution

* **SOC 1.0**:
  * Early focus on network and perimeter security.
  * Characterized by uncorrelated alerts and tasks spread across multiple platforms.
  * Some organizations still rely on this outdated approach.
* **SOC 2.0**:
  * Response to sophisticated threats, such as multi-vector, persistent, and asynchronous attacks.
  * Focus on integrating security telemetry, threat intelligence, and anomaly detection.
  * Employs layer-7 analysis, threat research, and collaboration for situational awareness.
  * Emphasizes vulnerability management, incident response, and refining security intelligence.
* **Cognitive SOC (Next-Generation SOC)**:
  * Aims to address SOC 2.0 shortcomings by incorporating learning systems.
  * Enhances collaboration between business and security teams.
  * Focuses on standardizing incident response and recovery procedures.

## MITRE ATT\&CK & Security Operations

### What Is MITRE ATT\&CK?

* **MITRE ATT\&CK (Adversarial Tactics, Techniques, and Common Knowledge)**: A comprehensive, regularly updated resource that outlines the tactics, techniques, and procedures (TTPs) used by cyber threat actors.
* **Purpose**: Helps cybersecurity professionals understand, identify, and respond to threats more effectively.
* **Framework Structure**:
  * **Matrices**: Tailored to various computing contexts (e.g., enterprise, mobile, cloud).
  * **Tactics**: Goals that attackers aim to achieve.
  * **Techniques**: Methods used to accomplish those goals.
  * **TTPs**: Link between tactics and techniques, enabling methodical examination and prediction of attacker activities.

### MITRE ATT\&CK Use Cases in Security Operations

* **Detection and Response**:
  * Supports the development of detection and response plans based on recognized attacker TTPs.
  * Enables security teams to identify potential threats and create proactive countermeasures.
* **Security Evaluation and Gap Analysis**:
  * Helps organizations identify strengths and weaknesses in their security posture.
  * Prioritizes security control investments to defend effectively against relevant threats.
* **SOC Maturity Assessment**:
  * Measures an organization's ability to detect, respond to, and mitigate various TTPs.
  * Assists in identifying areas for improvement and resource prioritization to strengthen overall security.
* **Threat Intelligence**:
  * Provides a unified language and format to describe adversarial actions.
  * Enhances collaboration among internal teams and with external stakeholders.
* **Cyber Threat Intelligence Enrichment**:
  * Enriches cyber threat intelligence by offering context on attacker TTPs and insights into potential targets and indicators of compromise (IOCs).
  * Supports informed decision-making and effective threat mitigation strategies.
* **Behavioral Analytics Development**:
  * Maps TTPs to specific user and system behaviors, aiding in the development of behavioral analytics models.
  * Improves detection capabilities and enables proactive risk mitigation.
* **Red Teaming and Penetration Testing**:
  * Provides a systematic way to replicate genuine attacker techniques during exercises.
  * Assesses an organization's defensive capabilities.
* **Training and Education**:
  * Acts as an exceptional resource for training and educating security professionals on the latest adversarial tactics and methods.

### Conclusion

* **MITRE ATT\&CK** is an indispensable asset for security operations, offering a shared language and structure for describing and understanding adversarial behavior.
* It enhances various aspects of security operations, from threat intelligence and behavioral analytics to SOC maturity assessment and cyber threat intelligence enrichment.



## SIEM Use Case Development

#### What Is a SIEM Use Case?

A SIEM (Security Information and Event Management) use case is a specific scenario or condition defined to help identify and detect potential security incidents within an organization's network. These use cases guide the configuration and deployment of SIEM tools, enabling the monitoring, analysis, and alerting of suspicious activities based on predefined criteria.

#### Example Use Case

**Scenario:**

* A user named Rob experiences 10 consecutive failed authentication attempts. This could be due to either the user forgetting their password or a malicious actor attempting a brute force attack.

**Process:**

1. **Event Correlation:** The SIEM system aggregates these 10 failed attempts into a single event and triggers an alert under the "brute force" use case.
2. **SOC Response:** The Security Operations Center (SOC) team receives the alert and takes appropriate action based on the log data.

#### SIEM Use Case Development Lifecycle

<figure><img src="../../.gitbook/assets/image (171).png" alt=""><figcaption></figcaption></figure>

1. **Requirements:**
   * Identify the specific scenario requiring an alert (e.g., detecting a brute force attack after 10 consecutive login failures within 4 minutes).
2. **Data Points:**
   * Determine where the relevant data is generated within the network (e.g., Windows machines, Linux machines, VPN logs).
   * Ensure logs capture essential details like user ID, timestamp, source, destination, etc.
3. **Log Validation:**
   * Verify that logs contain all necessary information and are received during key events like authentication attempts.
4. **Design and Implementation:**
   * Define the conditions for triggering an alert (e.g., 10 failed login attempts within 4 minutes).
   * Consider aggregation to reduce false positives and assign priority based on the user’s role.
5. **Documentation:**
   * Create Standard Operating Procedures (SOP) that detail how to handle alerts, including escalation procedures.
6. **Onboarding:**
   * Test the alert in a development environment, identify gaps, and refine the alert before deploying it in production.
7. **Periodic Updates/Fine-Tuning:**
   * Continuously refine the use case based on feedback and operational experience to reduce false positives and improve detection accuracy.

#### Building SIEM Use Cases

1. **Understand Needs and Risks:**
   * Tailor use cases to monitor systems based on identified risks.
2. **Prioritize and Map Alerts:**
   * Assign severity levels and map alerts to frameworks like the MITRE ATT\&CK framework.
3. **Define TTD and TTR:**
   * Set metrics for Time to Detection (TTD) and Time to Response (TTR) to evaluate SIEM effectiveness.
4. **Create SOPs:**
   * Develop procedures for alert management and incident response.
5. **Refine Alerts:**
   * Continuously improve alerts based on monitoring results.
6. **Develop an Incident Response Plan (IRP):**
   * Establish a plan for handling confirmed incidents.
7. **Set SLAs and OLAs:**
   * Define agreements between teams for handling alerts and following the IRP.
8. **Implement Audit Processes:**
   * Regularly audit the management of alerts and incident reporting.

#### Practical Examples

**Example 1: MSBuild Started by an Office Application**

* **Scenario:** Monitoring for instances where MSBuild (Microsoft Build Engine) is initiated by Excel or Word, which could indicate a malicious script.
* **Risk:** High, as it may suggest an attack using Living-off-the-land binaries (LoLBins).
* **MITRE Mapping:** Defense Evasion (TA0005), Trusted Developer Utilities Proxy Execution (T1127), Execution (TA0002).
* **Response:** Analysts investigate the alert by examining process names, user activity, and system logs.

**Example 2: MSBuild Making Network Connections**

* **Scenario:** Detecting outbound connections initiated by MSBuild.exe, which might indicate adversarial activity.
* **Risk:** Medium, as the connection might be legitimate (e.g., to a Microsoft IP), but could also be a sign of an attack.
* **Response:** Analysts assess the event action, IP reputation, and other factors to determine if the connection is suspicious.

#### Conclusion

SIEM use cases are essential for tailoring the detection and response capabilities of a SIEM system to an organization’s specific security needs. They involve defining specific conditions that, when met, trigger alerts, guiding the SOC team in identifying and responding to potential security threats. The continuous development, refinement, and documentation of these use cases are crucial for maintaining an effective cybersecurity posture.

## The Triaging Process































































