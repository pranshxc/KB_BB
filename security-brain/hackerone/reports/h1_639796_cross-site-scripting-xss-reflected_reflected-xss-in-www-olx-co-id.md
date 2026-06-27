---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '639796'
original_report_id: '639796'
title: Reflected XSS in www.olx.co.id
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-07-10T19:57:20.935Z'
disclosed_at: '2019-09-19T09:26:47.164Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in www.olx.co.id

## Metadata

- HackerOne Report ID: 639796
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-09-19T09:26:47.164Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability :  Reflected XSS in www.olx.co.id
Steps to Reproduce :
1) Go to (https://www.olx.co.id/iklan/di-jual-t120ss-habis-kena-php-IDA4JSB.html?ad_type=OR).
2) Inject this payload ("><script>alert(1)<%2fscript>l43ax) in ad_type get parameter.
https://www.olx.co.id/iklan/di-jual-t120ss-habis-kena-php-IDA4JSB.html?ad_type=ORrxhtm%22%3E%3Cscript%3Ealert(1)%3C%2fscript%3El43ax
3) Then see the response in browser and constantly three popup will appear.

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

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
