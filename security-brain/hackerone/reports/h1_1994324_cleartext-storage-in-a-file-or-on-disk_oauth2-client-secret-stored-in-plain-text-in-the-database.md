---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1994324'
original_report_id: '1994324'
title: OAuth2 client_secret stored in plain text in the database
weakness: Cleartext Storage in a File or on Disk
team_handle: nextcloud
created_at: '2023-05-19T11:22:17.158Z'
disclosed_at: '2023-11-15T07:22:13.305Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-in-a-file-or-on-disk
---

# OAuth2 client_secret stored in plain text in the database

## Metadata

- HackerOne Report ID: 1994324
- Weakness: Cleartext Storage in a File or on Disk
- Program: nextcloud
- Disclosed At: 2023-11-15T07:22:13.305Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If an attacker would obtain a dumb of the database they could read out the OAuth2 client secret trivially.
https://github.com/nextcloud/server/blob/master/apps/oauth2/lib/Controller/OauthApiController.php#L128

While I realise this is a big if it is not that hard to make sure the client secret is stored properly hashed.
Or at the very least make sure it is stored encrypted. (however non recoverable has the preference here I'd say)

## Impact

An attacker obtaining the read access to a dump of the database can trivially impersonate any OAuth2 client.

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
