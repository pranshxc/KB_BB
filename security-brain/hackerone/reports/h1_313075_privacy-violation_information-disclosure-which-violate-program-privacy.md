---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '313075'
original_report_id: '313075'
title: Information Disclosure which violate program privacy
weakness: Privacy Violation
team_handle: security
created_at: '2018-02-07T03:50:51.945Z'
disclosed_at: '2018-02-20T15:42:12.559Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Information Disclosure which violate program privacy

## Metadata

- HackerOne Report ID: 313075
- Weakness: Privacy Violation
- Program: security
- Disclosed At: 2018-02-20T15:42:12.559Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:**
please refer to the following report:
https://hackerone.com/reports/311289

It was noticed that TTS changed the summary and set the domain to example.gov as not to reveal to the public. But at the bottom of the page, "britta changed the scope from https://ci.fr.cloud.gov to None."

Recommendation:
Should only provide general message for such situation: "britta changed the scope"

## Impact

not much of impact. but violate Confidentiality of the program.

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
