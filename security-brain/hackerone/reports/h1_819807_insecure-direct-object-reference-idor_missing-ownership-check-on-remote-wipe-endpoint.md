---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '819807'
original_report_id: '819807'
title: Missing ownership check on remote wipe endpoint
weakness: Insecure Direct Object Reference (IDOR)
team_handle: nextcloud
created_at: '2020-03-15T21:55:05.955Z'
disclosed_at: '2020-04-19T13:15:25.770Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 130
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Missing ownership check on remote wipe endpoint

## Metadata

- HackerOne Report ID: 819807
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: nextcloud
- Disclosed At: 2020-04-19T13:15:25.770Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

On settings/user/security

You can mark a device for wipe out that does not belong to you.

Steps:

1. Create 2 accounts one for the hacker and one for the victim
2. On both accounts add devices with different names
3.  On the hacker account, while intercepting with burpsuite, select the option to wipe out a device
4.  Forward with burpsuite and in the url that looks like settings/personal/authtokens/wipe/{data-id}, change the data-id to the id of the device of the victim
5. Stop intercepting or forward again and the device of the victim will be marked for wipe out. 

Here is a video demo 
{F748890}

## Impact

Attacker can wipe out the device of another user by using the device ID

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
