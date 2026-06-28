---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-22_harvesting-all-private-invites-using-leave-program-fast-tracked-invitation-and-s.md
original_filename: 2018-10-22_harvesting-all-private-invites-using-leave-program-fast-tracked-invitation-and-s.md
title: Harvesting all private invites using leave program fast-tracked invitation
  and security@ email forwarding feature
category: documents
detected_topics:
- business-logic
- command-injection
- otp
tags:
- imported
- documents
- business-logic
- command-injection
- otp
language: en
raw_sha256: 562c08fc9e563736422a85d44328c9132e09494251b5d9fc1e7d952d9f4d0873
text_sha256: df6852d49ca3a9a473fae16b598191c61763ab31f4d3514c5516f677320492a6
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Harvesting all private invites using leave program fast-tracked invitation and security@ email forwarding feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-22_harvesting-all-private-invites-using-leave-program-fast-tracked-invitation-and-s.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `562c08fc9e563736422a85d44328c9132e09494251b5d9fc1e7d952d9f4d0873`
- Text SHA256: `df6852d49ca3a9a473fae16b598191c61763ab31f4d3514c5516f677320492a6`


## Content

---
title: "Harvesting all private invites using leave program fast-tracked invitation and security@ email forwarding feature"
url: "https://medium.com/japzdivino/harvesting-all-private-invites-using-leave-program-fast-tracked-invitation-and-security-email-a01c8b3ce76f"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["Logic flaw"]
bounty: "2,500"
publication_date: "2018-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5635
scraped_via: "browseros"
---

# Harvesting all private invites using leave program fast-tracked invitation and security@ email forwarding feature

Member-only story

Harvesting all private invites using leave program fast-tracked invitation and security@ email forwarding feature
Japz Divino
Follow
3 min read
·
Oct 22, 2018

219

2

Severity: Medium (6.1)
Weakness: Business Logic Errors (CWE-840)

Summary:

I have found a way that it is possible to harvest all private HackerOne invitation using the Leave Program feature together with the Security@ email forwarding feature without any user interaction.

HackerOne Security@ Email Forwarding Feature

First, when the program activated the security@ email forwarding feature on hackerone and the hacker sent an email to company configured security email (e.g security@company.com), hackerone system will send an automated email invitation token (link) to hackers and this invitation will allow the hackers to join and become a participants of private program. (see image below)

Automated HackerOne email invitation for private programs having security@ email forwarding feature enabled.

Decline Invites and Leave Programs

Now, hackers can choose to leave the program in exchange of another automated invite when the hackers filled-up the leave program survey form using the new Leave Program functionality. (see image below)
