---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-12_unveiling-vulnerabilities-loose-permissions-in-salesforce-lightning-pose-data-se.md
original_filename: 2024-01-12_unveiling-vulnerabilities-loose-permissions-in-salesforce-lightning-pose-data-se.md
title: 'Unveiling Vulnerabilities: Loose Permissions in Salesforce Lightning Pose
  Data Security Threats'
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- cloud-security
language: en
raw_sha256: 11c06905b568c0f88fb9c2b4c6f604ff0379596e90dcd2062fc65eff6630bcf2
text_sha256: cf43330a49bc0057b9a756dd868eb06b75a5f67499b0e6337f011e45005bc0ad
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Unveiling Vulnerabilities: Loose Permissions in Salesforce Lightning Pose Data Security Threats

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-12_unveiling-vulnerabilities-loose-permissions-in-salesforce-lightning-pose-data-se.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `11c06905b568c0f88fb9c2b4c6f604ff0379596e90dcd2062fc65eff6630bcf2`
- Text SHA256: `cf43330a49bc0057b9a756dd868eb06b75a5f67499b0e6337f011e45005bc0ad`


## Content

---
title: "Unveiling Vulnerabilities: Loose Permissions in Salesforce Lightning Pose Data Security Threats"
url: "https://samshadow.medium.com/unveiling-vulnerabilities-loose-permissions-in-salesforce-lightning-pose-data-security-threats-41eaba372937"
authors: ["Sam Shadow"]
bugs: ["Information disclosure", "Salesforce"]
publication_date: "2024-01-12"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 550
scraped_via: "browseros"
---

# Unveiling Vulnerabilities: Loose Permissions in Salesforce Lightning Pose Data Security Threats

Unveiling Vulnerabilities: Loose Permissions in Salesforce Lightning Pose Data Security Threats
Sam Shadow
Follow
2 min read
·
Jan 13, 2024

67

Introduction:

Salesforce Lightning is a potent CRM solution that makes it easier to develop data-driven applications in the ever-evolving web application landscape. However, a recent vulnerability report has revealed possible security risks related to the loose permissions on some objects within the Salesforce Lightning instance at https://example.com/s/sfsites/aura. This disclosure makes it possible for unauthenticated attackers to extract sensitive data from various objects, which poses a serious risk to data security.

Vulnerability Discovery:

Using Salesforce Lightning, the web application in question has loose permissions granted to unauthenticated Guest users on important objects like Case, Account, User, Contact, Document, ContentDocument, ContentVersion, ContentBody, CaseComment, Note, Employee, Attachment, EmailMessage, CaseExternalDocument, Lead, Name, EmailTemplate, and EmailMessageRelation. This oversight could potentially allow a malicious attacker to extract sensitive data belonging to other users of the application by crafting HTTP requests directly to the Aura API at https://example.com/s/sfsites/aura and using built-in controller methods.

Steps to Reproduce:
Ensure Burp Suite is sniffing all HTTP(S) requests in the background
Navigate to https://example.com/s/, this is to retrieve a template aura request for use
Find a POST request in Burp's Proxy history to the /s/sfsites/aura endpoint. Send it to the repeater
Change the message POST parameter to the payload below. Please note that all other parameters should remain untouched, and that in this example payload, a pageSize of 100 is used for speed however more records can be retrieved:

message={“actions”:[{“id”:”123;a”,”descriptor”:”serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems”,”callingDescriptor”:”UNKNOWN”,”params”:{“entityNameOrId”:”<OBJECT>”,”layoutType”:”FULL”,”pageSize”:100,”currentPage”:0,”useTimeout”:false,”getCount”:false,”enableRowActions”:false}}]}

Get Sam Shadow’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6) Submit the request

7) The response contains sensitive information belonging to other users.

Impact:

The platform’s inability to implement adequate authorization checks is caused by the loose permissions on particular objects within the Salesforce Lightning instance. As a result, unauthenticated attackers can take advantage of this vulnerability and extract sensitive data from records within these objects. This data could include information pertaining to Case, Account, User, Contact, Document, and more, thereby posing a serious risk to the confidentiality and integrity of user information.

Conclusion:

Since more and more businesses are depending on CRM solutions like Salesforce Lightning, it is critical to identify and fix security flaws like the one that was found in the Salesforce Lightning instance. Security teams, administrators, and developers should work together to implement the necessary fixes, ensuring a secure and resilient web application environment. Proactive measures like regular security audits and updates are crucial to protecting sensitive data and keeping users trusting the digital ecosystem.
