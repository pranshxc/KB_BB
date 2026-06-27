---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264426'
original_report_id: '264426'
title: Nextcloud logs ldap passwords
weakness: Plaintext Storage of a Password
team_handle: nextcloud
created_at: '2017-08-29T20:09:23.497Z'
disclosed_at: '2020-01-31T14:27:11.481Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Nextcloud logs ldap passwords

## Metadata

- HackerOne Report ID: 264426
- Weakness: Plaintext Storage of a Password
- Program: nextcloud
- Disclosed At: 2020-01-31T14:27:11.481Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When the ldap server is (temporarily) unavailable, data like the attached ends up in log files. I've replaced usernames with `XXX_USERn_XXX` and passwords with `XXX_PASSn_XXX`. It seems that at least the following are missing from `$methodsWithSensitiveParameters` in `lib/private/Log.php`:
 - `bind`
 - `areCredentialsValid`
 - `invokeLDAPMethod`
 - `checkPasswordNoLogging`

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
