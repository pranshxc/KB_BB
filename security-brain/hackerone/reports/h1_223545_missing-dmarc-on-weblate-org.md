---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223545'
original_report_id: '223545'
title: Missing DMARC on weblate.org
team_handle: weblate
created_at: '2017-04-24T18:55:03.356Z'
disclosed_at: '2017-05-17T14:23:30.854Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Missing DMARC on weblate.org

## Metadata

- HackerOne Report ID: 223545
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T14:23:30.854Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary
Email spoofing is possible due to missing SPF/Dmarc Records.
Similar to this report submitted to Hackerone itself: https://hackerone.com/reports/575

##Steps to reproduce:
1- Go to https://emkei.cz ( A Fake Mailer )
2- Set the from to parameter as noreply@weblate.org or any other name, and send it.
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
