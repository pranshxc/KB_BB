---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '904659'
original_report_id: '904659'
title: PII Leak via /███████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-06-22T05:21:41.931Z'
disclosed_at: '2021-02-18T19:09:42.629Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# PII Leak via /███████

## Metadata

- HackerOne Report ID: 904659
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-02-18T19:09:42.629Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The ██████████ website allows access to PII of all site users via faulty access control to the /██████ endpoint.

## Step-by-step Reproduction Instructions

1. Browse to ████████ and login or create an account.
2. Browse to ███████/████████. You will be able to access PII of all site users (click a username to view the PII).

## Suggested Mitigation/Remediation Actions
Restrict access to the /██████████ module to only administrative users.

## Impact

An adversary can gain access to PII of all ███████ users.

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
