---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200762'
original_report_id: '200762'
title: Email Spoofing
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2017-01-24T12:22:08.499Z'
disclosed_at: '2017-01-25T14:01:02.287Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email Spoofing

## Metadata

- HackerOne Report ID: 200762
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2017-01-25T14:01:02.287Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

Similar to this report submitted to Hackerone itself: https://hackerone.com/reports/575

You also are vulnerable to email spoofing.

Steps to reproduce:
1- Go to https://emkei.cz ( A Fake Mailer )
2- Set the from to parameter as support@nextcloud.com or any other name, and send it.
3- The email is sent with any content you'd like to add as the message.

Thanks.

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
