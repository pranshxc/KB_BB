---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '326434'
original_report_id: '326434'
title: Able to Select Every Poll Option[http://tedwebers-famous-loudspeakers.vanillacommunities.com]
weakness: Privilege Escalation
team_handle: vanilla
created_at: '2018-03-15T20:48:32.246Z'
disclosed_at: '2018-08-08T14:37:37.595Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Able to Select Every Poll Option[http://tedwebers-famous-loudspeakers.vanillacommunities.com]

## Metadata

- HackerOne Report ID: 326434
- Weakness: Privilege Escalation
- Program: vanilla
- Disclosed At: 2018-08-08T14:37:37.595Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hello
I would like to report a bug in which i was able to select multiple poll options even when a user is only allowed to select a single option.

**Description:**
In the New discussion are of the site http://tedwebers-famous-loudspeakers.vanillacommunities.com , there is an option to create a new poll , so when i tried to create a poll with four options , using proxy i was able to replay four requests with four different poll id's and was successful in selecting all four options which should not have been allowed.
## Steps to reproduce:

1.Open  http://tedwebers-famous-loudspeakers.vanillacommunities.com
2. Go to Discussions tab
3. Select New Poll option
4 Create a Poll
5. Select one of the options of the poll
6. Capture the request in Burp
7. Replay the request By changing the Poll Option ID in request 

The output can be seen below:-

{F272656}

##Patch:- 
There should be mapping of the user id who has given a vote with the poll option id.

Regards
sahil tikoo

## Impact

A user can give multiple votes in a Poll which should not be allowed , such parameter tampering can result in malfunction of poll voting functionality.

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
