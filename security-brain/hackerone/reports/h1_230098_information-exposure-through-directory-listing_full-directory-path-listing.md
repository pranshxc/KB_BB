---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230098'
original_report_id: '230098'
title: Full directory path listing
weakness: Information Exposure Through Directory Listing
team_handle: paragonie
created_at: '2017-05-20T08:15:30.071Z'
disclosed_at: '2017-05-20T21:53:04.349Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 13
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Full directory path listing

## Metadata

- HackerOne Report ID: 230098
- Weakness: Information Exposure Through Directory Listing
- Program: paragonie
- Disclosed At: 2017-05-20T21:53:04.349Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

STEP:
====================
1. goto https://bridge.cspr.ng/login and enter your username,password
2.  click "LogIn" and intercept the request
3.   change the value in cookie header and add '(single quote) in PHPSESSID field
      eg: PHPSESSID=kn7e21dpp2ocai2ckn1v147qev'
4.  Forward the packet and see full path is disclose
{F186342}

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
