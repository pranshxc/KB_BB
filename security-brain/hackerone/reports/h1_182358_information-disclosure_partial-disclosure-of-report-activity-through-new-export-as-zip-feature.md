---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '182358'
original_report_id: '182358'
title: Partial disclosure of report activity through new "Export as .zip" feature
weakness: Information Disclosure
team_handle: security
created_at: '2016-11-15T20:35:30.442Z'
disclosed_at: '2016-11-29T01:51:51.404Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 339
tags:
- hackerone
- information-disclosure
---

# Partial disclosure of report activity through new "Export as .zip" feature

## Metadata

- HackerOne Report ID: 182358
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-11-29T01:51:51.404Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
I noticed a new feature has been launched, which allows to export report. Great feature.
But unfortunately it discloses comments of partially disclosed reports which supposed to be hidden..

###POC:
* Go to this partially disclosed report > https://hackerone.com/reports/██████████
* Click **Export** Button.
* You'll see comments are getting disclosed!

{F134909}

This way you can see all the partially disclosed reports comments.

Please let me know if you need more information!

Looking forward!

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
