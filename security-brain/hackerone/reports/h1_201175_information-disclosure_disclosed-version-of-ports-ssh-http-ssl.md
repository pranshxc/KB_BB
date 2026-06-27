---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201175'
original_report_id: '201175'
title: Disclosed Version of PORTS SSH|HTTP|SSL
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2018-05-27T13:57:25.961Z'
disclosed_at: '2018-06-14T14:41:15.737Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: scan.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosed Version of PORTS SSH|HTTP|SSL

## Metadata

- HackerOne Report ID: 201175
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2018-06-14T14:41:15.737Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

I found Version of ports are disclosed ,But the intersting that SSH port is open and showing his version 
==> OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
F:302383
Searching I have found that this version has common vulunrablitie
https://vuldb.com/?id.89622
So it's not good to disclose the version of this port(SSH) 
##Fix
make sure you have patched version or just by hiding his version

## Impact

Give an attacker the ability to make specific attack

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
