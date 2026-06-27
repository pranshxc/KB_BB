---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '883693'
original_report_id: '883693'
title: Information Disclosure(PHPINFO/Credentials) on DoD Asset
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-05-27T14:45:20.010Z'
disclosed_at: '2021-03-11T20:41:03.457Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Information Disclosure(PHPINFO/Credentials) on DoD Asset

## Metadata

- HackerOne Report ID: 883693
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:41:03.457Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
A DoD leaks credentials on a phpinfo() page.

**Description:**
https://███ publicly displays a phpinfo() page that leaks system information and credentials.

## Impact
The impact is medium not only due to information leakage of numerous different details such as system information but also the leakage of domain credentials.
USERDOMAIN	███████
USERNAME	██████
█████████PASSWORD']	████████

## Step-by-step Reproduction Instructions

1. Visit: https://████/████
2. Information Disclosed

## Suggested Mitigation/Remediation Actions
████████ BAT  suggests removing the ███ page or requiring authentication before making it accessible.

## Impact

The impact is medium not only due to information leakage of numerous different details such as system information but also the leakage of domain credentials.

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
