---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131053'
original_report_id: '131053'
title: Submit a non valid syntax email
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-04-15T11:01:53.521Z'
disclosed_at: '2017-08-21T13:28:04.878Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Submit a non valid syntax email

## Metadata

- HackerOne Report ID: 131053
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-08-21T13:28:04.878Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

At https://gratipay.com/USER/emails/ you can submit a non valid email.
To do it you only need to change `type="email"` in `type="text"` , you are using a filter, but special chars pass though, as you can see in the screenshots.

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
