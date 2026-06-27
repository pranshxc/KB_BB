---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361287'
original_report_id: '361287'
title: DOMXSS in redirect param
weakness: Cross-site Scripting (XSS) - DOM
team_handle: semmle
created_at: '2018-06-03T10:03:13.734Z'
disclosed_at: '2019-03-20T12:34:50.453Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 81
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOMXSS in redirect param

## Metadata

- HackerOne Report ID: 361287
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: semmle
- Disclosed At: 2019-03-20T12:34:50.453Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Summary
The **redirect** param can consist of a ``javascript:`` url, which results in XSS. If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.

#Steps to reproduce
1) Logout
2) Visit `` https://lgtm-com.pentesting.semmle.net/?redirect=javascript:prompt(document.domain)%2f%2f
 ``
3) Log in through email

## Impact

If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.

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
