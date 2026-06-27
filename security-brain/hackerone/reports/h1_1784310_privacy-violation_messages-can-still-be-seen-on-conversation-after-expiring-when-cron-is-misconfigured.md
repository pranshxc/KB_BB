---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1784310'
original_report_id: '1784310'
title: Messages can still be seen on conversation after expiring when cron is misconfigured
weakness: Privacy Violation
team_handle: nextcloud
created_at: '2022-11-25T16:25:36.195Z'
disclosed_at: '2023-02-27T15:48:58.336Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Messages can still be seen on conversation after expiring when cron is misconfigured

## Metadata

- HackerOne Report ID: 1784310
- Weakness: Privacy Violation
- Program: nextcloud
- Disclosed At: 2023-02-27T15:48:58.336Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Nextcloud talk has a feature called ```Message Expiration```, Chat messages can be expired after a certain time. However the message  does not really expire and can still be seen by anyone.

## Steps To Reproduce:

1. Create a conversation
1. Set the message expiration Go to Settings > Moderation 
1. Pick anything and using burp intercept the request and set it to 60 or 120 seconds.
1. send a message
1. wait for the message to expire
1. Copy the conversation link and open it to a new tab


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

 ██████████

## Impact

Messages that should expired is divulged to anyone that can access the conversation, This includes personal and group.

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
