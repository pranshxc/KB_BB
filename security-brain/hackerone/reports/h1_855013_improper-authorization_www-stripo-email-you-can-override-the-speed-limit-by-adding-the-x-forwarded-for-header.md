---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '855013'
original_report_id: '855013'
title: '[www.stripo.email] You can override the speed limit by adding the X-Forwarded-For
  header.'
weakness: Improper Authorization
team_handle: stripo
created_at: '2020-04-21T12:41:29.813Z'
disclosed_at: '2020-04-23T08:44:00.659Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 34
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- improper-authorization
---

# [www.stripo.email] You can override the speed limit by adding the X-Forwarded-For header.

## Metadata

- HackerOne Report ID: 855013
- Weakness: Improper Authorization
- Program: stripo
- Disclosed At: 2020-04-23T08:44:00.659Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Summary
In *https://stripo.email/template-order* I think you have implemented rate limiting via 429 status code for too many requests, but in reality it is not. An attacker could bypass the 429 speed limit by adding an X-Forwarded-For header.

###Steps To Reproduce
1. Go to the *https://stripo.email/template-order* page
2. fill in the random content and Click the Order Template grab the packet.
3. Automate the request by adding the X-Forwarded-For header.

###Proof of Concept
The first photo bypasses the speed limit by adding an X-Forwarded-For header.
{F797676}

The second figure shows the 429 status code playing due to the speed limit if the X-Forwarded-For header is not added.
{F797677}

###Fix
Fix this bug by changing the way the server handles X-Forwarded-For headers

## Impact

Override speed limit

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
