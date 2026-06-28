---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-05_multiple-information-exposed-due-to-misconfigured-service-now-itsm-instances.md
original_filename: 2020-06-05_multiple-information-exposed-due-to-misconfigured-service-now-itsm-instances.md
title: Multiple Information exposed due to misconfigured Service-now ITSM instances
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 2c31a9ea30cc8870e8359d4dfeaec3f532780f1d0f48f785dd7a6665f1a33a57
text_sha256: 0aa330e3629975f47f20539cb2a34739aebb89968b1639521ba003abbf92aad3
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Information exposed due to misconfigured Service-now ITSM instances

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-05_multiple-information-exposed-due-to-misconfigured-service-now-itsm-instances.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `2c31a9ea30cc8870e8359d4dfeaec3f532780f1d0f48f785dd7a6665f1a33a57`
- Text SHA256: `0aa330e3629975f47f20539cb2a34739aebb89968b1639521ba003abbf92aad3`


## Content

---
title: "Multiple Information exposed due to misconfigured Service-now ITSM instances"
url: "https://medium.com/@th3g3nt3l/multiple-information-exposed-due-to-misconfigured-service-now-itsm-instances-de7a303ebd56"
authors: ["Th3G3nt3lman (@Th3G3nt3lman)"]
bugs: ["Missing authentication", "Information disclosure"]
bounty: "30,000"
publication_date: "2020-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4523
scraped_via: "browseros"
---

# Multiple Information exposed due to misconfigured Service-now ITSM instances

Multiple Information exposed due to misconfigured Service-now ITSM instances
Th3G3nt3lman
Follow
3 min read
·
Jun 5, 2020

754

4

ServiceNow is a cloud-based company that provides software as a service (SaaS) for technical management support. The company specializes in IT services management (ITSM), IT operations management (ITOM) and IT business management (ITBM), allowing users to manage projects, teams and customer interactions via a variety of apps and plugins.

ServiceNow products offer a service model based on what can help users identify the root cause of the issues they encounter, as well as helps them to correct issues with self-service. The service model appears as tasks, activities and processes from ServiceNow products, separated by cloud services.

To reach your instance it will be using: https://yourcompanyname.service-now.com

The issue

One of the modules that i worked on is the Knowledge base, The ServiceNow® Knowledge Management (KM) application enables the sharing of information in knowledge bases. These knowledge bases contain articles that provide users with information such as self-help, troubleshooting, and task resolution.

Once created each KB is identified with a unique number as seen below :

Press enter or click to view image in full size
Number Column is the unique identifier

and once a user opens one of those articles the endpoint called is the below :

https://company.service-now.com/kb_view_customer.do?sysparm_article=KB00xxxx

Exploitation

It was noticed a lot of companies had this endpoints reachable publicly without authentication, even though reaching the company instance itself directly will send you to Okta, onelogin, ..etc in order to login with corporate credentials, but not for the KB endpoints.

The best methodology for me was doing a normal subdomain scan for *.service-now, then using top alexa companies as list and bruteforce subdomains, lastly checking what out of those companies had a bug bounty program.

Get Th3G3nt3lman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once the misconfigured instance identified i used burp intruder to bruteforce the latest 4 digits of sysparm_article parameter, then i sorted results by size or by using burp Grep/Match options for words like (password, internal, credentials, confidential)

Results

For most of the companies tested it was identified this is was not used as intended ( Knowledge base ) , summary of findings was :

1- Internal Procedures , SOP, Diagrams , development plans.

2- Passwords, tokens for Internal corporate domains.

3- Attachments for change requests contained IP addresses, configurations.

4- Some customers PII in communications between employees.

For other companies that was an accepted risk, as there wasn’t anything sensitive or with an impact if an unauthorized person read it, but still i encouraged them to fix the permission issue.

Initial Discovery to $30,000

It took almost two days to report the findings for multiple companies externally or within H1 & bugcrowd platforms with the help and support of my close friends, that resulted so far in approximately 30K bounties and still some reports are in triage.

Servicenow is one of the top 5 cloud ITSM’s and its used by a lot of big companies worldwide.

Is this a vulnerability in servicenow product?

No. This is a common misconfiguration made by the individual companies where they didn't setup the permission properly on knowledge base and had it opened for unauthorized people publicly.
