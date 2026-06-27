---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1523584'
original_report_id: '1523584'
title: Attacker shall recieve order updates on whatsapp for users who have activated
  whatsapp notification
weakness: Business Logic Errors
team_handle: zomato
created_at: '2022-03-27T18:18:46.521Z'
disclosed_at: '2022-04-06T06:00:20.037Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: '434613896'
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Attacker shall recieve order updates on whatsapp for users who have activated whatsapp notification

## Metadata

- HackerOne Report ID: 1523584
- Weakness: Business Logic Errors
- Program: zomato
- Disclosed At: 2022-04-06T06:00:20.037Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

H

Summary:
1. Order ID are IDOR ( Insecure Direct Object Reference )
2. When users activated whats app notification an attacker would start receiving the notification without user interaction about their order.

Proof Of Concept:-

When an user order on a restaurant he/she can start whatsapp notification on their order.

██████████

Steps to Reproduce:-

1. When the user activates whats app notification by sending the message with order id. His order notification's vulnerable.

2. Now the attacker sends the message with above vulnerable order id ( Order id is IDOR - eg:15625383 )

3. He will get the error notification, though he will start receiving the updates.

{F1670097}

3.1 the updates would be
3.1.1 delivery partner assigned.
3.1.2 when he will reach
3.1.2 once he delivered the order.

## Impact

business logic error.

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
