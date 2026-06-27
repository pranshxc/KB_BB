---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2063636'
original_report_id: '2063636'
title: Twitter Subscriptions Information Disclosure
weakness: Information Disclosure
team_handle: x
created_at: '2023-07-11T15:56:49.118Z'
disclosed_at: '2023-09-18T19:33:19.959Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Twitter Subscriptions Information Disclosure

## Metadata

- HackerOne Report ID: 2063636
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2023-09-18T19:33:19.959Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

Hi team,
I was scrolling on Twitter connected from US location, and a Tweet appeared on my timeline; I couldn't see the tweet because it is only visible to subscribers. However I was able to extract the images from that tweet even though I'm not a subscriber

**Description:**

A subscriber only tweet of MrBeast appeared on my timeline (which i can't see)
{F2487967}

Clicking on the quotes button revealed the images and the tweet content which should be invisible to me.

**Steps To Reproduce:**

  1.  Go to https://twitter.com/MrBeast/status/1678121172196630531
  1. Ensure that you are not a subscriber therefore cannot see the tweet
  1. Click on quotes button and see the tweet and images

## Supporting Material/References:

POC video:
████

## Impact

Information disclosure

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
