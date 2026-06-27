---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1744264'
original_report_id: '1744264'
title: read and message other user's messages
weakness: Insecure Direct Object Reference (IDOR)
team_handle: reddit
created_at: '2022-10-20T13:16:16.693Z'
disclosed_at: '2023-05-18T13:56:34.566Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: '*.reddit.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# read and message other user's messages

## Metadata

- HackerOne Report ID: 1744264
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: reddit
- Disclosed At: 2023-05-18T13:56:34.566Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

go to your account's chat page, stop the request and change the reddit session parameter, now leave the request and you will be able to access the test account's chat screen

send the request to the repeater change the reddit session parameter and send it then you will see the return result is 200

show reply in browser and copy and paste the address into your browser you will access the chat page of your test account

## Impact

other users' chat screen can be accessed
and message can be sent

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
