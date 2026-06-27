---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272272'
original_report_id: '272272'
title: Export vault feature is vulnerable to CSV injection
weakness: OS Command Injection
team_handle: bitwarden
created_at: '2017-09-27T03:28:10.139Z'
disclosed_at: '2017-09-28T07:58:09.848Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: vault.bitwarden.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# Export vault feature is vulnerable to CSV injection

## Metadata

- HackerOne Report ID: 272272
- Weakness: OS Command Injection
- Program: bitwarden
- Disclosed At: 2017-09-28T07:58:09.848Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello guys

I don't know if you care about this issue but it seems that the export feature in your https://vault.bitwarden.com/#/tools is vulnerable to CSV injection. If a CSV contains a malicious command it may have big impact

Even though there is a popup notification for users before opening the CSV but due to it is coming from bitwarden site. User might trust the CSV.

I provide a video demo to show how the issue was found
https://www.youtube.com/watch?v=Y8zmUZu9z4c

Attack
-------
If the data inside the CSV if from other users then this might be a big impact. attackers will insert malicious command.

Im using this excel command
@SUM(1+1)*cmd|' /C calc'!A0

Fix
---
Prefix =, +, - and @ symbols with a ' in issues when exporting them to a .csv file might do the tricks.


Referrence
------------
https://hackerone.com/reports/111192
https://hackerone.com/reports/216243

Cheers
Kenziy

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
