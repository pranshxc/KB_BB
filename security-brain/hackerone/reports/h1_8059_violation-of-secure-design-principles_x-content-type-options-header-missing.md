---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8059'
original_report_id: '8059'
title: X-Content-Type-Options header missing
weakness: Violation of Secure Design Principles
team_handle: localize
created_at: '2014-04-18T17:25:00.081Z'
disclosed_at: '2014-05-19T01:16:44.310Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# X-Content-Type-Options header missing

## Metadata

- HackerOne Report ID: 8059
- Weakness: Violation of Secure Design Principles
- Program: localize
- Disclosed At: 2014-05-19T01:16:44.310Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL :  http://www.localize.io/

Description : The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'

Solution : This check is specific to Internet Explorer 8 and Google Chrome. Ensure each page sets a Content-Type header and the X-CONTENT-TYPE-OPTIONS if the Content-Type header is unknown

content sniffing is possible

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
