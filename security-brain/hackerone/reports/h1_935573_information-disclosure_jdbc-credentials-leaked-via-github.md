---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '935573'
original_report_id: '935573'
title: JDBC credentials leaked via github
weakness: Information Disclosure
team_handle: yelp
created_at: '2020-07-22T23:21:52.278Z'
disclosed_at: '2020-07-27T16:44:01.064Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# JDBC credentials leaked via github

## Metadata

- HackerOne Report ID: 935573
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2020-07-27T16:44:01.064Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
jdbc credentials found on a public github repo.though the repo belongs to yelp or not there is a doubt.I have found many more sensitive data on that repo.so kindly check the repo all together.sensitive data found publicly.
## Platform(s) Affected:
website
## Steps To Reproduce:
1. visit the link 
```https://github.com/supernebula/yelp-j/blob/36de49095d7f3221e3a50adf9bd7ab26ef585f24/yelp/yelp-web-search/src/main/resources/application-dev.properties
```
 you will see leaked credentials.also visit other path to discover more sensitive info.

## Impact

private credentials disclosure.

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
