# Security Auditing & Penetration Testing

## Security Auditing vs. Penetration Testing

<figure><img src="../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

## Sequential Approach

* <mark style="color:blue;">Perform Security Audit First</mark>: Companies often conduct a security audit first to evaluate their overall security posture, ensure compliance with regulations, and identify areas for improvement in policies and procedures.
* <mark style="color:blue;">Conduct Penetration Test Afterwards</mark>: Based on the findings of the audit, a penetration test may be performed to assess the effectiveness fo technical controls and identify specific vulnerabilities.

### Advantages

* Provides a comprehensive view of security from both policy and technical perspectives.
* Identifies and addresses gaps in both procedural and technical controls.
* Helps prioritize remediation efforts based on audit findings.

## Combines Approach

* <mark style="color:blue;">Integrate Security Audit and Penetration Testing</mark>: Some organizations choose to combine security audits and penetration tests, often through a holistic security assessment that incorporates both elements.

### Advantages

* Streamlines the assessment process by combining policy, procedural, and technical evaluations.
* Provides a more complete picture of the organization's security posture in a single engagement.
* Can be more efficient and cost-effective by addressing both compliance and technical vulnerabilities simultaneously.

## Example: Sequential Approach

* Consider a fictional organization, "SecurePayments Inc.," which processes credit card transactions and must adhere to PCI DSS standards.&#x20;
* In this example, “SecurePayments Inc.” is using a sequential approach to assess their overall security posture. The organization has already performed a security audit through an independent audit firm and are using the findings in the audit report as the basis of their remediation plan/efforts.&#x20;
* As part of their remediation plan, the organization has decided to hire you (or your firm) to perform a penetration test with a focus on ensuring PCI DSS compliance.
* The external audit performed by the independent audit firm outlined the following findings:&#x20;
  * Inadequate encryption for cardholder data in transit.&#x20;
  * Weak/inadequate network security controls and traffic monitoring.&#x20;
  * Weak access control policies that allow excessive permissions.&#x20;
  * Outdated incident response procedures&#x20;
* The corresponding recommendations for the findings outlined above are:&#x20;
  * Implement strong encryption protocols for data in transit. ○&#x20;
  * Revise access control policies to follow the principle of least privilege.&#x20;
  * Update and test incident response procedures regularly. The company followed the Security Audit lifecycle/process outlined in the “Security Auditing Process/Lifecycle video and made the necessary improvements based on the recommendations.

#### Objectives:&#x20;

* After making the necessary changes/improvements based on the findings and recommendations in the external audit report, "SecurePayments Inc.," has hired you to test the technical controls and security measures implemented based on audit findings to verify whether they are effective.

### Phase 1: Planning and Preparation:&#x20;

During the initial phase, you identify that the PCI DSS scope includes the cardholder data environment (CDE). You review SecurePayments Inc.’s network diagrams and PCI DSS self-assessment questionnaires to understand their current security measures and compliance status.&#x20;

#### Objectives:&#x20;

* Define the scope of the penetration test to focus on the areas identified in the audit, such as network security and application vulnerabilities.&#x20;
* Set up a testing schedule and inform stakeholders.

### Phase 2: Information Gathering and Reconnaissance:&#x20;

* You gather information on SecurePayments Inc.'s security policies, such as their access control policies, encryption standards, and incident response procedures.&#x20;
* You also review their most recent PCI DSS audit report to identify areas of concern highlighted by auditors. Example: Sequential Approach

### Phase 3: Penetration Test Execution:&#x20;

* Conduct network scanning, enumeration and vulnerability assessments to identify weaknesses, misconfigurations or vulnerabilities.&#x20;
* Attempt exploitation of identified vulnerabilities to assess their impact.&#x20;
* Test the effectiveness of newly implemented encryption and access controls.

Phase 4: Findings and Recommendations:&#x20;

* Outcome: The penetration test uncovers additional vulnerabilities:&#x20;
  * An exposed administrative interface that allows unauthorized access.&#x20;
  * SQL injection vulnerabilities in a customer-facing web application.&#x20;
* Recommendations:&#x20;
  * Secure the administrative interface by implementing additional authentication and access controls.&#x20;
  * Patch the SQL injection vulnerabilities and conduct a thorough review of application security.
* Security Audit Results:&#x20;
  * Identified compliance gaps and policy deficiencies.&#x20;
  * Provided recommendations for improving security policies and procedures.&#x20;
* Penetration Testing Results:&#x20;
  * Revealed specific technical vulnerabilities.&#x20;
  * Offered targeted recommendations to address these technical weaknesses.







































