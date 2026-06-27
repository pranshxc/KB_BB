---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '434116'
original_report_id: '434116'
title: Exposing voting results on the Slowvote application without actually voting
team_handle: phabricator
created_at: '2018-11-04T21:59:36.712Z'
disclosed_at: '2018-11-05T19:06:59.943Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# Exposing voting results on the Slowvote application without actually voting

## Metadata

- HackerOne Report ID: 434116
- Weakness: 
- Program: phabricator
- Disclosed At: 2018-11-05T19:06:59.943Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
There is a feature on the Phabricator Slowvote application which allows creating polls and asking questions. The poll creator can choose to only allow people who voted to actually see the poll results. However, it seems that by sending an illegal vote a user can still see the poll's results.

## Steps to reproduce
1. As user1 creator a poll on the Slowvote application and make it visible for anyone and also check the "Require a vote to see the responses" option.
2. As user2 browse to the poll and see that since you haven't voted you can't see the actual result.
3. As user2 choose one of the options and vote while intercepting the request.
4. Change the "vote%5B%5D" parameter to contain an illegal vote_id (usually just a big number should be enough).
5. See that you can now see the poll's results but you didn't actually vote.

## Mitigation
You should probably verify that the user is actually voting for a valid option.

## Impact

An unauthorized user can see poll results without making a vote as required by an admin.

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
