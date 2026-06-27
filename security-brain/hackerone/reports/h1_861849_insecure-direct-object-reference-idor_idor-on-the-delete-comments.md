---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '861849'
original_report_id: '861849'
title: Idor on the DELETE /comments/
weakness: Insecure Direct Object Reference (IDOR)
team_handle: rghost
created_at: '2020-04-28T22:30:42.188Z'
disclosed_at: '2020-05-13T17:17:24.324Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
asset_identifier: rghost.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Idor on the DELETE /comments/

## Metadata

- HackerOne Report ID: 861849
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: rghost
- Disclosed At: 2020-05-13T17:17:24.324Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[Idor on /comments]

## Steps To Reproduce:
[Make sure you have 2 different ID's to maintain 2 different session for ensurity]

  1. The request can be tamper with the ID of different (comment) both the functions of edit/delete can be used
  2. Delete gets hampered with the Captcha which is thrown but the Comment of different user can be observed in the request
  3. Assume user 1"victim" made a comment "comment X" user 2 can edit the request for editing his comment "Y" to "X" further as the attacker failed editing the comment of victim, further disabling the edit option for user 1 :| that will make user 1"victim" left with only option to delete the comment. sed very sed
  4. Even this works widely with Burp_Intruder that means it doesn't even have rate limit.

## Impact

An attacker with a privilege to the user can harness the activities of any user around intentionally or target them widely.

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
