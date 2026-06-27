---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269279'
original_report_id: '269279'
title: SQL injection in partner id field on https://www.teavana.com (Sign-up form)
weakness: SQL Injection
team_handle: starbucks
created_at: '2017-09-18T17:25:04.779Z'
disclosed_at: '2018-01-23T01:06:00.770Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: www.teavana.com
asset_type: URL
max_severity: none
tags:
- hackerone
- sql-injection
---

# SQL injection in partner id field on https://www.teavana.com (Sign-up form)

## Metadata

- HackerOne Report ID: 269279
- Weakness: SQL Injection
- Program: starbucks
- Disclosed At: 2018-01-23T01:06:00.770Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While signing up for "teavana" shopping account on it came to notice that the partner id validation fails and exists SQL injection.

So this is what I did:

1) Visit https://www.teavana.com/us/en/account
2) Click on signin > create shopping account
3) In the partnerno, gave an input of "1234" (1.PNG)
     Result :No issue as expected . Signup fails
     message: "We are unable to verify starbucks partner id" (2 .PNG)
4) Changed input to "1234' OR 1=1" (without double qoutes) (3.PNG)
    Result: This time signup succeeds!!! (4.PNG)

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
