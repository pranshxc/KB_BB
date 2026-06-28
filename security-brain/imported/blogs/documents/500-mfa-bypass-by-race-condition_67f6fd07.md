---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-28_500-mfa-bypass-by-race-condition.md
original_filename: 2024-01-28_500-mfa-bypass-by-race-condition.md
title: '500$: MFA bypass By Race Condition'
category: documents
detected_topics:
- mfa
- command-injection
- otp
- race-condition
- api-security
tags:
- imported
- documents
- mfa
- command-injection
- otp
- race-condition
- api-security
language: en
raw_sha256: 67f6fd07cc1b2b5f67a8ea9a830ad3d870afc8d13743ab2054651cc50eb8720e
text_sha256: 177d080409d96080b863cf1ea9fcb35c034b000e1357c79d83f5367d76d7a49e
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# 500$: MFA bypass By Race Condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-28_500-mfa-bypass-by-race-condition.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, race-condition, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `67f6fd07cc1b2b5f67a8ea9a830ad3d870afc8d13743ab2054651cc50eb8720e`
- Text SHA256: `177d080409d96080b863cf1ea9fcb35c034b000e1357c79d83f5367d76d7a49e`


## Content

---
title: "500$: MFA bypass By Race Condition"
url: "https://medium.com/@a13h1/500-mfa-bypass-by-race-condition-176421462902"
authors: ["Abhi Sharma (@a13h1_)"]
bugs: ["Race condition", "2FA / MFA bypass"]
bounty: "500"
publication_date: "2024-01-28"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 489
scraped_via: "browseros"
---

# 500$: MFA bypass By Race Condition

Member-only story

500$: MFA bypass By Race Condition
Abhi Sharma
Follow
3 min read
·
Jan 27, 2024

1K

4

The article is about a bug I found when I was trying to break the other logic in the software. But instead i founded a way to bypass the MFA by Race Condition.

Press enter or click to view image in full size

Last year I was hunting on a private program and I hit a point where it asked for MFA to generate the API key, and there was a limit of 10 API keys. I tried to make more than 10, and I found that using Race Condition I could bypass the MFA without code.

The Flow

The API keys generated in the integration process are crucial for accessing and controlling Exendly accounts. MFA is implemented to ensure that only genuine users can generate these keys, preventing unauthorized access and potential misuse. The discovered vulnerability compromises the integrity of MFA, potentially granting unauthorized users control over admin accounts.

Bug Description

My testing has uncovered a significant security issue within Exendly’s(Virtual name of bbp) integration platform, specifically related to Multi-Factor Authentication (MFA). The bug allows an attacker to exploit a race condition during the generation of API tokens, potentially leading to unauthorized access and compromising the security of Exendly’s accounts.

When users attempt to generate API tokens on the integration platform, the MFA process is initiated to…
