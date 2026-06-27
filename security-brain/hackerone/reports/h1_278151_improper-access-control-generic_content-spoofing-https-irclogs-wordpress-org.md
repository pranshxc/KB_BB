---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '278151'
original_report_id: '278151'
title: Content Spoofing @ https://irclogs.wordpress.org/
weakness: Improper Access Control - Generic
team_handle: wordpress
created_at: '2017-10-17T09:11:43.631Z'
disclosed_at: '2017-12-04T08:02:35.589Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- improper-access-control-generic
---

# Content Spoofing @ https://irclogs.wordpress.org/

## Metadata

- HackerOne Report ID: 278151
- Weakness: Improper Access Control - Generic
- Program: wordpress
- Disclosed At: 2017-12-04T08:02:35.589Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Greetings,

Today I was Free So I Decided to Do Pentest WordPress So i Found a SubDomain which is Vulnerable to Plain text Content Spoofing.

PoC:-
Url:-
https://irclogs.wordpress.org/chanlog.php?channel=wordpress&day=[Message Goes Here]&sort=asca
Example:-
https://irclogs.wordpress.org/chanlog.php?channel=wordpress&day=today%20is%20not%20found%20because%20Wordpress%20Is%20Currently%20Down%20Kindly%20Visit%20Phishing.com%20and%20Login%20with%20Your%20Account%20For%20Further%20Details.%20Regards,%20Wordpress%20Team.&sort=asca

Thanks,
Abdulwahab Khan,
Independent Cyber Security Researcher

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
