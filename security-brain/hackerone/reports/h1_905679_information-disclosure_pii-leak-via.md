---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '905679'
original_report_id: '905679'
title: PII Leak via /████████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-06-22T21:00:02.410Z'
disclosed_at: '2021-02-18T19:10:51.200Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# PII Leak via /████████

## Metadata

- HackerOne Report ID: 905679
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-02-18T19:10:51.200Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker is able to view PII (Full name/address/e-mail/phone) of all website users via █████████/████████

## Step-by-step Reproduction Instructions

1. Browse to ████ and login or create an account.
2. Browse to ████/███████
3. Begin typing a name in the `Select User` field, and click the `(i)` icon on the right side of the field to view the users data.
██████

## Suggested Mitigation/Remediation Actions
Restrict access to this endpoint to administrative roles.

## Impact

An adversary can gather PII of all `█████████` users via this endpoint.

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
