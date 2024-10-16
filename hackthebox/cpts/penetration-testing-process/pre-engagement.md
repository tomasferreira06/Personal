# Pre Engagement

Pre-engagement is the stage of preparation for the actual penetration test. During this stage, many questions are asked, and some contractual agreements are made. The client informs us about what they want to be tested, and we explain in detail how to make the test as efficient as possible.



<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

The entire pre-engagement process consists of three essential components:

1. Scoping questionnaire
2. Pre-engagement meeting
3. Kick-off meeting

Before any of these can be discussed in detail, a `Non-Disclosure Agreement` (`NDA`) must be signed by all parties. There are several types of NDAs:

| **Type**           | **Description**                                                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Unilateral NDA`   | This type of NDA obligates only one party to maintain confidentiality and allows the other party to share the information received with third parties.                                                  |
| `Bilateral NDA`    | In this type, both parties are obligated to keep the resulting and acquired information confidential. This is the most common type of NDA that protects the work of penetration testers.                |
| `Multilateral NDA` | Multilateral NDA is a commitment to confidentiality by more than two parties. If we conduct a penetration test for a cooperative network, all parties responsible and involved must sign this document. |

Below is a sample (not exhaustive) list of company members who may be authorized to hire us for penetration testing.

| Chief Executive Officer (CEO) | Chief Technical Officer (CTO) | Chief Information Security Officer (CISO) |
| ----------------------------- | ----------------------------- | ----------------------------------------- |
| Chief Security Officer (CSO)  | Chief Risk Officer (CRO)      | Chief Information Officer (CIO)           |
| VP of Internal Audit          | Audit Manager                 | VP or Director of IT/Information Security |

This stage also requires the preparation of several documents before a penetration test can be conducted that must be signed by our client and us so that the declaration of consent can also be presented in written form if required.

| **Document**                                                         | **Timing for Creation**                             |
| -------------------------------------------------------------------- | --------------------------------------------------- |
| `1. Non-Disclosure Agreement` (`NDA`)                                | `After` Initial Contact                             |
| `2. Scoping Questionnaire`                                           | `Before` the Pre-Engagement Meeting                 |
| `3. Scoping Document`                                                | `During` the Pre-Engagement Meeting                 |
| `4. Penetration Testing Proposal` (`Contract/Scope of Work` (`SoW`)) | `During` the Pre-engagement Meeting                 |
| `5. Rules of Engagement` (`RoE`)                                     | `Before` the Kick-Off Meeting                       |
| `6. Contractors Agreement` (Physical Assessments)                    | `Before` the Kick-Off Meeting                       |
| `7. Reports`                                                         | `During` and `after` the conducted Penetration Test |



### Scoping Questionnaire

After initial contact is made with the client, we typically send them a `Scoping Questionnaire` to better understand the services they are seeking. This scoping questionnaire should clearly explain our services and may typically ask them to choose one or more from the following list:

|                                     |                                       |
| ----------------------------------- | ------------------------------------- |
| ☐ Internal Vulnerability Assessment | ☐ External Vulnerability Assessment   |
| ☐ Internal Penetration Test         | ☐ External Penetration Test           |
| ☐ Wireless Security Assessment      | ☐ Application Security Assessment     |
| ☐ Physical Security Assessment      | ☐ Social Engineering Assessment       |
| ☐ Red Team Assessment               | ☐ Web Application Security Assessment |

Aside from the assessment type, client name, address, and key personnel contact information, some other critical pieces of information include:

<table><thead><tr><th width="748"></th><th></th></tr></thead><tbody><tr><td>How many expected live hosts?</td><td></td></tr><tr><td>How many IPs/CIDR ranges in scope?</td><td></td></tr><tr><td>How many Domains/Subdomains are in scope?</td><td></td></tr><tr><td>How many wireless SSIDs in scope?</td><td></td></tr><tr><td>How many web/mobile applications? If testing is authenticated, how many roles (standard user, admin, etc.)?</td><td></td></tr><tr><td>For a phishing assessment, how many users will be targeted? Will the client provide a list, or we will be required to gather this list via OSINT?</td><td></td></tr><tr><td>If the client is requesting a Physical Assessment, how many locations? If multiple sites are in-scope, are they geographically dispersed?</td><td></td></tr><tr><td>What is the objective of the Red Team Assessment? Are any activities (such as phishing or physical security attacks) out of scope?</td><td></td></tr><tr><td>Is a separate Active Directory Security Assessment desired?</td><td></td></tr><tr><td>Will network testing be conducted from an anonymous user on the network or a standard domain user?</td><td></td></tr><tr><td>Do we need to bypass Network Access Control (NAC)?</td><td></td></tr></tbody></table>

Finally, we will want to ask about information disclosure and evasiveness (if applicable to the assessment type):

* Is the Penetration Test black box (no information provided), grey box (only IP address/CIDR ranges/URLs provided), white box (detailed information provided)
* Would they like us to test from a non-evasive, hybrid-evasive (start quiet and gradually become "louder" to assess at what level the client's security personnel detect our activities), or fully evasive.

### **Rules of Engagement - Checklist**

| **Checkpoint**                              | **Contents**                                                                                          |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `☐ Introduction`                            | Description of this document.                                                                         |
| `☐ Contractor`                              | Company name, contractor full name, job title.                                                        |
| `☐ Penetration Testers`                     | Company name, pentesters full name.                                                                   |
| `☐ Contact Information`                     | Mailing addresses, e-mail addresses, and phone numbers of all client parties and penetration testers. |
| `☐ Purpose`                                 | Description of the purpose for the conducted penetration test.                                        |
| `☐ Goals`                                   | Description of the goals that should be achieved with the penetration test.                           |
| `☐ Scope`                                   | All IPs, domain names, URLs, or CIDR ranges.                                                          |
| `☐ Lines of Communication`                  | Online conferences or phone calls or face-to-face meetings, or via e-mail.                            |
| `☐ Time Estimation`                         | Start and end dates.                                                                                  |
| `☐ Time of the Day to Test`                 | Times of the day to test.                                                                             |
| `☐ Penetration Testing Type`                | External/Internal Penetration Test/Vulnerability Assessments/Social Engineering.                      |
| `☐ Penetration Testing Locations`           | Description of how the connection to the client network is established.                               |
| `☐ Methodologies`                           | OSSTMM, PTES, OWASP, and others.                                                                      |
| `☐ Objectives / Flags`                      | Users, specific files, specific information, and others.                                              |
| `☐ Evidence Handling`                       | Encryption, secure protocols                                                                          |
| `☐ System Backups`                          | Configuration files, databases, and others.                                                           |
| `☐ Information Handling`                    | Strong data encryption                                                                                |
| `☐ Incident Handling and Reporting`         | Cases for contact, pentest interruptions, type of reports                                             |
| `☐ Status Meetings`                         | Frequency of meetings, dates, times, included parties                                                 |
| `☐ Reporting`                               | Type, target readers, focus                                                                           |
| `☐ Retesting`                               | Start and end dates                                                                                   |
| `☐ Disclaimers and Limitation of Liability` | System damage, data loss                                                                              |
| `☐ Permission to Test`                      | Signed contract, contractors agreement                                                                |



















































































