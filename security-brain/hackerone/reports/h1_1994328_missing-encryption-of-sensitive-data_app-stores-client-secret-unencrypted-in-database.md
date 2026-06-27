---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1994328'
original_report_id: '1994328'
title: App stores client secret unencrypted in database
weakness: Missing Encryption of Sensitive Data
team_handle: nextcloud
created_at: '2023-05-19T11:29:28.092Z'
disclosed_at: '2023-08-23T14:56:00.746Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/user_oidc
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- missing-encryption-of-sensitive-data
---

# App stores client secret unencrypted in database

## Metadata

- HackerOne Report ID: 1994328
- Weakness: Missing Encryption of Sensitive Data
- Program: nextcloud
- Disclosed At: 2023-08-23T14:56:00.746Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

To identify the nextcloud server need to have the client id and the client secret.
The id is public but the secret is not. Currently this is stored in plain text in the database. Here you can't use hashing as you need the actual value. But Nextcloud should at the very least make sure that this data is properly encrypted at rest in the database.

## Impact

An attacker that obtains read only access to (a snapshot of) the database can impersonate the Nextcloud server without issues

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
