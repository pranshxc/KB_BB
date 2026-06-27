---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '313050'
original_report_id: '313050'
title: IDOR in treat subscriptions
weakness: Insecure Direct Object Reference (IDOR)
team_handle: zomato
created_at: '2018-02-07T02:38:01.307Z'
disclosed_at: '2018-04-25T12:25:30.883Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in treat subscriptions

## Metadata

- HackerOne Report ID: 313050
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: zomato
- Disclosed At: 2018-04-25T12:25:30.883Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The treat subscriptions tab in my profile has an IDOR.

The corresponding api:

POST /php/filter_user_tab_content.php HTTP/1.1
user_id=██████&tab=treat_subscription&order_history_offset=0&order_history_limit=20


You can give any user id and you will be able to see the treat subscriptions of that user.

## Impact

A user can view treat subscriptions of any other user.

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
