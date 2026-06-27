---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '426547'
original_report_id: '426547'
title: Missing Rate Limitation at /photo_videos/photoset/create
weakness: Business Logic Errors
team_handle: chaturbate
created_at: '2018-10-21T20:00:27.961Z'
disclosed_at: '2018-11-24T23:09:33.537Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Missing Rate Limitation at /photo_videos/photoset/create

## Metadata

- HackerOne Report ID: 426547
- Weakness: Business Logic Errors
- Program: chaturbate
- Disclosed At: 2018-11-24T23:09:33.537Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,I discovered that one is able to create an unlimited number of albums Via /photo_videos/photoset/create/
Steps To Reproduce:
1.Login And Go to http://fr.chaturbate.co /photo_videos/photoset/create/
2.Fill the form
3.Enable a proxy interception tool (e.g Burp Suite)
4.Click Save
5.Send the POST request made to /photo_videos/photoset/create to intruder
6.Set 500 or more custom inputs and Start attack

I've been able to create many albums without restrictions

Reference:
F364058

## Impact

Create an unlimited number of albums

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
