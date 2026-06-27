---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '664038'
original_report_id: '664038'
title: protected Tweet settings overwritten by other settings
team_handle: x
created_at: '2019-07-30T23:46:23.862Z'
disclosed_at: '2020-01-01T16:37:18.833Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 174
tags:
- hackerone
---

# protected Tweet settings overwritten by other settings

## Metadata

- HackerOne Report ID: 664038
- Weakness: 
- Program: x
- Disclosed At: 2020-01-01T16:37:18.833Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

protected tweet settings will be disabled without the account owner's knowledge

## step for reproduction
1.Log in to an account with unprotected tweets on the Android app.
2. Log in to the same account on mobile.twitter.com and turn on protected tweets.
3. Confirm that the account's tweets are protected.
4. In the Android app, go to the NOTIFICATION the  click for ON
5. The account's tweets are now unprotected.

==I have deleted all data (stored data and cache), so you don't need to save any cache or history!==

## Impact

your tweet not protected

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
