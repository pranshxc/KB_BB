---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1083923'
original_report_id: '1083923'
title: Sharing products with Mail allows phishing attacks due to misconfiguration.
weakness: Business Logic Errors
team_handle: openmage
created_at: '2021-01-22T02:34:08.980Z'
disclosed_at: '2021-04-25T00:13:31.730Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
asset_identifier: demo.openmage.org
asset_type: URL
max_severity: medium
tags:
- hackerone
- business-logic-errors
---

# Sharing products with Mail allows phishing attacks due to misconfiguration.

## Metadata

- HackerOne Report ID: 1083923
- Weakness: Business Logic Errors
- Program: openmage
- Disclosed At: 2021-04-25T00:13:31.730Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team. I found a part that could cause a phishing attack. Incorrect configuration in the part of sharing products with mail causes this.

1. Go to https://demo.openmage.org/sendfriend/product/send/id/430/cat_id/20/
2. The Sender email address should normally be an email address provided by you. Here, our own e-mail address allows us to send an e-mail to a user with an e-mail address that does not belong to us.
3. Then write the e-mail address of the person you will send the e-mail to and send it.
4. Check your mailbox and spam box. You can send mail from accounts that do not belong to you.


Correction: We can only choose the e-mail address to send. You can get yourself an e-mail address and use that e-mail address to share products.
Example: An e-mail address in the form of sharefriend@demo.openmage.org. This will likely prevent this event.

## Impact

It enables phishing attacks.

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
