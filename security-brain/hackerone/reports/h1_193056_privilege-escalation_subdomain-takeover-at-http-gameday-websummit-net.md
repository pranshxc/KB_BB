---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '193056'
original_report_id: '193056'
title: Subdomain Takeover at http://gameday.websummit.net
weakness: Privilege Escalation
team_handle: websummit
created_at: '2016-12-21T13:10:21.742Z'
disclosed_at: '2017-01-30T12:54:53.006Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover at http://gameday.websummit.net

## Metadata

- HackerOne Report ID: 193056
- Weakness: Privilege Escalation
- Program: websummit
- Disclosed At: 2017-01-30T12:54:53.006Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As i said in the title i found a subdomain takeover vulnerability on the url http://gameday.websummit.net
The url was trying to find a bucket that didn't exist from a probably forgotten dns entry that was at
gameday.websummit.net.s3-website-eu-west-1.amazonaws.com

So i created a bucket with the specified name and uploaded a poc.
POC in the pictures

For more infos please ask...

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
