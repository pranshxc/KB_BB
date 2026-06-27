---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '434689'
original_report_id: '434689'
title: Global defaming of any twitter user
weakness: Business Logic Errors
team_handle: x
created_at: '2018-11-06T05:11:12.639Z'
disclosed_at: '2018-12-06T23:43:48.668Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Global defaming of any twitter user

## Metadata

- HackerOne Report ID: 434689
- Weakness: Business Logic Errors
- Program: x
- Disclosed At: 2018-12-06T23:43:48.668Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Private tweets can be used to keep any user's tweet secret from rest of twitter world. Once the user changes his setting from private tweets to public tweets, all his secret tweets become visible. This can become a major issue causing global distributed attacks

**Steps to Reproduce**

1. Assume the attacker is targeting certain president XYZ for the next election
2. Attacker goes to settings and enable private tweet
3. Attacker find famous tweets from 10000+ celebrity profiles
4. Attacker replies on all those 10000+ celebrity profile tweets mentioning "XYZ is the worst candidate. See what he did <some video or something>"
5. None of the twitter user can see that reply from Attacker since it is a private tweet
6. Once the elections are really near, Attacker changes his setting from private to public tweet
7. Attacker reply comments are now visible in all those 10000+ celebrity profile famous tweets
8. This can cause mass defaming, before twitter could actually intervene and remove attacker

## Impact

This can be used to defame any famous celebrity on a mass level

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
