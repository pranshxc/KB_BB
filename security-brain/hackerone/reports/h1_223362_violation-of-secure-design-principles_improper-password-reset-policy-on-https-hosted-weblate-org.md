---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223362'
original_report_id: '223362'
title: Improper Password Reset Policy on https://hosted.weblate.org/
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-04-24T10:25:40.189Z'
disclosed_at: '2017-05-17T14:08:31.105Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Improper Password Reset Policy on https://hosted.weblate.org/

## Metadata

- HackerOne Report ID: 223362
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-17T14:08:31.105Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Application should not allow the user to set the last 3-5 password in terms of secure design principles. It should give a warning or provide such avoidance while user is using repetitive usage of passwords.

Repro:
1. Try to set same old password via Password Reset link.

Fix: Application should avoid user to set last history of passwords to enforce the security.

Let me know if any further info is required.

Regards,
Mr_R3boot.

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
