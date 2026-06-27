---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1244798'
original_report_id: '1244798'
title: Client Side string length check
weakness: Client-Side Enforcement of Server-Side Security
team_handle: khanacademy
created_at: '2021-06-26T02:47:50.894Z'
disclosed_at: '2023-10-14T00:36:00.126Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- client-side-enforcement-of-server-side-security
---

# Client Side string length check

## Metadata

- HackerOne Report ID: 1244798
- Weakness: Client-Side Enforcement of Server-Side Security
- Program: khanacademy
- Disclosed At: 2023-10-14T00:36:00.126Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
in the "Class Settings" page on khanacademy.org  you can rename the class, but the string length check is not done on the server side. 
Throughout the experimentation I used an account with associated email "██████████" and where applicable, class ID ████.
An attacker can save thousands of characters instead of the expected 50 (while I was testing I was able to set a string of over 108 thousand characters!).
The fix may be limited to the server-side string length check, however I recommend checking the string length on all other pages as well.

Request URL: https://it.khanacademy.org/api/internal/graphql/renameStudentListMutation
Parameter (POST): "name"

## Impact

An attacker could exploit this lack of control to save content, break the page template (for /profile/attackerusername too), crash the page for low-memory visitors, and possibly cause unexpected behavior.

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
