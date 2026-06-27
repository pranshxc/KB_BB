---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1267380'
original_report_id: '1267380'
title: Reflected XSS on [█████████]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-07-18T12:41:02.157Z'
disclosed_at: '2022-04-07T20:09:29.406Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on [█████████]

## Metadata

- HackerOne Report ID: 1267380
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T20:09:29.406Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi security team members,

I found a reflected XSS on the URL

## Impact

1. An attacker can steal the victim's cookies.
2. An attacker can execute JS code.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to this link:- https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E
2. Then, it will execute.

## Suggested Mitigation/Remediation Actions

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
