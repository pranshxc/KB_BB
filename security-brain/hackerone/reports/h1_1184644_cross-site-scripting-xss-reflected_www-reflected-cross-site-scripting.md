---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1184644'
original_report_id: '1184644'
title: '[www.███] Reflected Cross-Site Scripting'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-05-05T11:09:59.543Z'
disclosed_at: '2021-06-30T20:42:52.577Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [www.███] Reflected Cross-Site Scripting

## Metadata

- HackerOne Report ID: 1184644
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-30T20:42:52.577Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Good morning, there's a reflected cross-site scripting vulnerability on https://www.██████████/█████
There was some difficult in making a payload for this vulnerability, mainly due to the WAF blocking some vectors; But exploitation is still possible.
Here's a proof of concept showing an alert popup.
https://www.████/███████?██████=-20a")});a=alert;a(1);//
## References

## Impact

A reflected cross-site scripting vulnerability can allow common client-side attacks.

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Open the following URL: https://www.███/█████?█████=-20a")});a=alert;a(1);//
2. An alert box should pop-up, indicating the presence of the vulnerability.

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
