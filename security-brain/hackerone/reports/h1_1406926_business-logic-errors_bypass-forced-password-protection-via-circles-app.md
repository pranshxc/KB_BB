---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1406926'
original_report_id: '1406926'
title: bypass forced password protection via circles app
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2021-11-22T09:25:03.593Z'
disclosed_at: '2022-06-19T08:10:12.075Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/circles
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# bypass forced password protection via circles app

## Metadata

- HackerOne Report ID: 1406926
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2022-06-19T08:10:12.075Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A user can bypass password enforcement for link and email shares by using a circle

## Steps To Reproduce:
 1. enable forced passwords for link shares and email shares as administrator in the share settings
 2. as user create a circle and add an e-mail-address
 3. share some file to that circle

## Supporting Material/References:
Used version: Nextcloud Version 22.2.3 circles version 22.1.1

## Impact

A user can create an link that is not password protected even if this is forced by the administrator.

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
