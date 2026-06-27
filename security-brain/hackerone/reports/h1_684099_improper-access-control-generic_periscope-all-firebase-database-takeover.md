---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '684099'
original_report_id: '684099'
title: Periscope-all Firebase database takeover
weakness: Improper Access Control - Generic
team_handle: x
created_at: '2019-08-29T03:22:26.687Z'
disclosed_at: '2019-09-25T22:01:29.016Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: '*.periscope.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# Periscope-all Firebase database takeover

## Metadata

- HackerOne Report ID: 684099
- Weakness: Improper Access Control - Generic
- Program: x
- Disclosed At: 2019-09-25T22:01:29.016Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found one public Firebase database of periscope.tv and I can able to insert data to this database and i only used it once for the testing purposes, so other database queries also possible.

Please follow the below link to check the inserted test data.

###Periscope-all Firebase URL :- 

https://█████████/.json

## Impact

This is quite serious because by using this database attacker can use this for malicious purposes and also an attacker can track this database if periscope uses it for future perspective and at that time it will be much easier for the attacker to steal the data from this repository and later it will harm the reputation of the Periscope.

So please immediately change the rule of the database to private so that nobody can able to access it outside.

Thanks
Deeptiman Pattnaik

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
