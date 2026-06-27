---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151772'
original_report_id: '151772'
title: Directory Listening
weakness: Information Disclosure
team_handle: gocd
created_at: '2016-07-16T15:51:31.651Z'
disclosed_at: '2016-09-14T15:07:28.460Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Directory Listening

## Metadata

- HackerOne Report ID: 151772
- Weakness: Information Disclosure
- Program: gocd
- Disclosed At: 2016-09-14T15:07:28.460Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

Found Directory Listening :

http://IP:8153/go/NOTICE/

{F105317}


There is not usually any good reason to provide directory listings, and disabling them may place additional hurdles in the path of an attacker. This can normally be achieved in two ways:
Configure your web server to prevent directory listings for all paths beneath the web root;
Place into each directory a default file (such as index.htm) that the web server will display instead of returning a directory listing.

Thanks!

Best,
Arbaz

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
