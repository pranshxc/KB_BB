---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '924393'
original_report_id: '924393'
title: PIN for passwordless WebAuthn is asked for but not verified
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2020-07-15T12:18:30.607Z'
disclosed_at: '2020-10-28T09:19:31.956Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# PIN for passwordless WebAuthn is asked for but not verified

## Metadata

- HackerOne Report ID: 924393
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2020-10-28T09:19:31.956Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Nextcloud introduced WebAuthn passwordless authentication with version 19. As far as we understand, you assume that your implementation provide two-factor authentication:

"The server asking for authentication can request verification of multiple factors, so that a configured key requires the user to not just plug it in but also enter a PIN or scan a finger print." (see https://www.nitrokey.com/news/2020/what-passwordless-world-looks )

We found the same issue like in Microsoft’s implementation: userVerification is not set and the UV flag is not checked on the server. Thus, even though a FIDO2 key with a PIN is added in a user account, the PIN is not required to log in.

The full description is available in our unlisted blog post at: https://hwsecurity.dev/2020/06/webauthn-pin-bypass/

## Impact

We have a nice video in our blog post:  https://hwsecurity.dev/2020/06/webauthn-pin-bypass/

An attacker could log into the victims account without a PIN by sneaking up on the victim and using the security hardware over NFC.

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
