---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137404'
original_report_id: '137404'
title: List of a ton of internal twitter servers available on GitHub
weakness: Information Disclosure
team_handle: x
created_at: '2016-05-10T04:25:19.405Z'
disclosed_at: '2016-10-17T18:32:15.798Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# List of a ton of internal twitter servers available on GitHub

## Metadata

- HackerOne Report ID: 137404
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2016-10-17T18:32:15.798Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The page at https://raw.githubusercontent.com/adi2909/basic-py/0532539f86cbb584aa7bfd8cc357fc9df4c25c03/data/allHostInfo.json

has a ton of internal info about twitter hosts, including MACs, NICs, other hardware info, and hostnames.  This data, albeit a little dated, gives an attacker an excellent view into hardware, patching status, and network topology.

I've uploaded a parsed JSON of this information

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
