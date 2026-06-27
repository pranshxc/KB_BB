---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '684070'
original_report_id: '684070'
title: Authentication bypass and RCE on the https://████ due to exposed Cisco TelePresence
  SX80 with default credentials
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2019-08-29T01:13:11.963Z'
disclosed_at: '2021-01-12T21:55:36.855Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- improper-authentication-generic
---

# Authentication bypass and RCE on the https://████ due to exposed Cisco TelePresence SX80 with default credentials

## Metadata

- HackerOne Report ID: 684070
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:55:36.855Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I was able to identify Cisco TelePresence SX80 device located on the https://█████
According to the IP Info: https://ipinfo.io/████████it belongs to ASN with ID 
```
███████
```
so it's likely in scope of the program.
The mentioned instance has default credentials `████`

##POC
https://███████
Login with `█████████`
████
Since we are logged in as ███, we can completely control the device and all connections, and add our startup scripts via https://██████████/web/scripts

##Suggested fix
Change the credentials and likely you will need to reset the device

## Impact

Potential device compromise and code execution. This devices are used mainly for trainings, briefings, and demonstration rooms, as well as auditoriums, so attacker with full control of the device potentially can intercept the data (RCE potential is interesting, but ability to silently compromise the device and use it as backdoor can be much more harmful).

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
