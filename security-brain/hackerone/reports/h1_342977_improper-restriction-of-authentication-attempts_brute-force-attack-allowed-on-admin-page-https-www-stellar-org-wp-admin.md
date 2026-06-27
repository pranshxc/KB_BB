---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '342977'
original_report_id: '342977'
title: brute force attack allowed on admin page https://www.stellar.org/wp-admin/
weakness: Improper Restriction of Authentication Attempts
team_handle: stellar
created_at: '2018-04-25T03:08:06.911Z'
disclosed_at: '2020-02-23T16:21:28.604Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 16
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# brute force attack allowed on admin page https://www.stellar.org/wp-admin/

## Metadata

- HackerOne Report ID: 342977
- Weakness: Improper Restriction of Authentication Attempts
- Program: stellar
- Disclosed At: 2020-02-23T16:21:28.604Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi security team
-due to your bug bounty program , i found basic authentication method
-by doing many trials the server will response and will not block the logging process
- the attack can be automated by burp intruder till getting access to admin page
- in second screen the request is intercepted by burp proxy
F290121:

-in third anf forth screen i used burp intruder to automate  bruit force attack (i tried only 9 times to make POC)
F290122:
F290123:

## Impact

if the attack coleted , admin page is accessed

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
