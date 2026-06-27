---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149028'
original_report_id: '149028'
title: '[URGENT] Password reset emails are sent in clear-text (without encryption)'
weakness: Cryptographic Issues - Generic
team_handle: paragonie
created_at: '2016-07-03T11:42:19.058Z'
disclosed_at: '2016-07-03T17:27:00.619Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# [URGENT] Password reset emails are sent in clear-text (without encryption)

## Metadata

- HackerOne Report ID: 149028
- Weakness: Cryptographic Issues - Generic
- Program: paragonie
- Disclosed At: 2016-07-03T17:27:00.619Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey, I've found that when we use the 'forgot password' page to recover our password, bridge.cspr.ng sends an email to us, and when I tried to get more information about the email from noreply@cspr.ng, I saw that the email is sent in *clear-text* instead of TLS which is so vulnerable since any Man-in-the-middle attacker is able to read these sensitive Emails and get the password reset link -> which can lead to **account takeover**.

You can see in this image that 'no encryption' is used:

{F103057}


--------------
This can further lead to **Account Takeover** that's why I've added [URGENT] in the title.

If you have any other questions or if anything needs clarification, please let me know.

**Thanks,
Ahsan Tahir**

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
