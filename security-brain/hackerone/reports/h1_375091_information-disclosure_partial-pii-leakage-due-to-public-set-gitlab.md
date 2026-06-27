---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '375091'
original_report_id: '375091'
title: Partial PII leakage due to public set gitlab
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2018-07-01T22:20:43.563Z'
disclosed_at: '2019-12-02T19:06:43.878Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Partial PII leakage due to public set gitlab

## Metadata

- HackerOne Report ID: 375091
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:06:43.878Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
 ████████ allows you to explore the repos, snippets,etc. On the snippets we find a name+icon and some code information. This shouldn't publicly exposed as an attacker may use it to perform further attacks
**Description:**
A configuration issue allows code and the name+icon of a user on the gitlab instance to leaked publicly.
## Impact
A tiny bit of PII leakage, mainly name+ personal picture. Along with a bit of code leakage
## Step-by-step Reproduction Instructions

https://█████/snippets/72
https://███/explore/snippets

## Product, Version, and Configuration (If applicable)
Gitlab
## Suggested Mitigation/Remediation Actions
Make private

## Impact

Recovery of  partial code and username+picture

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
