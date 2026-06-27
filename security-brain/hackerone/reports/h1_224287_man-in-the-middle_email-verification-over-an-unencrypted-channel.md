---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224287'
original_report_id: '224287'
title: Email verification over an unencrypted channel
weakness: Man-in-the-Middle
team_handle: weblate
created_at: '2017-04-27T11:00:52.313Z'
disclosed_at: '2017-05-17T14:08:06.226Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- man-in-the-middle
---

# Email verification over an unencrypted channel

## Metadata

- HackerOne Report ID: 224287
- Weakness: Man-in-the-Middle
- Program: weblate
- Disclosed At: 2017-05-17T14:08:06.226Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey guys,

When registered for an account, the confirmation email sent out, has a http link (refer the attachment) and allows a man-in-the-middle attacker to take over the account. He can do the following:
- Obtain the confirmation tokens while transmitting to the weblate infra and redirect the user to a fake site.
- On clicking the link, the user is auto logged in to the account. The attacker can take over the account if he obtains the tokens in the transmission.

**Steps to reproduce:**
- Navigate to https://hosted.weblate.org/accounts/register/
- Fill up the form and submit
- Open the email inbox
- See the link contains http://. Verify both the visible text as well as the actually link is http://.
- Note that all other links are http:// too

**Suggested Fix:**
- Change the confirmation link sent through the email, to *https://*. Both the text visible as well as the actual link.
- Avoid automatic logging into the account when the link is clicked. Display a message saying *Your account is verified. Please login to continue.


**Affected area:** https://hosted.weblate.org/accounts/register/

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
