---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1912671'
original_report_id: '1912671'
title: Sensitive Data Exposure via wp-config.php file
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2023-03-20T00:36:50.098Z'
disclosed_at: '2023-05-15T15:04:32.303Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Sensitive Data Exposure via wp-config.php file

## Metadata

- HackerOne Report ID: 1912671
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:04:32.303Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

Hi team,
A copy of the WordPress config file wp-config.php has been found at  █████████ endpoint. It contains sensitive information, such as MySQL and AWS credentials, and various keys.

## References

https://codex.wordpress.org/WordPress_Files

## Impact

The page provides information to users who do not need it.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to: ███/wp-config.php_
2. See the information.

## Suggested Mitigation/Remediation Actions
Implement access control.

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
