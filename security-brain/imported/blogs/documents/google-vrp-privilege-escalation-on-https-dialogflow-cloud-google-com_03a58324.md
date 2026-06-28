---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-13_google-vrp-privilege-escalation-on-httpsdialogflowcloudgooglecom.md
original_filename: 2021-06-13_google-vrp-privilege-escalation-on-httpsdialogflowcloudgooglecom.md
title: '[Google VRP] Privilege escalation on https://dialogflow.cloud.google.com'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- cloud-security
language: en
raw_sha256: 03a58324cb233b7a372085394354c7db7d0b04421171cb5b8bb073e7969c7a44
text_sha256: a1b8115573144885ec62d710d400e6de4ab9200bd73d98f53a6b77599449eba0
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# [Google VRP] Privilege escalation on https://dialogflow.cloud.google.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-13_google-vrp-privilege-escalation-on-httpsdialogflowcloudgooglecom.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `03a58324cb233b7a372085394354c7db7d0b04421171cb5b8bb073e7969c7a44`
- Text SHA256: `a1b8115573144885ec62d710d400e6de4ab9200bd73d98f53a6b77599449eba0`


## Content

---
title: "[Google VRP] Privilege escalation on https://dialogflow.cloud.google.com"
url: "https://0x01alka.medium.com/google-vrp-privilege-escalation-on-https-dialogflow-cloud-google-com-599af6c4516d"
authors: ["lalka (@0x01alka)"]
programs: ["Google"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "3,133.70"
publication_date: "2021-06-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3582
scraped_via: "browseros"
---

# [Google VRP] Privilege escalation on https://dialogflow.cloud.google.com

[Google VRP] Privilege escalation on https://dialogflow.cloud.google.com
lalka
Follow
1 min read
·
Jun 13, 2021

136

2

Hi.

This is a short story (because I’m lazy, yes) about my last bug for Google VRP.

While testing the privilege escalation problems on https://dialogflow.cloud.google.com/ I noticed that downgrading the access level for the invited user does not work as expected.

Steps to reproduce:

1. Go to https://dialogflow.cloud.google.com/#/editAgent/{project}/ settings -> Share -> invite another user with “Developer” role.
2. Downgrade “Developer” role to “Reviewer” and apply changes.
3. Observe that although the changes have been applied and the role is “Reviewer” now, but the user can still perform all actions as “Developer”.

But why?

Get lalka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I went to https://console.cloud.google.com/iam-admin/ and saw that roles and assignments of invited users for https://dialogflow.cloud.google.com/#/editAgent/{project}/ not changing properly. When access level are changed, the permissions do not change (“Developer” -> “ Reviewer “), but adding to each other (“ Developer “+” Reviewer “).

Timeline :

Apr 6, 2021 reported
Apr 7, 2021 triaged
Apr 16, 2021 Nice catch!
Apr 22, 2021 Awarded $3133.70
Jun 13, 2021 Fix
