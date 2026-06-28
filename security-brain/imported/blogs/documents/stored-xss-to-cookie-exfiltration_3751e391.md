---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_stored-xss-to-cookie-exfiltration.md
original_filename: 2022-10-26_stored-xss-to-cookie-exfiltration.md
title: Stored XSS To Cookie Exfiltration
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
raw_sha256: 3751e391a370799f61e80b789e47b97ed49b1e39a8c9ffb6033afc11fa1cbba7
text_sha256: 0adc21705ac9369e0155e98fc75d6f2eef422d4beaf95679f1489bfc68dc86d2
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS To Cookie Exfiltration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_stored-xss-to-cookie-exfiltration.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `3751e391a370799f61e80b789e47b97ed49b1e39a8c9ffb6033afc11fa1cbba7`
- Text SHA256: `0adc21705ac9369e0155e98fc75d6f2eef422d4beaf95679f1489bfc68dc86d2`


## Content

---
title: "Stored XSS To Cookie Exfiltration"
url: "https://medium.com/@raymond-lind/stored-xss-to-cookie-exfiltration-2cbca6a8c7f0"
authors: ["Raymond Lind"]
bugs: ["Stored XSS"]
publication_date: "2022-10-26"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1990
scraped_via: "browseros"
---

# Stored XSS To Cookie Exfiltration

Member-only story

Stored XSS To Cookie Exfiltration
Raymond Lind
Follow
8 min read
·
Oct 26, 2022

9

1

Today I will be explaining an XSS (“Cross Site Scripting”) vulnerability I found in a private bug bounty program that allowed me to exfiltrate victim’s cookies and steal sensitive user data.

Introduction

When noticing applications that allow for multiple user input fields to be reflected into different parts of the website, they are a great target to thoroughly test for XSS vulnerabilities. This is because when allowing user input, websites often fail to implement safe coding practices such as filtering, encoding, and CSP configurations, which therefore allow users to exploit these weaknesses to carry out attacks like XSS. Whenever I see many input fields, XSS is one of the first things I look for as it is one the most common vulnerabilities in web applications and often has a high impact on overall security.

So How Does XSS Occur?

XSS or Cross Site Scripting is a vulnerability in which user input is processed in an unsafe way, allowing attackers to break out or modify the context of the code and insert their own within it. This causes the attacker to be able to execute arbitrary javascript on the vulnerable site which can turn out to be very dangerous if leveraged against other users correctly. This can lead to performing actions on other accounts without their permission, stealing…
