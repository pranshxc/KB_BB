---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-31_bypass-hackerone-2fa-requirement-and-reporter-blacklist.md
original_filename: 2018-10-31_bypass-hackerone-2fa-requirement-and-reporter-blacklist.md
title: Bypass HackerOne 2FA requirement and reporter blacklist
category: documents
detected_topics:
- mfa
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- mfa
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 3a84c9b6f35eba776fe7d88f3d79d231d88269c8f796da4d79ecf8c6298d26fd
text_sha256: 09491afa004716d039c57486386c2a1d60f13fad2c0d0edcba32272f493504be
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass HackerOne 2FA requirement and reporter blacklist

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-31_bypass-hackerone-2fa-requirement-and-reporter-blacklist.md
- Source Type: markdown
- Detected Topics: mfa, access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `3a84c9b6f35eba776fe7d88f3d79d231d88269c8f796da4d79ecf8c6298d26fd`
- Text SHA256: `09491afa004716d039c57486386c2a1d60f13fad2c0d0edcba32272f493504be`


## Content

---
title: "Bypass HackerOne 2FA requirement and reporter blacklist"
url: "https://medium.com/japzdivino/bypass-hackerone-2fa-requirement-and-reporter-blacklist-46d7959f1ee5"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["Logic flaw", "2FA / MFA bypass", "Broken authentication"]
bounty: "10,000"
publication_date: "2018-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5616
scraped_via: "browseros"
---

# Bypass HackerOne 2FA requirement and reporter blacklist

Member-only story

Bypass HackerOne 2FA requirement and reporter blacklist
Japz Divino
Follow
4 min read
·
Oct 31, 2018

730

7

Severity: Medium (5.0) — High (7.1)
Weakness: Improper Authorization
Bounty: $10,000

Summary:

First, the initial submission got a bounty of $2,500. But while HackerOne was doing their Root Cause Analysis (RCA) of my report submission, they have stumbled upon another vulnerability with High severity.

Since my submission gives them a nudge in the right direction, they rewarded me another $7,500 for the increase scope of finding.

Research:

My routine when i am hunting on HackerOne main platform is always checking if they have new incoming feature, And i saw that there is beta feature called Embedded Submission Form which enables hackers to Anonymously submit reports without having to create an account on HackerOne. For additional information. Learn more here.

Now, with that new feature i have found an Improper Authorization bug that bypasses the 2 security features of HackerOne for the bug bounty programs.

Bypass 2FA requirements when submitting new reports to a program. Learn more here.
Bypass hacker blacklisted by a program (when a program does not want to receive report from specific hackers). Learn more here.
Bypass 2FA requirements when submitting new reports to a program
