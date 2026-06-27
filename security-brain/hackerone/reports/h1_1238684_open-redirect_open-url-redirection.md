---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1238684'
original_report_id: '1238684'
title: Open URL Redirection
weakness: Open Redirect
team_handle: unikrn
created_at: '2021-06-20T10:38:01.056Z'
disclosed_at: '2021-06-28T10:03:31.304Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 100
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open URL Redirection

## Metadata

- HackerOne Report ID: 1238684
- Weakness: Open Redirect
- Program: unikrn
- Disclosed At: 2021-06-28T10:03:31.304Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Open URL Redirect  

Steps To Reproduce:
1) Go to the following link & Register for new account https://unikrn.com/██████
2) After registering It will redirect to example.com


Reference: https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet

## Impact

The attacker can force the user to install trojans, malwares, etc. into his system.
And also can steal cookies, conduct phishing attacks.

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
