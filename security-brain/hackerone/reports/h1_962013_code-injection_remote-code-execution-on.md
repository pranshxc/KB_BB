---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '962013'
original_report_id: '962013'
title: Remote Code Execution on █████████
weakness: Code Injection
team_handle: deptofdefense
created_at: '2020-08-19T04:07:49.230Z'
disclosed_at: '2020-09-03T17:25:54.912Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- code-injection
---

# Remote Code Execution on █████████

## Metadata

- HackerOne Report ID: 962013
- Weakness: Code Injection
- Program: deptofdefense
- Disclosed At: 2020-09-03T17:25:54.912Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An unauth solr lead to RCE on ██████████

**Description:**
Hello, I found a solr unauth at https://██████/solr/

This version is 5.5.1, vulnerable with CVE-2019-0192 and CVE-2019-0193, i have try CVE-2019-0193 and successful RCE.

## Impact
Attacker can get shell on server.

## Step-by-step Reproduction Instructions

1. First go to Core Admin and copy path.
██████
2. Update the config.
███████
3. Execute code.
██████████

## Product, Version, and Configuration (If applicable)
Apache Sole 5.5.1
## Suggested Mitigation/Remediation Actions
Update to the latest version and set auth.

## Impact

Attacker can get shell on server.

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
