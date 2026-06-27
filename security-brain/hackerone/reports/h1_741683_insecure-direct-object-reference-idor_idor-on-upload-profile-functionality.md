---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '741683'
original_report_id: '741683'
title: idor on upload profile functionality
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2019-11-20T08:50:00.444Z'
disclosed_at: '2020-05-14T17:12:54.195Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# idor on upload profile functionality

## Metadata

- HackerOne Report ID: 741683
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2020-05-14T17:12:54.195Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable URL: https://██████████/███████ID/#Common/EditOne/Person/{account_id}
steps to reproduce:
1).browse the image and click on the upload button
2).capture this request in burp suite 
3). change the value 'personId' parameter to account2 account_id 
(please see screenshot1)
4).then goes to account2, then you will see the uploaded image is successfully goes to the approved tab 

please see video attach below you will understand completely

## Impact

an attacker is able to change profile image of any user

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
