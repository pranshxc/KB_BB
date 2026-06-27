---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273819'
original_report_id: '273819'
title: Content spoofing on
weakness: Violation of Secure Design Principles
team_handle: torproject
created_at: '2017-10-02T17:26:27.869Z'
disclosed_at: '2023-11-28T08:59:16.877Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content spoofing on

## Metadata

- HackerOne Report ID: 273819
- Weakness: Violation of Secure Design Principles
- Program: torproject
- Disclosed At: 2023-11-28T08:59:16.877Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Scenerio
An attacker can include any arbitrary text using specially crafted tor project url.
Reporting this but not sure if this is in scope (text injection not marked in exclusion list)
Kindly mark it as informative in case if it is out of scope.

Steps
1) Attacker distributed the below url by means of spamming or through his website
Go To-
https://www.torproject.org/index%20not%20found%20at%20this%20server!%20Server%20is%20currently%20on%20maintanance.%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20Please%20visit%20at.HTTP:/EVIL.ATTACKER.COM%20for%20latest%20updates.%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20Changes%20are%20in%20progress
2) Since the text came from official site so user believes and gets into attacker trap.

Best Regards
Aryan.

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
