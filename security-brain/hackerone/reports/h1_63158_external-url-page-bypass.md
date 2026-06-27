---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '63158'
original_report_id: '63158'
title: External URL page bypass
team_handle: security
created_at: '2015-05-20T21:58:06.883Z'
disclosed_at: '2015-05-28T08:36:19.194Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# External URL page bypass

## Metadata

- HackerOne Report ID: 63158
- Weakness: 
- Program: security
- Disclosed At: 2015-05-28T08:36:19.194Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A specially crafted URL can bypass the external URL warning page.

# Details

A url that starts with two forward slashes is treated as absolute by browsers.  The markdown renderer refuses to render links that start like this, however it can be tricked by using a control character e.g.

"[test](/\x08/evil.com)"

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
