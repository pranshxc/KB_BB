---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246302'
original_report_id: '246302'
title: Running 2 accounts with a single email
weakness: Business Logic Errors
team_handle: wakatime
created_at: '2017-07-06T05:35:07.799Z'
disclosed_at: '2017-07-06T05:42:23.970Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- business-logic-errors
---

# Running 2 accounts with a single email

## Metadata

- HackerOne Report ID: 246302
- Weakness: Business Logic Errors
- Program: wakatime
- Disclosed At: 2017-07-06T05:42:23.970Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

While testing, I found a logic flaw which made me to make two accounts with a single email

Reproduction Steps

1-Create one account with abc@gmail.com
2-another with abc+1@gmail.com or abc+2@gmail.com etc
3-Emails of both accounts will come at abc@gmail.com

fix:
Dont allow "+" in emails.

Thanks,

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
