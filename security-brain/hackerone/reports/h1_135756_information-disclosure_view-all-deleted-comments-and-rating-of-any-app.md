---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135756'
original_report_id: '135756'
title: View all deleted comments and rating of any app .
weakness: Information Disclosure
team_handle: shopify
created_at: '2016-05-02T11:19:21.779Z'
disclosed_at: '2016-09-01T06:10:03.218Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# View all deleted comments and rating of any app .

## Metadata

- HackerOne Report ID: 135756
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2016-09-01T06:10:03.218Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi ,
Deleted comments and rating of any app can be viewed by following url -

https://apps.shopify.com/<app>/reviews/<review-id>/edit

for example review with review id 47935 is deleted but still can be view by following link -
https://apps.shopify.com/swell/reviews/47935/edit 

As review id is incremental id so all reveiw of app can be collected easily.

It is not a big issue but deleted comment should not be allowed to view . Please let me know what you think about this .
Thanks

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
