---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1108662'
original_report_id: '1108662'
title: The POS app doesn't revoke the Xauth token
weakness: Insufficient Session Expiration
team_handle: shopify
created_at: '2021-02-22T11:19:13.940Z'
disclosed_at: '2021-04-08T18:37:17.397Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Shopify Mobile Applications
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# The POS app doesn't revoke the Xauth token

## Metadata

- HackerOne Report ID: 1108662
- Weakness: Insufficient Session Expiration
- Program: shopify
- Disclosed At: 2021-04-08T18:37:17.397Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It was identified that the POS android application doesn't revoke the authentication token when the user logs off from the session.  More specifically despite the fact that the app removes the entry from the shared_prefs/default_user.xml, the token remains active on the server side and may be used to validate an HTTP request. In order to reproduce the issue, follow the steps bellow:
- Connect to the POS mobile android app 
- Fetch the authentication token, from either the default_user file or from a captured HTTP request 
- Disconnect from the application 
- Use the same token to perform authenticated request in behalf of the account that was connected in the POS

## Impact

An application should always revoke an authentication token by the time that the end user choses to Log Off from a session. Keeping a token active, while the user is not aware of it imposes a big risk, since by the time that an unauthorised entity fetches it, may hijack the user's session and get full control of the store.

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
