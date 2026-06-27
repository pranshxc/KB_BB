---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '32137'
original_report_id: '32137'
title: Content Spoofing via reports
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-10-19T12:14:07.346Z'
disclosed_at: '2016-05-25T02:17:19.521Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing via reports

## Metadata

- HackerOne Report ID: 32137
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-05-25T02:17:19.521Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The `report_id[]` param simply returns whatever entered , instead of showing report id's only. This can result in content injection in the reports field.
For example check this one : http://goo.gl/py2V8j

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
