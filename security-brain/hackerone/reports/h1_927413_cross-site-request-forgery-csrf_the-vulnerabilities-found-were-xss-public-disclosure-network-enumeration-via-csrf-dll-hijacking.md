---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '927413'
original_report_id: '927413'
title: The vulnerabilities found were XSS, Public disclosure, Network enumeration
  via CSRF, DLL hijacking.
weakness: Cross-Site Request Forgery (CSRF)
team_handle: zomato
created_at: '2020-07-19T16:36:54.858Z'
disclosed_at: '2020-07-21T16:30:17.762Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 10
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# The vulnerabilities found were XSS, Public disclosure, Network enumeration via CSRF, DLL hijacking.

## Metadata

- HackerOne Report ID: 927413
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: zomato
- Disclosed At: 2020-07-21T16:30:17.762Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Summary
IP found using ping command- 52.77.124.190 Then I used nmap tool to find the indepth information. I used burp suite and DNS scanner but it was not fruitful. Then I
explored some GitHub repositories to perform thorough web-application testing. Using
Aquatone I found some hidden domains. The results of Maltego tool and Aquatone
differed a lot. The vulnerabilities found were XSS, Public disclosure, Network
enumeration via CSRF, DLL hijacking.

**Platform(s) Affected:** Website

Details:
1. We found a domain which compiles on auth.zomato.com which is running 443
TCP as is well understood that 443 is for SSH and it is brute forcible on the IP
address
2. The next utility which I used is gitSploit. It is basically is used to find the
vulnerability and I found around 10 of them, the category varies from low to
critical.

## Impact

Information Disclosure, Server Can be Hijacked although it is not updated

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
