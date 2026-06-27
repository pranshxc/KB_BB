---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '488643'
original_report_id: '488643'
title: Disclosure of h1 challenges name through the calendar
weakness: Information Disclosure
team_handle: security
created_at: '2019-01-30T16:16:01.379Z'
disclosed_at: '2019-01-30T21:53:55.135Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of h1 challenges name through the calendar

## Metadata

- HackerOne Report ID: 488643
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-01-30T21:53:55.135Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

It seems like the Calendar somehow grabs the name of the target for a h1 challenge even though the target name is not public. 

**Description:**

`h1challenges` do not disclose the name of the target until the time it starts. For example for this challenge: █████ the name of the target is not disclosed anywhere and the page looks something like this: 

█████

However, once we import the calendar on something like Google calendar, it shows the name of the target: 

█████████

This is super useful specially because sometimes program run multiple challenges in short period of time. For example, knowing more about this challenge (the name of the target), a hacker can hack and hodl bugs until the program starts. 

### Steps To Reproduce

1. Add yourself to challenge like the one linked above.
2. Link/update your Google Calendar with the hackerone events calendar.
3. Find the date in the calendar when the challenge is set to start and you can see the name there.

## Impact

Disclosure of h1c-* challenge targets.

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
