---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '402658'
original_report_id: '402658'
title: XSS in request approvals
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2018-08-29T23:40:12.485Z'
disclosed_at: '2021-04-23T13:52:34.076Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 93
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in request approvals

## Metadata

- HackerOne Report ID: 402658
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2021-04-23T13:52:34.076Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, team!

I found xss.

Steps to reproduce:

1.  Open project settings
2.  paste in this field link777
{F339770}
3. click on result
{F339772}

In the username, a XSS poc should be written, like mine.

## Impact

XSS.

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
