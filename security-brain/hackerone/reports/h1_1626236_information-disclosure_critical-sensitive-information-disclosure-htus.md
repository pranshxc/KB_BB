---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1626236'
original_report_id: '1626236'
title: Critical sensitive information Disclosure. [HtUS]
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2022-07-05T14:04:33.062Z'
disclosed_at: '2023-01-13T18:05:48.810Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
tags:
- hackerone
- information-disclosure
---

# Critical sensitive information Disclosure. [HtUS]

## Metadata

- HackerOne Report ID: 1626236
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2023-01-13T18:05:48.810Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

(Database user,Database password,Database name) 
on https://██████.edu/

I got sensitive information:
view-source:https://██████████.edu/database.php.orig


Database information (Database user,Database password,Database name)
$hostname     = '████████.edu';
$db         = '█████████';
$username     = '████_user';
$password     = '████';

## Impact

Bug impact:
Sensitive information disclosed and possible for an attacker can access into the system.

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
