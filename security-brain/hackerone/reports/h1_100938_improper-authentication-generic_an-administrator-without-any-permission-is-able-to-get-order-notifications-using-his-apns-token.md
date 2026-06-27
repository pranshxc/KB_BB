---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100938'
original_report_id: '100938'
title: An administrator without any permission is able to get order notifications
  using his APNS Token.
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-11-22T12:16:06.681Z'
disclosed_at: '2015-12-14T18:00:13.307Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# An administrator without any permission is able to get order notifications using his APNS Token.

## Metadata

- HackerOne Report ID: 100938
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-12-14T18:00:13.307Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description**
----
An administrator who lacks the 'Settings' permission is not able to add notifications through the UI. But the endpoint `shop.myshopify.com/admin/mobile_devices.json` does allow the unprivileged user to add his own device.



**PoC**
----
This PoC simply show how to get & re-use the mobile APNS Token.

. Log in the Shopify phone app with a full access account
. Intercept the request to `POST /admin/mobile_devices.json`
. Remove all permissions of that account.
. Remove the mobile notification added.
. Replay the request to `POST /admin/mobile_devices.json`

The order notification has been added in `/admin/settings/notifications`
Make an order, and the mobile will get the notification.

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
