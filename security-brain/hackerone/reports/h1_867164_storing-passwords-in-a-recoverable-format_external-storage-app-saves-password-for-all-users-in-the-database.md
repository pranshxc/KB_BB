---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '867164'
original_report_id: '867164'
title: External storage app saves password for all users in the database
weakness: Storing Passwords in a Recoverable Format
team_handle: nextcloud
created_at: '2020-05-06T13:13:40.888Z'
disclosed_at: '2021-03-01T11:01:47.786Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- storing-passwords-in-a-recoverable-format
---

# External storage app saves password for all users in the database

## Metadata

- HackerOne Report ID: 867164
- Weakness: Storing Passwords in a Recoverable Format
- Program: nextcloud
- Disclosed At: 2021-03-01T11:01:47.786Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

External storage (files_external) app save passwords of all users to database table "oc_credentials" even when "Log-in credentials, save in database" option is not used.

It's a security risk that allow password extraction of all users.

A local system admin that has access to database and nextcloud config file could decrypt any user password.

### Steps to reproduce
1. Enable app "External storage support" (files_external).
2. Login to nextcloud.
3. User recoverable password will be saved to table "oc_credentials" at "password::logincredentials/credentials".

### Expected behaviour
Don't save user password to table "oc_credentials" unless user has a mount with "Log-in credentials, save in database" option.

### Actual behaviour
Passwords of all users is saved to table "oc_credentials" when files_external app is enabled.

### Tested with
Nextcloud 18.0.4 + External storage 1.9.0
Nextcloud 17.0.5 + External storage 1.8.0

## Impact

A local system admin could recover any user password.

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
