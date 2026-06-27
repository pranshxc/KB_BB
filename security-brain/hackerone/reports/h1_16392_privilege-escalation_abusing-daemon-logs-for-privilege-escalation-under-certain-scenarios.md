---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '16392'
original_report_id: '16392'
title: Abusing daemon logs for Privilege escalation under certain scenarios
weakness: Privilege Escalation
team_handle: phabricator
created_at: '2014-06-14T03:09:35.523Z'
disclosed_at: '2014-06-18T13:44:53.500Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Abusing daemon logs for Privilege escalation under certain scenarios

## Metadata

- HackerOne Report ID: 16392
- Weakness: Privilege Escalation
- Program: phabricator
- Disclosed At: 2014-06-18T13:44:53.500Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Setup Needed

+ A normal user account
+ A momentary disruption of mail services

# Replication steps

+ Login as **normal user**
+ Wait for **momentary disruption** of mail services
+ Use **Password Reset Link** for admin mail address
+ BOOM!!!
+ You can see the password reset link in the daemon logs because of interrupted mail service (check the screenshot)
+ Click on the link and upgrade to **Admin**

# Attack Scenarios

(Virtually unlimited) 
A moment misconfiguration of 
+ Mail configuration
+ Firewall settings
+ Mail Service down
etc.. etc.. (we just need a moment :P)

I actually discovered this bug when gmail rejected my smtp credentials to prevent suspicious login :P.

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
