---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '459532'
original_report_id: '459532'
title: Persistent CSV injection
team_handle: semrush
created_at: '2018-12-10T09:56:23.899Z'
disclosed_at: '2019-01-11T13:39:33.860Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Persistent CSV injection

## Metadata

- HackerOne Report ID: 459532
- Weakness: 
- Program: semrush
- Disclosed At: 2019-01-11T13:39:33.860Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Team,

https://www.semrush.com/notes is vulnerable to persistent csv injection (stored csv injection) 

POC:
1) Login into application and open https://www.semrush.com/notes

2) click on "Add note" button

3) And enter csv injection payloads like =4+4, =HYPERLINK("http://evil.com", "EVIL") and click on save

4) and click on "Export to CSV"

5) Open the downloaded csv file

6) Observe the payload you entered in the above step


Reference:
https://payatu.com/csv-injection-basic-to-exploit/

## Impact

Attacker can execute kernel/OS level commands from victims machine.

As it is stored at database, so users across SEMrush who ever downloads that csv file will be victims for the attacker.

Also attacker can use victims to perform DDOS attack from victims machines.

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
