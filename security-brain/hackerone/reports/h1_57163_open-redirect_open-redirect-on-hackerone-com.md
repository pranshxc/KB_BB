---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57163'
original_report_id: '57163'
title: Open-redirect on hackerone.com
weakness: Open Redirect
team_handle: security
created_at: '2015-04-18T10:50:57.996Z'
disclosed_at: '2015-04-23T15:38:54.773Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- open-redirect
---

# Open-redirect on hackerone.com

## Metadata

- HackerOne Report ID: 57163
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2015-04-23T15:38:54.773Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

I would like to report about open-redirect on hackerone.com

Here is the PoC that redirects to example.com IP address: https://hackerone.com/%2F1572395042

There is one more strange behavior in URL. For example:
https://hackerone.com//hackerone.com - works
https://hackerone.com//hackerone1.com - doesn't work

I will investigate it further and get back with details if I find something more.

Thanks!

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
