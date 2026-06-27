---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8053'
original_report_id: '8053'
title: X-Content-Type-Options header missing
weakness: Violation of Secure Design Principles
team_handle: respondly
created_at: '2014-04-18T16:31:24.890Z'
disclosed_at: '2014-05-21T03:32:00.072Z'
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

- HackerOne Report ID: 8053
- Weakness: Violation of Secure Design Principles
- Program: respondly
- Disclosed At: 2014-05-21T03:32:00.072Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL : https://respond.ly/

Description : The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'

Solution : This check is specific to Internet Explorer 8 and Google Chrome. Ensure each page sets a Content-Type header and the X-CONTENT-TYPE-OPTIONS if the Content-Type header is unknown

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
