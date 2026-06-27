---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '75936'
original_report_id: '75936'
title: Security Missconfiguration in Autologin
weakness: Cryptographic Issues - Generic
team_handle: zendesk
created_at: '2015-07-16T10:42:02.128Z'
disclosed_at: '2015-08-14T23:33:44.758Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Security Missconfiguration in Autologin

## Metadata

- HackerOne Report ID: 75936
- Weakness: Cryptographic Issues - Generic
- Program: zendesk
- Disclosed At: 2015-08-14T23:33:44.758Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Here  I am addressing Critical misconfiguration in autologin feature 
1. Open the link in the browser https://dashboard.zopim.com/#home and enter your username and password and don't tick (select) the option Always sign in automatically  and login 
2. now logout from your account 
3. now you logged out again reload the page https://dashboard.zopim.com/#home and you will be logged in
here the user does not selected the autologin option but still he./she logged in automatically

attack scenario
lets a user is using his account on local computer so he doesnot selected the autologin option while login 
then his work finished and signout and left after that any one can reload the link and login his/her account 

Regards
Dipak

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
