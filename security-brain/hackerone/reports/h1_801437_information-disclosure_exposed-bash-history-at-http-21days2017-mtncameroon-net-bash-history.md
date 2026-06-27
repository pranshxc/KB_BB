---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '801437'
original_report_id: '801437'
title: Exposed .bash_history at http://21days2017.mtncameroon.net/.bash_history
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2020-02-21T06:19:28.491Z'
disclosed_at: '2022-03-20T05:31:11.037Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: mtncameroon.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Exposed .bash_history at http://21days2017.mtncameroon.net/.bash_history

## Metadata

- HackerOne Report ID: 801437
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2022-03-20T05:31:11.037Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Dear Security Team,

I found some dangerous urls on your servers that reveal important informations about the servers configuration themself and that are very interesting from a hacker point of view.

## Steps To Reproduce:
http://21days2017.mtncameroon.net/.bash_history

##Remediation

*  disable that kind of function on production server
*  protect them with strong credentials
*   use ip restriction

Best regards,
Vishu10x00 ❤️

## Impact

While this does not represent a real security issue, this reveal important informations about your system and could be used by a malicious user for a future attack.

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
