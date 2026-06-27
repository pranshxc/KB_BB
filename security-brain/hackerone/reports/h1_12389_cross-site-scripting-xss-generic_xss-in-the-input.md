---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12389'
original_report_id: '12389'
title: XSS in the input
weakness: Cross-site Scripting (XSS) - Generic
team_handle: respondly
created_at: '2014-05-17T17:15:01.875Z'
disclosed_at: '2014-07-08T10:00:33.994Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in the input

## Metadata

- HackerOne Report ID: 12389
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: respondly
- Disclosed At: 2014-07-08T10:00:33.994Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://app.respond.ly/create
once there go to Team Name and input the code ?'"--></style></script><script>alert(1337)</script> and put the email as a valid one and should inject the XSS code even should show when u login all the time.

Thanks,
Jordan Jones
@CEHSecurity

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
