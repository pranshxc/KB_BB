---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1878381'
original_report_id: '1878381'
title: CSRF protection on OIDC login is broken
weakness: Cross-Site Request Forgery (CSRF)
team_handle: nextcloud
created_at: '2023-02-18T11:43:16.340Z'
disclosed_at: '2023-04-04T08:03:38.236Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: nextcloud/user_oidc
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF protection on OIDC login is broken

## Metadata

- HackerOne Report ID: 1878381
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: nextcloud
- Disclosed At: 2023-04-04T08:03:38.236Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

To protect against CSRF the "state" is used in the OIDC flow. On callback this code is verified against the code stored in the session for that user. However in case the token does not match a JSON response is provided that includes the expected state. Thus making it trivial for the attacker to obtain the correct state.

Judging from the code it clearly seem to be debug leftovers https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/LoginController.php#L336-L344

Fixing the todo there should mitigate the issue and ensure the OIDC flow is more secure.


I didn't test ID4ME. But the code is almost identical. So I assume the bug is also the same https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/Id4meController.php#L175-L181

## Impact

The CSRF protection provided with the state is practically useless now.

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
