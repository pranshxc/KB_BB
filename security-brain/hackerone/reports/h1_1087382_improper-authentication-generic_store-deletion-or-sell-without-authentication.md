---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1087382'
original_report_id: '1087382'
title: Store Deletion or Sell without authentication
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2021-01-26T09:46:38.775Z'
disclosed_at: '2021-10-21T18:57:07.762Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Store Deletion or Sell without authentication

## Metadata

- HackerOne Report ID: 1087382
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2021-10-21T18:57:07.762Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In order for an owner to "close or sell" the store,  a password is required in order to confirm the decision, when the action is applied in the web application.  
It was identified that  the mobile application doesn't require credentials in order to perform the same action, thus by navigating to the Settings->Plan and Permissions -> Sell or Close [bottom of the page] , the user may 'close' the shop without issuing a password.
- The flow in the first case is shown in the screenshots  close1.png, close2.png, close3.png (see attachments)
- The flow in the second case is shown in the screenshot cloceAccountMobile1.png

## Impact

By the time that the physical access requirement is satisfied and since the application is not protected by any kind of user verification (e.g. login pin), as a first place, an unauthorised entity may access the options mentioned above add Sell or Delete a shop without providing any authentication.

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
