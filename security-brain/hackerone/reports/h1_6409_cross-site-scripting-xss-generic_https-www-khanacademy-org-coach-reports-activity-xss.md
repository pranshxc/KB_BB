---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6409'
original_report_id: '6409'
title: https://www.khanacademy.org/coach/reports/activity XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-04-08T06:07:23.800Z'
disclosed_at: '2014-04-09T17:06:12.302Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# https://www.khanacademy.org/coach/reports/activity XSS

## Metadata

- HackerOne Report ID: 6409
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2014-04-09T17:06:12.302Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I created a class called `"><img src=x onerror=alert(4)>`, I hope that you know how to make a class..
After that, when you go to https://www.khanacademy.org/coach/reports/activity and select a class it might not load directly but when you reloud the page it will (and persistent).

Best regards,

Olivier Beg

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
