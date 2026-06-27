---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1656380'
original_report_id: '1656380'
title: Reddit talk promotion offers don't expire, allowing users to accept them after
  being demoted
weakness: Insecure Direct Object Reference (IDOR)
team_handle: reddit
created_at: '2022-08-01T15:44:16.502Z'
disclosed_at: '2022-10-03T15:25:08.187Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Reddit talk promotion offers don't expire, allowing users to accept them after being demoted

## Metadata

- HackerOne Report ID: 1656380
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: reddit
- Disclosed At: 2022-10-03T15:25:08.187Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description: 

When promoting a user to a speaker/host, an offerId is created which can be accepted by the user. However, after accepting them the offerIds don't expire. This means that after the user is demoted back to a listener, they can still use the offerIds to go back to their previous promoted role.

## Steps To Reproduce:

1. Have 2 accounts ready UserAVictim and UserBAttacker.
2. Create a new reddit talk as UserAVictim.
3. As UserB join the talk.
4. As UserA promote UserB to the speaker (works as well with host). This can be done by clicking their avatar and choosing invite to speak (to promote to speaker) or add as host (to promote to host).
5. As UserB notice that a pop up appears saying "USER has invited you to speak". Monitor and save the request used when clicking accept.
The request should be to https://gql.reddit.com 
The body should be similar to 
{"variables":{"platformUserId":"PLATFORM_USER_ID","offerId":"UUID_OFFER_ID"},"id":"475c91dd4480"}
6. As UserA demote UserB to listener. (Click UserB's avatar and click Move to Audience)
7. As UserB repeat/re-send the request used in step 5. Notice that you will be promoted back to speaker/host.
This works even after you are demoted again.

## Impact

This allows speakers/hosts of a talk to re-become a speaker/host at any time after being demoted. This could lead to interruptions to the reddit talk.

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
