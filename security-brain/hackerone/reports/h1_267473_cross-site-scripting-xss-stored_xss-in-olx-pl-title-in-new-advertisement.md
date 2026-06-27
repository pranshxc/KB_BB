---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267473'
original_report_id: '267473'
title: XSS in OLX.pl ("title" in new advertisement)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: olx
created_at: '2017-09-11T10:06:15.283Z'
disclosed_at: '2018-07-18T09:14:20.998Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in OLX.pl ("title" in new advertisement)

## Metadata

- HackerOne Report ID: 267473
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: olx
- Disclosed At: 2018-07-18T09:14:20.998Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found XSS vulnerability in "new advertisement" in OLX.pl
Step to reproduce:
1. Go to https://www.olx.pl/nowe-ogloszenie/
2. Put this payload "<svg/onload=prompt(document.cookie)>" in "add-title" element
3. Complete all data in this form and click Next
4. On the next page we can see executed XSS

Regards,
4rch

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
