---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '905688'
original_report_id: '905688'
title: PII Leak via /██████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-06-22T21:21:08.924Z'
disclosed_at: '2021-02-18T19:11:50.422Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# PII Leak via /██████

## Metadata

- HackerOne Report ID: 905688
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-02-18T19:11:50.422Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker is able to access ServiceNow e-mail notification modules via █████/██████████. Once on this page, the attacker can click any of the notifications, select `Preview Notification`, and choose a user to view their profile data to include Full Name, rank, organization, e-mail address, physical address, and phone number.

## Step-by-step Reproduction Instructions

1. Browse to ██████ and create an account or sign in.
2. Browse to █████████/███████.
3. Click on any of the notification names. Once the notification menu appears, click `Preview Notification` in the top right corner of the screen.
4. The `████` field can now be used to query a user. Once a user is identified, the `(i)` icon can be clicked to view the users PII.
██████

## Suggested Mitigation/Remediation Actions
Restrict access to the █████ and sysevent_email_action.do modules to prevent unauthorized viewing of PII.

## Impact

An adversary can gather PII of all `███████` users via this endpoint.

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
