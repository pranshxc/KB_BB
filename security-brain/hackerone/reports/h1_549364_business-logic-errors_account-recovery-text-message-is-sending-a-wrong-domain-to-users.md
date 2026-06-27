---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '549364'
original_report_id: '549364'
title: Account recovery text message is sending a wrong domain to users.
weakness: Business Logic Errors
team_handle: security
created_at: '2019-04-27T15:50:20.341Z'
disclosed_at: '2019-05-31T06:14:21.904Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 112
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Account recovery text message is sending a wrong domain to users.

## Metadata

- HackerOne Report ID: 549364
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2019-05-31T06:14:21.904Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I hope you're fine. :)

**Summary:**
When users setup Account recovery at Authentication section Hackerone sends them text message to their updated phone number with a wrong domain link.

**Description:**
When users adds phone number at Account recovery, they get a text message on their phone number, which shows "Your Hackerone account recovery phone number has been updated. If this is unexpected, please contact **supportahackerone.com**. Which is not your domain and can be bought or can be own by anyone. If a user contact to this domain and attacker have own this domain already, he can easy manipulate him/her to do something wrong with their accounts. He don't have to find another way to into the official Hackerone text messages to give his own website as Hackerone already doing it. He just have to own this domain and start manipulating users. And it also sounds very much similar "supportahackerone.com" to support.hackerone.com . Which can help him also.
 
**Steps To Reproduce:**
1. Go to Authentication section. And setup account recovery.
2. Add phone number and you'll receive a text message.

Fix:
Use support.hackerone.com instead of supportahackerone.com.

## Impact

Attacker can easily manipulate a user to do a wrong thing to his account.

Thank you,
Hope you'll fix this soon. And will response to my report nicely. :)
If you have any questions please feel free to ask me. :)

**And also my report is not really about support.hackerone.com subdomain, i know that is out of scope. But this message was sent through hackerone.com.**

**Screenshots:**

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
