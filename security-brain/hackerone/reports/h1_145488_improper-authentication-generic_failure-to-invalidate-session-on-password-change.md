---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145488'
original_report_id: '145488'
title: failure to invalidate session on password change
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-17T17:44:59.869Z'
disclosed_at: '2017-04-20T15:09:39.387Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# failure to invalidate session on password change

## Metadata

- HackerOne Report ID: 145488
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2017-04-20T15:09:39.387Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Steps to reproduce
1. Login as user1 in firefox browser
2. Go to http://localhost/nextcloud/index.php/settings/personal
3. Go to other browser (chrome) and login as user1
4. Change the password in chrome 

Observe that the session in firefox still works

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
