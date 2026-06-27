---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '961757'
original_report_id: '961757'
title: Twitter Media Studio Source Information Disclosure With Analyst Role
weakness: Information Disclosure
team_handle: x
created_at: '2020-08-18T17:39:44.152Z'
disclosed_at: '2020-10-26T16:10:29.541Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Twitter Media Studio Source Information Disclosure With Analyst Role

## Metadata

- HackerOne Report ID: 961757
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2020-10-26T16:10:29.541Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

== Steps ==
1. With "A" account go to "https://studio.twitter.com/account_management/your_account_number_here/account_users" and Add account "B" as analyst.
2. Now, With "B" account go to "https://studio.twitter.com/" and switch to "A" account. Then go to "https://studio.twitter.com/producer" and you can't see "Sources" section same page. Because you are Analyst role.
3. With "B" account go to GET request "https://studio.twitter.com/1/live/ingest/list.json?account_id=account_id&owner_id=owner_id&user_id=user_id" and you can Information Disclosure.

PoC Video: https://youtu.be/nalRNUeJq3Y

## Impact

With Analyst role you can access all producer sources in Victim's account.
You can see "source name", "source url" and "source key". You can will create new broadcast with this information. (With Analyst Role)

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
