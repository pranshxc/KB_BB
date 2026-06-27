---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1004750'
original_report_id: '1004750'
title: IDOR + Account Takeover  [UNAUTHENTICATED]
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2020-10-10T18:58:15.632Z'
disclosed_at: '2020-11-09T18:28:19.706Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR + Account Takeover  [UNAUTHENTICATED]

## Metadata

- HackerOne Report ID: 1004750
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2020-11-09T18:28:19.706Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1- Open the burp suite.
2- Switch the "Repeater" tab.
3- Paste the content of the attached request into the repeater.
4- Replace the "UID2 = 4820041" value in the cookie with the ID value of the user to be attacked. Also write the user's email in the "userName" input.
5- Replace the victim user's password

**Note: Follow the steps in the "1004745" report to get the user's email address.**

## Impact

You can change users' passwords and take over their account.

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
