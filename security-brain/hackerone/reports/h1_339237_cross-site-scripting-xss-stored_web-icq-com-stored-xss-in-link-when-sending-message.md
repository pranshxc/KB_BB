---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '339237'
original_report_id: '339237'
title: '[web.icq.com] Stored XSS in link when sending message'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2018-04-16T19:48:10.099Z'
disclosed_at: '2018-10-01T10:13:13.089Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [web.icq.com] Stored XSS in link when sending message

## Metadata

- HackerOne Report ID: 339237
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-10-01T10:13:13.089Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
https://web.icq.com/


Testing environment
--
Chrome

Steps to reproduce
--
1) Enter a chat
2) Send the following message:

``https://www.google.com/"onmouseover="javascript:prompt()"``

3) Hover the link

Actual results
--

XSS prompt shows.

Expected results, security impact description and recommendations
--


The **"** character should be sanitized.

PoC, exploit code, screenshots, video, references, additional resources
--

## Impact

If a victim opens a message and hovers this link, the attacker can perform actions on behalf of the victim (modify account info etc).

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://web.icq.com/

**Verified**
Yes

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
