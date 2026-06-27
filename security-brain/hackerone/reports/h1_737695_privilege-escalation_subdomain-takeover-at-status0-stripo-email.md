---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737695'
original_report_id: '737695'
title: subdomain takeover at status0.stripo.email
weakness: Privilege Escalation
team_handle: stripo
created_at: '2019-11-14T19:57:06.931Z'
disclosed_at: '2019-12-23T09:03:35.899Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 36
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- privilege-escalation
---

# subdomain takeover at status0.stripo.email

## Metadata

- HackerOne Report ID: 737695
- Weakness: Privilege Escalation
- Program: stripo
- Disclosed At: 2019-12-23T09:03:35.899Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi ,

The subdomain status0.stripo.email was pointed at uptimerobot.com
whereas it was not being used , but having Cname record as stats.uptimerobot.com .
Hence anyone can takeover it.

I have parked it with atest account on uptimerobot.com

{F634639}

{F634636}

thanks

## Impact

Anyone can use this subdomain on uptimerobot.com with a false message.

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
