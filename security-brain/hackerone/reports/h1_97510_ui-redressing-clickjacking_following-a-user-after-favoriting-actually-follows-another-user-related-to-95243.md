---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97510'
original_report_id: '97510'
title: 'Following a User After Favoriting Actually Follows Another User (related to
  #95243)'
weakness: UI Redressing (Clickjacking)
team_handle: x
created_at: '2015-11-03T21:43:56.140Z'
disclosed_at: '2015-12-02T17:42:20.929Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Following a User After Favoriting Actually Follows Another User (related to #95243)

## Metadata

- HackerOne Report ID: 97510
- Weakness: UI Redressing (Clickjacking)
- Program: x
- Disclosed At: 2015-12-02T17:42:20.929Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There appears to be a bug similar to #95243 which affects following a user after favoriting one of their tweets via an Intent dialog.

The following is a proof of concept:

https://twitter.com/intent/favorite/?tweet_id=661625230297821184&screen_name=ericrtest3

The screen_name param submits with the favorite form and ends up getting injected into the follow param on the resulting page.

This isn't quite as bad as the previous vulnerability I found, since it requires an additional step (favoriting a tweet) to exploit. However, the impact is exactly the same as the last vulnerability, in that the user has no idea that they're actually following a completely different user.

Please let me know if you have any other questions.

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
