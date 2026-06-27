---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1716249'
original_report_id: '1716249'
title: sensitive data exposure
weakness: Insecure Storage of Sensitive Information
team_handle: reddit
created_at: '2022-09-29T04:04:16.918Z'
disclosed_at: '2022-11-10T14:41:12.389Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# sensitive data exposure

## Metadata

- HackerOne Report ID: 1716249
- Weakness: Insecure Storage of Sensitive Information
- Program: reddit
- Disclosed At: 2022-11-10T14:41:12.389Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
[A Password hash entry was found in /etc/passwd. This is a major vulnerability since /etc/passwd is a world-readable file by default. Once the password hash is found, an attacker may extract the password using a program like crack.]

## Impact:
it is high impact vulnerability .once hacker found password hash it may be leads to develop a program like crack

## Steps To Reproduce:
[https://www.reddit.com/etc%2fpasswd]

  1. [add step]
  1. [add step]
  1. [add step]

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

A Password hash entry was found in /etc/passwd. This is a major vulnerability since /etc/passwd is a world-readable file by default. Once the password hash is found, an attacker may extract the password using a program like crack.

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
