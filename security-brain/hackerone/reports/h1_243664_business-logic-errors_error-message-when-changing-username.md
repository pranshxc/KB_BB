---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243664'
original_report_id: '243664'
title: Error Message When Changing Username
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-06-27T16:46:38.944Z'
disclosed_at: '2017-08-17T14:16:45.566Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- business-logic-errors
---

# Error Message When Changing Username

## Metadata

- HackerOne Report ID: 243664
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-08-17T14:16:45.566Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

## Description:

I have found a bug in your fix other my other report, #243609. I reported this in a new report as this is an error in the error message.

When changing your username that starts with a `.` the error message is:
`Username may only contain letters, numbers or the following characters: @ . + - _`

A normal user would be confused as it does not state any reason for the `.` not being allowed at the beginning of their username.

## POC:

1. Change your username to a name that starts with a `.`.
2. You will receive an error message that does not explain why this is not excepted. 

## Mitigation:

I recommend you add a specific error message that states that your username cannot start with a `.`.

Thanks!

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
