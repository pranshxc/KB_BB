---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '417839'
original_report_id: '417839'
title: H1514 Lack of access control on edit packing slip template
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2018-10-02T18:08:40.539Z'
disclosed_at: '2019-04-24T20:04:03.799Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# H1514 Lack of access control on edit packing slip template

## Metadata

- HackerOne Report ID: 417839
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2019-04-24T20:04:03.799Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

An admin is able to edit the Edit packing slip template at [/admin/settings/packing_slip_template](https://fisher-hackerone.myshopify.com/admin/settings/packing_slip_template). However, a staff user with only "Home" permission (and none other) can view and also make edits to this template. 

**Description:** 

The Edit packing slip feature exists so an admin user can customize the packing slip added to an order after fulfilment, without the need of external apps (such as Print Order). As mentioned, the problem here arises that any staff user in that Shop can access this endpoint and actually make edits to the template.

## Steps To Reproduce:

1. Create and login a user without permissions (Home only): 
{F354374}

2. As the user without permissions access [/admin/settings/packing_slip_template](https://fisher-hackerone.myshopify.com/admin/settings/packing_slip_template) and make any edits in the template file:
{F354375}

3. Login as other user with adequate permissions, e.g. admin and refresh the same endpoint to confirm that the changes were saved:

{F354377}

## Impact

Having control of the packing slip a malicious staff user can e.g. change the shipping address for his own, potentially receiving orders at some time in the future.

More importantly, besides any disruption of the service (by erasing the template) or manipulation, it can lead to further attacks targeting the exfiltration/disclosure of liquid variables.

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
