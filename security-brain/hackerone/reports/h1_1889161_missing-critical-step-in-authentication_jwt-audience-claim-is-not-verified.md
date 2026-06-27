---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1889161'
original_report_id: '1889161'
title: JWT audience claim is not verified
weakness: Missing Critical Step in Authentication
team_handle: ibb
created_at: '2023-02-28T18:06:26.462Z'
disclosed_at: '2023-04-16T18:43:01.524Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 87
asset_identifier: https://github.com/argoproj/argoproj
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- missing-critical-step-in-authentication
---

# JWT audience claim is not verified

## Metadata

- HackerOne Report ID: 1889161
- Weakness: Missing Critical Step in Authentication
- Program: ibb
- Disclosed At: 2023-04-16T18:43:01.524Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

All versions of Argo CD starting with v1.8.2 are vulnerable to an improper authorization bug causing the API to accept certain invalid tokens.

OIDC providers include an aud (audience) claim in signed tokens. The value of that claim specifies the intended audience(s) of the token (i.e. the service or services which are meant to accept the token). Argo CD does validate that the token was signed by Argo CD's configured OIDC provider. But Argo CD does not validate the audience claim, so it will accept tokens that are not intended for Argo CD.

## Impact

If Argo CD's configured OIDC provider also serves other audiences (for example, a file storage service), then Argo CD will accept a token intended for one of those other audiences. Argo CD will grant the user privileges based on the token's groups claim, even though those groups were not intended to be used by Argo CD.

This bug also increases the blast radius of a stolen token. If an attacker steals a valid token for a different audience, they can use it to access Argo CD.

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
