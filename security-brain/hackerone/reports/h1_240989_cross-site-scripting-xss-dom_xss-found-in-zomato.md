---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '240989'
original_report_id: '240989'
title: xss found in zomato
weakness: Cross-site Scripting (XSS) - DOM
team_handle: zomato
created_at: '2017-06-17T12:01:13.500Z'
disclosed_at: '2017-06-30T04:51:26.716Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# xss found in zomato

## Metadata

- HackerOne Report ID: 240989
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: zomato
- Disclosed At: 2017-06-30T04:51:26.716Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

while i was testing with your site i found a xss at add the restraunt option

steps to reproduce

1) login to zomato
2) goto add restraunt
3) in the name feild add any xss payload
4)complete it
 the restraunt will be sent for verification to the verification team and the xss payload will also be sent to there and get executed there
screen shot added

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
