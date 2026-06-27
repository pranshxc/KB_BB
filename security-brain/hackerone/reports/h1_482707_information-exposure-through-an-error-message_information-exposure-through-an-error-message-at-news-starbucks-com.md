---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '482707'
original_report_id: '482707'
title: Information Exposure Through an Error Message at news.starbucks.com
weakness: Information Exposure Through an Error Message
team_handle: starbucks
created_at: '2019-01-19T21:07:41.840Z'
disclosed_at: '2019-01-31T18:39:42.055Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Information Exposure Through an Error Message at news.starbucks.com

## Metadata

- HackerOne Report ID: 482707
- Weakness: Information Exposure Through an Error Message
- Program: starbucks
- Disclosed At: 2019-01-31T18:39:42.055Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I've discovered Information Exposure Through an Error Message
 on your system POC link:

https://news.starbucks.com/cms/index.php?/cp/login/forgotten_password_form=http://evil.com/?id=test-test

Vulnerable url --> https://news.starbucks.com/cms/index.php?/cp/login/forgotten_password_form=http://evil.com/?id=test-test

Proof screenshot attached.

## Impact

Impact references:

https://cwe.mitre.org/data/definitions/209.html

Best regards

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
