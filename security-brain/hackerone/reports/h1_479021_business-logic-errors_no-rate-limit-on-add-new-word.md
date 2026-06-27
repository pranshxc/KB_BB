---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '479021'
original_report_id: '479021'
title: No Rate Limit  On Add new word
weakness: Business Logic Errors
team_handle: weblate
created_at: '2019-01-13T22:57:47.318Z'
disclosed_at: '2019-01-14T19:24:41.313Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# No Rate Limit  On Add new word

## Metadata

- HackerOne Report ID: 479021
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2019-01-14T19:24:41.313Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

####Hello I found in that there is no limit in the place of adding a new word which allows the attacker to add an infinite number of words which may cause a problem in the site and the server

####Steps To Reproduce : 
##### 1. Go To https://hosted.weblate.org/dictionaries/andors-trail/en/#add And Fill in fields
##### 2.Click On Add
##### 3.And interceptThe Request With Proxy ( Burp )
##### 4.And Send The Request To Inturder
##### 5.And Go to Payloads and Select In The Payload type > Numbers ...
##### 6.Click On Start Attack

####POC : 
{F405705}
{F405706}

## Impact

#####An attacker could cause a problem for the server

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
