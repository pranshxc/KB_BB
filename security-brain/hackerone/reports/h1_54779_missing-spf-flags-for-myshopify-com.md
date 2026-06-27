---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54779'
original_report_id: '54779'
title: Missing spf flags for myshopify.com
team_handle: shopify
created_at: '2015-04-03T22:16:30.301Z'
disclosed_at: '2015-04-16T10:35:32.194Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Missing spf flags for myshopify.com

## Metadata

- HackerOne Report ID: 54779
- Weakness: 
- Program: shopify
- Disclosed At: 2015-04-16T10:35:32.194Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello guys

I just checked for SPF records for the **myshopify.com** domain, and there are none, effectively allowing for spam to originate from that domain. you can validate by testing yourself here: http://www.kitterman.com/spf/validate.html

The SPF records are correctly set for shopify.com so i guess myshopify was overlooked?

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
