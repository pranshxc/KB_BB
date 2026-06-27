---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '481654'
original_report_id: '481654'
title: No Rate On Add Suggest
weakness: Concurrent Execution using Shared Resource with Improper Synchronization
  ('Race Condition')
team_handle: weblate
created_at: '2019-01-17T23:13:57.902Z'
disclosed_at: '2019-01-22T13:59:29.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- concurrent-execution-using-shared-resource-with-improper-synchronization-race-condition
---

# No Rate On Add Suggest

## Metadata

- HackerOne Report ID: 481654
- Weakness: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
- Program: weblate
- Disclosed At: 2019-01-22T13:59:29.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Hello
###Description : 
####I have found that there is no limit in the number of requests in place of adding suggest, which may exploit the vulnerability of the attacker to send a large number of suggestions, for example, send a million suggest may lead to cause a problem to the server

###Steps To Reproduce : 
####1. Go To https://hosted.weblate.org/translate/andors-trail/game-content/ar/?checksum=c4ddb61773f5e641#suggestions add And Fill in fields
####2.Click On Add
####3.And intercept The Request With Proxy ( Burp )
####4.And Send The Request To Inturder
####5.And Go to Payloads and Select In The Payload type > Numbers ...
####6.Click On Start Attack
###POC : 
{F408287}
{F408288}

###Remediation : 
####1. limit the functionality to x attempts in a predefined period before blocking the account 
####2. set up a captcha to prevent robots

## Impact

####An attacker could cause a problem for the server

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
