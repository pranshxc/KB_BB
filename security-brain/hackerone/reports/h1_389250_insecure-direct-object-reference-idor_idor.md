---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '389250'
original_report_id: '389250'
title: IDOR
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2018-08-01T14:09:04.482Z'
disclosed_at: '2022-02-14T21:27:05.079Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR

## Metadata

- HackerOne Report ID: 389250
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:27:05.079Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
IDOR

**Description:**
By changing the value in the parameter █████████= from my own account █████ to something else such as ████████ it is possible to see barcode and expiration date of other ████ without their consent.

## Impact
Information Disclosure

## Step-by-step Reproduction Instructions

1. PoC: https://████████

## Product, Version, and Configuration (If applicable)
Web Application

## Suggested Mitigation/Remediation Actions
Restrict access to other meal cards which the user is not authorized to access.

## Impact

Information Disclosure

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
