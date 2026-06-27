---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42154'
original_report_id: '42154'
title: Gain access to any user's email address
weakness: Information Disclosure
team_handle: nearby
created_at: '2014-12-30T07:32:02.119Z'
disclosed_at: '2015-03-14T06:57:35.057Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Gain access to any user's email address

## Metadata

- HackerOne Report ID: 42154
- Weakness: Information Disclosure
- Program: nearby
- Disclosed At: 2015-03-14T06:57:35.057Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker can gain access to any user's email address by accessing the /points/buy page. This is a serious issue because the email address is used as one of the login credentials for the website.

Steps to reproduce : 
1. Go to https://www.wnmlive.com/account/points
2. Select "Get more points"
    + You should now be at https://www.wnmlive.com/points/buy/ [YOUR PID]
3. Change the PID portion for the PID of any other user.
    + You now see the email address of that user.

This is the PID of my test account : Cqx3vGgl4RD3NNIBqeJtrg.
 You will see the email c2576767@trbvm.com instead of your own email account.

The best solution would be to use the UID stored in the cookie files rather than using the PID in the URL.

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
