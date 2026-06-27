---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321410'
original_report_id: '321410'
title: A user can create an event in a group without being in it http://littleguy.vanillastaging.com/
team_handle: vanilla
created_at: '2018-03-02T15:01:10.433Z'
disclosed_at: '2018-06-14T15:29:22.625Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.vanillastaging.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# A user can create an event in a group without being in it http://littleguy.vanillastaging.com/

## Metadata

- HackerOne Report ID: 321410
- Weakness: 
- Program: vanilla
- Disclosed At: 2018-06-14T15:29:22.625Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello again,

I have found another failure other than the #321405 report, in this failure a user can create an event in a group in which he is not.

PoC
===

I've use two accounts.

With the first one I created the following groups

{F268608}

User B has joined the group `Hello`, therefore creates an event in that group

{F268609}

{F268611}

You can see that user B can not create an event since he is not in the group

Now user B is going to create a new event in the group `Hello`

{F268612}

Now user B modifies the group ID by the ID of the pentesting group (as we saw in the previous report the corresponding ID was number 4)

{F268613}

Finally, user B creates the new event

{F268617}


Thanks

## Impact

A user can create events in a group without being in it, in this way it is possible to show that there is no adequate filter to avoid this

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
