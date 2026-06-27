---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '30575'
original_report_id: '30575'
title: Missing Function Level Access Control in /cindex.php/widget/customize/
weakness: Violation of Secure Design Principles
team_handle: bookfresh
created_at: '2014-10-08T04:26:49.447Z'
disclosed_at: '2016-03-23T17:44:50.071Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing Function Level Access Control in /cindex.php/widget/customize/

## Metadata

- HackerOne Report ID: 30575
- Weakness: Violation of Secure Design Principles
- Program: bookfresh
- Disclosed At: 2016-03-23T17:44:50.071Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Most web applications verify function level access rights before making that functionality visible in the UI. However, applications need to perform the same access control checks on the server when each function is accessed. If requests are not verified, attackers will be able to forge requests in order to access functionality without proper authorization.

The URL "https://www.bookfresh.com/cindex.php/widget/customize/" is accessible to anyone even without authentication. The page should only be accessible to authenticated users.

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
