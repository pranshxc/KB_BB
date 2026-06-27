---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '416906'
original_report_id: '416906'
title: Missing Rate Limitation at /apps/upload_app/
weakness: Business Logic Errors
team_handle: chaturbate
created_at: '2018-10-01T14:11:18.837Z'
disclosed_at: '2018-10-07T10:52:01.487Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Missing Rate Limitation at /apps/upload_app/

## Metadata

- HackerOne Report ID: 416906
- Weakness: Business Logic Errors
- Program: chaturbate
- Disclosed At: 2018-10-07T10:52:01.487Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary##
I discovered that one is able to create **unlimited** number of apps via `/apps/upload_app/ `. 

**PS: I feel this is within the scope of your program and you want to know about it. If otherwise, I'll be happy to close this.**

## Steps To Reproduce:

  1. Login and go to https://chaturbate.com/apps/upload_app/
  1. Fill the form
  1. Enable a proxy interception tool (e.g Burp Suite)
  1. Click Save
  1. Send the `POST` request made to  `/apps/upload_app/` to intruder
  1. Set 100 or more custom inputs and Start attack
  1. I was able to create many apps without limitation and I've had to pause because of your policy on rate limits

## Supporting Material/References:
{F353746}

## Impact

Create unlimited apps

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
