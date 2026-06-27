---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280529'
original_report_id: '280529'
title: Incorrect Functionality of Password reset links
weakness: Violation of Secure Design Principles
team_handle: infogram
created_at: '2017-10-19T14:45:49.949Z'
disclosed_at: '2017-10-30T09:23:39.528Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Incorrect Functionality of Password reset links

## Metadata

- HackerOne Report ID: 280529
- Weakness: Violation of Secure Design Principles
- Program: infogram
- Disclosed At: 2017-10-30T09:23:39.528Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability:-
->Password reset links should work in such a way that "only the last generated password reset link should be valid" i.e; if two tokens are generated at a time, then 2nd token must work and 1st token must be invalid.
->If not, another case is that "if some number of reset links are generated at a time, if any one link is used in that links, then all remaining links should get invalid".

This is the standard practice followed and implemented by all secured websites that are running bug bounty programs on hackerone.

Any issues, please let me know...

Thank you

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
