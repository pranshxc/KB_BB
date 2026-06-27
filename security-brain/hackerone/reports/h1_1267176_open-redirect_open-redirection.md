---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1267176'
original_report_id: '1267176'
title: Open Redirection
weakness: Open Redirect
team_handle: jetblue
created_at: '2021-07-17T23:33:10.286Z'
disclosed_at: '2023-02-05T13:00:27.505Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: movil.jetblue.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirection

## Metadata

- HackerOne Report ID: 1267176
- Weakness: Open Redirect
- Program: jetblue
- Disclosed At: 2023-02-05T13:00:27.505Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi jetblue Security Team.

The following URL is vulnerable to an open redirect (it will redirect to google.com):
- https://█████_https@google.com

Work at Google Chrome & Other Browser 
Except Firefox will ask you first if you want to redirect to that page , See:-

█████████
  
##What is Open Redirect:-
Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behavior can be leveraged to facilitate phishing attacks against users of the application. The ability to use an authentic application URL

Supporting Material/References:
-https://blog.detectify.com/2019/05/16/the-real-impact-of-an-open-redirect/
-https://medium.com/@0xrishabh/open-redirect-to-account-takeover-e939006a9f24

## Steps To Reproduce:
1. Go to  https://████_https@google.com
2. Redirect to google.com

## Impact

Open Redirection

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
