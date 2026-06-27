---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9318'
original_report_id: '9318'
title: Home page reflected XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-04-23T10:58:46.134Z'
disclosed_at: '2014-06-06T11:43:17.708Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Home page reflected XSS

## Metadata

- HackerOne Report ID: 9318
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-06-06T11:43:17.708Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is an XSS on the front page of mail.ru which can be exploited by manipulating the _regionConfirm_ page parameter. The parameter is included without proper escaping in JavaScript code featured on the page. Because of the nature of the exploit, browser XSS protection may be bypassed.

Proof-of-concept:

http://mail.ru/?regionConfirm=alert(document.cookie)});}}%3C/script%3E

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
