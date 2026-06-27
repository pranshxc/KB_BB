---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223344'
original_report_id: '223344'
title: CSV Injection with the CSV export feature
weakness: OS Command Injection
team_handle: weblate
created_at: '2017-04-24T09:43:51.956Z'
disclosed_at: '2017-05-17T18:03:47.076Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- os-command-injection
---

# CSV Injection with the CSV export feature

## Metadata

- HackerOne Report ID: 223344
- Weakness: OS Command Injection
- Program: weblate
- Disclosed At: 2017-05-17T18:03:47.076Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Step to reproduce :**
1.go to https://hosted.weblate.org/dictionaries/aptoide-uploader/bn/#add
2.add "=1+1" to **Source** and ** Translation** filed 
{F178723}
3.now do **CSV export**
4.you can see all the cell is displayed as "2" which means the code is executed.

Best Regad's,
Jay Patel

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
