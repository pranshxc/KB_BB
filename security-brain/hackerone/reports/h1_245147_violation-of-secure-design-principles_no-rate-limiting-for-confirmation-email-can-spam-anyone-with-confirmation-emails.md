---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245147'
original_report_id: '245147'
title: No rate limiting for confirmation email, can spam anyone with confirmation
  emails
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-07-01T16:34:22.548Z'
disclosed_at: '2017-07-03T16:51:02.039Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limiting for confirmation email, can spam anyone with confirmation emails

## Metadata

- HackerOne Report ID: 245147
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-03T16:51:02.039Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, there is no rate limiting implemented in sending the confirmation email. Thus, attacker can use this vulnerability to bomb out the email inbox of the victim.

Proof of Concept :

1. Register a account  in wakatime.com
2. Login to account and go to https://wakatime.com/settings/account
3.  Under that click on send confirmation email to any email you want and capture that request with burp.
4. Now you can use the intruder and repeat the request by using different payloads under User Agent.
5. Check the email inbox, it will be bombed with lots of email.

{F199308}

Reference from : #87531

Hope, you fix this soon.

Best Regards,
Pratyush Janghel

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
