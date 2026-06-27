---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '323992'
original_report_id: '323992'
title: Publicly accessible Order confirmations leaking User Emails on ███
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2018-03-09T20:29:06.164Z'
disclosed_at: '2019-10-08T18:55:41.949Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- information-disclosure
---

# Publicly accessible Order confirmations leaking User Emails on ███

## Metadata

- HackerOne Report ID: 323992
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-10-08T18:55:41.949Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I noticed that a user's order confirmation was publicly accessible leaking email information
**Description:**
An attacker can gleam sensitive information that is stored in the order confirmation file
## Impact
Medium
## Step-by-step Reproduction Instructions

https://██████████/BinaryHandler.ashx?RecordID=MZtO1v39KiFWXykCvQEcOw%3D%3D

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Scrub user data

## Impact

Attackers can steal PII

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
