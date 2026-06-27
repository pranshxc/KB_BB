---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152477'
original_report_id: '152477'
title: Username .. (double dot) should be restricted or handled carefully
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-07-20T10:23:48.235Z'
disclosed_at: '2016-07-20T13:46:30.099Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Username .. (double dot) should be restricted or handled carefully

## Metadata

- HackerOne Report ID: 152477
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-07-20T13:46:30.099Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

If I change my username to "**test**" then as in normal case it will send a GET request to **/test/settings** but if I change my username to "**..**" (**double dot** within inverted commas)  then it will send GET request to /settings because /../settings will change to /settings and hence final GET request will be to /settings which will show a 404 page.
 I have attached a video as POC.

Regards!

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
