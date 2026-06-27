---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1004964'
original_report_id: '1004964'
title: All private support requests to ███████ are being disclosed at https://███████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-10-11T07:02:44.354Z'
disclosed_at: '2021-07-29T19:53:11.477Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- information-disclosure
---

# All private support requests to ███████ are being disclosed at https://███████

## Metadata

- HackerOne Report ID: 1004964
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-07-29T19:53:11.477Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello DoD Team
**Summary:**
I have found out that all personal requests made to https://█████ form are being disclosed to the public at https://███████, which posses a critical privacy issue.

**Description:**
While searching my name at google "naglinagli" i have encountered a weird mention of my xss payload at the following endpoint https://██████████, which made realize that all the requests made at the contact form are open to the public

## Step-by-step Reproduction Instructions

1. Navigate to https://███████
2. File a request.

█████████

3. Your request will publicly appear at https://█████

████

##
## Suggested Mitigation/Remediation Actions
Making the access to the vulnerable endpoint to authorized personal only.

##Best Regards,
nagli.

## Impact

Personal reports made to █████ including PII of customers is being disclosed to the public through publicly accessible endpoint

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
