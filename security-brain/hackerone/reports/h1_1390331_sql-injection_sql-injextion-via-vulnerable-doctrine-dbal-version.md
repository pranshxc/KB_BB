---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1390331'
original_report_id: '1390331'
title: SQL injextion via vulnerable doctrine/dbal version
weakness: SQL Injection
team_handle: nextcloud
created_at: '2021-11-03T07:38:44.435Z'
disclosed_at: '2022-05-11T14:08:04.479Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- sql-injection
---

# SQL injextion via vulnerable doctrine/dbal version

## Metadata

- HackerOne Report ID: 1390331
- Weakness: SQL Injection
- Program: nextcloud
- Disclosed At: 2022-05-11T14:08:04.479Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
SQL injection via limit parameter on user facing APIs

## Steps To Reproduce:
Run security scanner:

  1. REPORT /remote.php/dav/comments/files/1985
  1. XML input oc:filter-comments.oc:limit#text was set to 1'"
  1. You have an error in your SQL syntax

## Supporting Material/References:
For more details see:
https://github.com/nextcloud-gmbh/h1/issues/197

## Impact

Full flexed SQL injection via user provided input

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
