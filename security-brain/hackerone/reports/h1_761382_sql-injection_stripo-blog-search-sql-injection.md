---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761382'
original_report_id: '761382'
title: stripo blog search  SQL Injection
weakness: SQL Injection
team_handle: stripo
created_at: '2019-12-19T01:25:21.170Z'
disclosed_at: '2020-01-30T11:50:16.629Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- sql-injection
---

# stripo blog search  SQL Injection

## Metadata

- HackerOne Report ID: 761382
- Weakness: SQL Injection
- Program: stripo
- Disclosed At: 2020-01-30T11:50:16.629Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Sql injection of search parameters at blog search request

## Steps To Reproduce:

  1. request https://stripo.email/blog/search/
  2. input search `1' AND (SELECT 6268 FROM (SELECT(SLEEP(5)))ghXo) AND 'IKlK'='IKlK`
  3. See a very large response delay

## Supporting Material/References:
See attached screenshot

## Impact

Causes an attacker to obtain database information

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
