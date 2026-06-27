---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1018094'
original_report_id: '1018094'
title: Staff Member can Get POS Access Without User Interaction
team_handle: shopify
created_at: '2020-10-25T00:54:23.928Z'
disclosed_at: '2020-11-19T22:08:27.893Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Staff Member can Get POS Access Without User Interaction

## Metadata

- HackerOne Report ID: 1018094
- Weakness: 
- Program: shopify
- Disclosed At: 2020-11-19T22:08:27.893Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found that it is possible for a staff member to grant themselves POS access without user interaction from admin.

## Steps to reproduce
- Login as a staff member with `Manage Locations` permission only, in a shop that has POS channel up and running (Could be Lite)
- Make sure your staff member account didn't have POS enabled 
- Make this GraphQL call

```json
{"query":"mutation {retailUserDataUpdate(id:\"gid://shopify/StaffMember/63779504283\",retailUserData:{posAccess:true,pin:\"1423\"}){staffMember{name canAccessPrivateApps authenticationSettings{tfaEnabled}}userErrors{message}}}"}
```

Replace `63779504283` with your personal staff member id, you can find it in `https://your-store.myshopify.com/admin/settings/account/` and click your account name, then you staff member id is in the url.

- Now your staff member account has POS enabled, and pin is set.

## Impact

It will allow to a staff member to POS takeover without user interaction.

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
