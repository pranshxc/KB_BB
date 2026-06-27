---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228156'
original_report_id: '228156'
title: https://www.legalrobot.com/
weakness: Information Disclosure
team_handle: legalrobot
created_at: '2017-05-13T15:09:11.857Z'
disclosed_at: '2018-03-14T15:50:55.741Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# https://www.legalrobot.com/

## Metadata

- HackerOne Report ID: 228156
- Weakness: Information Disclosure
- Program: legalrobot
- Disclosed At: 2018-03-14T15:50:55.741Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello,
I found a info disclosure vulnerability. We can enumerate emails via user_id parameter from Manage users.

And I found that :

hello@legalrobot.com
mbay@codex.stanford.edu
contact@hackerunit.com
conduct@legalrobot.com
dmca@legalrobot.com 

I attached photos from burp repeater to be more explicit.

We can easily bruteforce user_id parameter with ids to harvest user's emails.

Regards,

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
