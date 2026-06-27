---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145430'
original_report_id: '145430'
title: 'help.nextcloud.com: Session Management Issue'
team_handle: nextcloud
created_at: '2016-06-17T15:05:49.816Z'
disclosed_at: '2016-06-17T19:10:22.617Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
---

# help.nextcloud.com: Session Management Issue

## Metadata

- HackerOne Report ID: 145430
- Weakness: 
- Program: nextcloud
- Disclosed At: 2016-06-17T19:10:22.617Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey, I've found a session management in help.nextcloud.com, which can lead to session takeover!
Issue:
========
When the password of an account is changed from a session, other sessions doesn't expire!

Steps to Reproduce:
--------------
[+] We need to use two different browsers.

Login to both browsers!

1. Then change the password from one browser.
2. After changing the password, go to other browser, the session will still be alive
3. That means, server-side session not expire after password change.
4. This could be a risky factor for the user.

Thanks,
Ahsan Tahir

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
