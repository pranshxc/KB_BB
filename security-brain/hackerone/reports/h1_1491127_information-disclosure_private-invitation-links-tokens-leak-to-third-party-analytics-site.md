---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1491127'
original_report_id: '1491127'
title: Private invitation links/tokens leak to third-party analytics site
weakness: Information Disclosure
team_handle: security
created_at: '2022-02-24T17:31:44.044Z'
disclosed_at: '2022-04-05T06:57:54.754Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private invitation links/tokens leak to third-party analytics site

## Metadata

- HackerOne Report ID: 1491127
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2022-04-05T06:57:54.754Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Private invite links are normally FILTERED before sending to  third-party analytics sites. But it is seen that in few cases where the invitation link that requires users to accept NDA policy, the private invitation links are still sent to third party analytics site. 


**Steps to reproduce**

1. Click on the invitation link that has NDA policy.
2. Look for request to https://www.google-analytics.com/collect with private invitation link in the `dl` parameter.

I am attaching a video PoC demonstrating the steps

██████

## Impact

1. As seen in majority of the cases, private links are normally redacted/FILTERED by hackerone before sending to third-party analytics sites. Some links like ones in the report, miss these security validations.
2. Leaking of private program links can be a privacy issue to the program and users.

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
