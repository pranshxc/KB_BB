---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-30_domain-takeover-without-domain-admin-permissions.md
original_filename: 2023-06-30_domain-takeover-without-domain-admin-permissions.md
title: Domain Takeover Without Domain Admin Permissions
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: ac4ba650e6a0268149bb7b72e3849f8c7280a81b04b18adc59f05e092a52988a
text_sha256: 8c524f7867320f3e019e1bc03bf6d103b50d32c8a8f31fd23995d094cc5f8675
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Domain Takeover Without Domain Admin Permissions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-30_domain-takeover-without-domain-admin-permissions.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `ac4ba650e6a0268149bb7b72e3849f8c7280a81b04b18adc59f05e092a52988a`
- Text SHA256: `8c524f7867320f3e019e1bc03bf6d103b50d32c8a8f31fd23995d094cc5f8675`


## Content

---
title: "Domain Takeover Without Domain Admin Permissions"
url: "https://medium.themayor.tech/domain-takeover-without-domain-admin-permissions-28a7bd330501"
authors: ["Joe Helle (@joehelle)"]
bugs: ["Active Directory Privilege Escalation", "Internal pentest"]
publication_date: "2023-06-30"
added_date: "2023-07-04"
source: "pentester.land/writeups.json"
original_index: 983
scraped_via: "browseros"
---

# Domain Takeover Without Domain Admin Permissions

Member-only story

Domain Takeover Without Domain Admin Permissions
Joe Helle
Follow
4 min read
·
Jun 29, 2023

20

1

Introduction

About a year ago I was conducting an internal assessment, and it was clear that the network was vulnerable to man in the middle attacks (in this case, IPv6 was vulnerable). Despite the network vulnerability, the client did a fairly decent job of limiting domain administrator usage across the network, and I wasn’t relaying anything of value.

At some point ntlmrelayx started getting me excited by saying that user privileges were found, and that it would attempt to add a new user with enterprise administrator privileges. Unfortunately, another message came across that said that the user account did not have create user privileges. How can that be so, and how did this become my favorite internal compromise attack?

Here’s how.

Not All Admins Are Created Equally

When systems administrators consider principles of least privilege, the use of stepdown accounts comes to mind. Rather than administrators using full domain admin or enterprise admin accounts, they grant privileges to their daily driver accounts that allow them to conduct administrative tasks without the risk of compromising the full domain admin account.

Take the below as an example. In the mayorsec.local domain, there are three domain administrators — a.adams, themayor, and the default administrator account.
