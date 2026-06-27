---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2427'
original_report_id: '2427'
title: XSRF token problem
weakness: Violation of Secure Design Principles
team_handle: relateiq
created_at: '2014-02-28T13:56:52.823Z'
disclosed_at: '2014-04-20T22:09:02.690Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# XSRF token problem

## Metadata

- HackerOne Report ID: 2427
- Weakness: Violation of Secure Design Principles
- Program: relateiq
- Disclosed At: 2014-04-20T22:09:02.690Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Your web application generates XSRF token values inside cookies which is not a best practice for web applications as revelation of cookies can reveal XSRF Tokens as well. Authenticity tokens should be kept separate from cookies and should be isolated to change operations in the account only.

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
