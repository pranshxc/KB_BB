---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1882592'
original_report_id: '1882592'
title: Reflected XSS in ████████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2023-02-22T07:35:42.122Z'
disclosed_at: '2023-04-14T17:26:48.340Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in ████████████

## Metadata

- HackerOne Report ID: 1882592
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-04-14T17:26:48.340Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
XSS vulnerability found on one of `███████` subdomains. [ DoD scope]

After analyzing `https://████████████/` (national levee database) I found  `auth/logout.jsx` page that have `home` parameter in `GET` request.  `home` parameter vulnerable to XSS vulnerability.


Payload:
`https://█████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()`
████████


## References
https://owasp.org/www-community/attacks/xss/

## Impact

By exploiting this vulnerability an attacker can trick the users to execute XSS and steal user's cookies.
Launch advanced phishing attacks.
Execute browser-based attacks etc.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit the following URL 
`https://████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()`

* click on `Click here to return to your application.`  and you will receive `XSS Success!` alert box.

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
