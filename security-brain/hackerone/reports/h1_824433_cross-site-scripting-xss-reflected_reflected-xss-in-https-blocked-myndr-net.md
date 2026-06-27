---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '824433'
original_report_id: '824433'
title: Reflected XSS in https://blocked.myndr.net
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: myndr
created_at: '2020-03-19T09:22:27.529Z'
disclosed_at: '2020-03-19T15:44:45.933Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 44
asset_identifier: '*.myndr.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://blocked.myndr.net

## Metadata

- HackerOne Report ID: 824433
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: myndr
- Disclosed At: 2020-03-19T15:44:45.933Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
Reflected XSS in Domain (https://blocked.myndr.net)

## Steps To Reproduce:
1. Go to the https://blocked.myndr.net.
2. Find the endpoint in the domain -https://blocked.myndr.net/?trg=1
3. Add the payload ?trg="><script>alert(1)</script>
4. You can see the pop up in your browser.

## Impact

With the help of XSS, a hacker or attacker can perform social engineering on users by redirecting them from real websites to fake ones. the hacker can steal their cookies and download malware on their system, and there are many more attacking scenarios a skilled attacker can perform with XSS.

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
