---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2068830'
original_report_id: '2068830'
title: HackerOne Support System Doesn't Require Any Authentication May Lead Unauthorized
  Action
weakness: Misconfiguration
team_handle: security
created_at: '2023-07-13T16:48:16.961Z'
disclosed_at: '2023-08-11T07:01:47.017Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: support.hackerone.com
asset_type: URL
max_severity: none
tags:
- hackerone
- misconfiguration
---

# HackerOne Support System Doesn't Require Any Authentication May Lead Unauthorized Action

## Metadata

- HackerOne Report ID: 2068830
- Weakness: Misconfiguration
- Program: security
- Disclosed At: 2023-08-11T07:01:47.017Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I have selected the asset hackerone.com because of the support.hackerone.com is not an accepted bug for bounty but I believe this bug should be fixed by HackerOne with Freshdesk.

**Description:**
We need to open a support ticket from this URL https://support.hackerone.com/support/tickets/new.
To open the ticket system doesn't need to require any authentication. If I have the email address & username of H1 account, I can request a support ticket for the H1 account.
After requesting the support ticket, H1 support agent takes action accordingly.
To test I opened a support ticket 460752. I requested to delete my account even I didn't open any account on support.hackerone.com
The support agent already processed the request & forwarded it to the relevant department.
The design of the system is not secure. Anyone may open a support ticket for my account & if the agent processes it accordingly it's may lead an authorized action for my account. Hackers may also do spamming with this, and even H1 also may suspend the H1 account for that.

### Steps To Reproduce

1. Open this link https://support.hackerone.com/support/tickets/new
2. Create a support ticket with the target account's email address & h1 username.

**Recommendation**
The support system design should be changed. To open a support ticket user should register here https://support.hackerone.com then need to create the support ticket. Otherwise, there needs an email verification step with OTP to open a support request without login.

## Impact

This bug may cause of Unauthorized Action by H1 support agent. Anyone may start spamming by using an H1 user's information.

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
