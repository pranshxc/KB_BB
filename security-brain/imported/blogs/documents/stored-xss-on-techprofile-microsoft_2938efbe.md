---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-09_stored-xss-on-techprofile-microsoft.md
original_filename: 2019-05-09_stored-xss-on-techprofile-microsoft.md
title: Stored XSS on Techprofile Microsoft
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 2938efbea9b897b0538508cca9659c71bc499bbcd45461144832ddbeb7272d08
text_sha256: 7cded404935dc2c96bd40ae529e1fd4bcb0fad60c30300c7575e6ce9c0d01d78
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Techprofile Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-09_stored-xss-on-techprofile-microsoft.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2938efbea9b897b0538508cca9659c71bc499bbcd45461144832ddbeb7272d08`
- Text SHA256: `7cded404935dc2c96bd40ae529e1fd4bcb0fad60c30300c7575e6ce9c0d01d78`


## Content

---
title: "Stored XSS on Techprofile Microsoft"
url: "https://medium.com/@kang_ali/stored-xss-on-techprofile-microsoft-d21757588cc1"
authors: ["Mohammad Ali Syarief"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
publication_date: "2019-05-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5265
scraped_via: "browseros"
---

# Stored XSS on Techprofile Microsoft

Stored XSS on Techprofile Microsoft
Mohammad Ali Syarief
Follow
2 min read
·
May 10, 2019

49

1

Details to Reproduce

Stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. The input that is stored is not correctly filtered.

** Introduction

Profile on Microsoft Learn Introducing a new approach to learning. The skills required to advance your career and earn your spot at the top do not come easily. Now there’s a more rewarding approach to hands-on learning that helps you achieve your goals faster. Earn points, levels, and achieve more!

** The bug

Vulnerability: XSS Stored (Stored Cross site scripting)
Severity: High
Owasp rank: (OTG-INPVAL-002)

Stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. The input that is stored is not correctly filtered.

Vulnerable Link on Profil : https://techprofile.microsoft.com/en-us/[profile]

** Scenario POC

Get Mohammad Ali Syarief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Attacker Edit Profil on https://techprofile.microsoft.com/en-us/edit
2. Set Payload XSS
3. Victim see Profil Attacker
4. Cookie send To Attacker Server

** Impact

Users can execute arbitrary JavaScript code in the context of other users. This is critical when targeted users have high privileges. Attackers are then able to grant themselves the administrator privileges and even takeover the ownership of the New Relic account.

The hacker selected the Cross-site Scripting (XSS) — Stored weakness. This vulnerability type requires contextual information from the hacker.

** Remediation

To protect against stored XSS attacks, make sure any dynamic content coming from the data store cannot be used to inject JavaScript on a page.

Referensi :

https://www.owasp.org/index.php/Testing_for_Stored_Cross_site_scripting_(OTG-INPVAL-002)

28/04/2019 ~ Report Vulnerability
30/04/2019 ~ Open Case.
08/05/2019 ~ -Patched / Fixed
