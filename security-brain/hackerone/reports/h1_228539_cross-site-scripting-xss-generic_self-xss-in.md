---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228539'
original_report_id: '228539'
title: self xss in
weakness: Cross-site Scripting (XSS) - Generic
team_handle: quora
created_at: '2017-05-15T16:01:11.452Z'
disclosed_at: '2017-05-22T22:54:08.333Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# self xss in

## Metadata

- HackerOne Report ID: 228539
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: quora
- Disclosed At: 2017-05-22T22:54:08.333Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Quora security team,

there is self XSS vulnerability in https://www.quora.com/profile/Username/

Steps:

copy and paste the link in chrome browser (copy entire link within double quotes
**"javascript:alert(document.domain)//https://www.quora.com/profile/Username/"**

then XSS payload will trigger

please let me know if you need more information.

best

Panther

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
