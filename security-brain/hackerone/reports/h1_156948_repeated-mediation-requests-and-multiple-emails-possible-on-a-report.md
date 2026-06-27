---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156948'
original_report_id: '156948'
title: Repeated mediation requests and multiple emails possible on a report.
team_handle: security
created_at: '2016-08-05T19:23:10.331Z'
disclosed_at: '2019-04-11T01:39:49.105Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Repeated mediation requests and multiple emails possible on a report.

## Metadata

- HackerOne Report ID: 156948
- Weakness: 
- Program: security
- Disclosed At: 2019-04-11T01:39:49.105Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

1) We can by pass used buttom Confirm on Request Mediation from HackerOne where is disable him

POC:
Edit html and delete disabled=""
<input type="submit" data-reactid=".8.0.1.0.6.1" disabled="" class="button button--success button--modal pull-right" value="Confirm">

<input type="submit" data-reactid=".8.0.1.0.6.1"  class="button button--success button--modal pull-right" value="Confirm">

And buttom in active.

2) Next catch request
https://hackerone.com/reports/nubmerreport/hacker_help
POST:
message=&mediation_type=resolution

If parametr message null , we can send multiple requests.  And spamming support
But if message is no null we have 404

PS Yes you page is write
Spamming other users with automated HackerOne emails or notifications (e.g. abusing the forgot password form).
But this problem is multiple requests.

thx,, sorry bad eng.

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
