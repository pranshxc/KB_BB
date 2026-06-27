---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '121382'
original_report_id: '121382'
title: doc.owncloud.org has missing PHP handler
weakness: Information Disclosure
team_handle: owncloud
created_at: '2016-03-08T16:55:06.069Z'
disclosed_at: '2016-04-04T13:22:15.711Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# doc.owncloud.org has missing PHP handler

## Metadata

- HackerOne Report ID: 121382
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2016-04-04T13:22:15.711Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When visiting the following URL
https://doc.owncloud.org/server/8.2/go.php?to=admin-backup
the web server does interpret the php code but delivers the php code itself.
This might expose internal information to anyone visiting the website.

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
