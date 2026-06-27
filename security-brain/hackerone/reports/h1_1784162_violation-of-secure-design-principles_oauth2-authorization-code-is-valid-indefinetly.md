---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1784162'
original_report_id: '1784162'
title: OAuth2 "authorization_code" is valid indefinetly
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2022-11-25T11:50:10.407Z'
disclosed_at: '2024-02-17T08:39:14.500Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# OAuth2 "authorization_code" is valid indefinetly

## Metadata

- HackerOne Report ID: 1784162
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2024-02-17T08:39:14.500Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Your OAuth2 endpoint is not at all following best practices. When the authorization_code is generated it is stored without a timeout. Now according to https://www.rfc-editor.org/rfc/rfc6749#section-4.1.2 10 minutes is recommended. As the goal is that is gets used almost directly or not at all.

Now there is a debate maybe to have on the 10 minutes. But there is kind of a big difference between 10 minutes and no timeout at all.

## Impact

An attacker that obtains this code could possibly easily redeem it in the future.
Or an attacker could just keep trying codes.

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
