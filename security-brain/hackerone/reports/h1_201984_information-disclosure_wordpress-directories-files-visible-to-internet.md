---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201984'
original_report_id: '201984'
title: Wordpress directories/files visible to internet
weakness: Information Disclosure
team_handle: ui
created_at: '2017-01-29T19:08:17.181Z'
disclosed_at: '2017-03-08T14:13:46.151Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- information-disclosure
---

# Wordpress directories/files visible to internet

## Metadata

- HackerOne Report ID: 201984
- Weakness: Information Disclosure
- Program: ui
- Disclosed At: 2017-03-08T14:13:46.151Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Issue
During my testing I noticed that ubnt website `https://directory.corp.ubnt.com` seems to leak some data into internet. Wordpress directory `https://directory.corp.ubnt.com/wp-content/uploads/` is showing files which I suppose shouldn't be visible to internet. 

I noticed that these files include UBNT-employee email addresses (including personal?), pictures etc.

#Reproduction
Just open URL https://directory.corp.ubnt.com/wp-content/uploads/ and start browsing folders/files.
Most "juicy" stuff can be seen in these folders: ██████████

BR,
-Tomi

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
