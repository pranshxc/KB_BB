---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '380158'
original_report_id: '380158'
title: svcardproxydevus.starbucks.com Subdomain take over
weakness: Improper Access Control - Generic
team_handle: starbucks
created_at: '2018-07-10T13:14:17.255Z'
disclosed_at: '2018-07-23T17:47:15.343Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- improper-access-control-generic
---

# svcardproxydevus.starbucks.com Subdomain take over

## Metadata

- HackerOne Report ID: 380158
- Weakness: Improper Access Control - Generic
- Program: starbucks
- Disclosed At: 2018-07-23T17:47:15.343Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

You have left a dns record pointing to a dead cloudapp vm.

```
svcardproxydevus.starbucks.com -> s00307ntmp0svcardproxydev0.trafficmanager.net -> s00307dpipsvcardproxy00.eastus.cloudapp.azure.com = Dead
```

## Impact

```
1) Attacker takes over subdomain and then puts something like porn or something that shouldn't be on the domain.
2) hacker then contacts support pretending to be a concerned user.
3) support click on it to check what is going on
4) attacker has put responder on the page via a image file using a UNC path (https://github.com/SpiderLabs/Responder)
5) attacker is then sent supports hash for their windows login.
6) attacker then cracks hash and uses the VPN to pivot 
```

They can also use it to phish and other bad activitys

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
