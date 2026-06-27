---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2021684'
original_report_id: '2021684'
title: Issuer not verified from obtained token in user_oidc
team_handle: nextcloud
created_at: '2023-06-12T10:27:14.826Z'
disclosed_at: '2023-08-23T14:56:24.707Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: nextcloud/user_oidc
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Issuer not verified from obtained token in user_oidc

## Metadata

- HackerOne Report ID: 2021684
- Weakness: 
- Program: nextcloud
- Disclosed At: 2023-08-23T14:56:24.707Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As per OIDC spec the issues of the token should be verified to match the issuer obtained in the discovery phase.
https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation (step 2)

Very similar to the aud check in https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/LoginController.php

There are some more steps in that document that I don't think are currently implemented correctly.
However I do not have an OIDC setup to check/verify. So might be worth it to have a look.

## Impact

Without verifying the issuer a MITM is possible.

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
