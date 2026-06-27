---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76784'
original_report_id: '76784'
title: Cheating at gallery rating
weakness: Privilege Escalation
team_handle: zaption
created_at: '2015-07-19T13:38:24.628Z'
disclosed_at: '2015-07-22T21:59:40.255Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Cheating at gallery rating

## Metadata

- HackerOne Report ID: 76784
- Weakness: Privilege Escalation
- Program: zaption
- Disclosed At: 2015-07-22T21:59:40.255Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello!

Example: http://www.zaption.com/listing/55aba5719c77e5386eb28df0

We can rate tour any mark by POST http://www.zaption.com/ajax/gallery/listing/{tour_id}/rate/{mark}
For example:
POST http://www.zaption.com/ajax/gallery/listing/55aba5719c77e5386eb28df0/rate/100000000000000000

So, we have "curve" layout and cheating in voting.

Thank you for reading this report!

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
