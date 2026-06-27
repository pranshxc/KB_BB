---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1164854'
original_report_id: '1164854'
title: Store Admin Page Accessible Without Authentication at http://www.grouplogic.com/ADMIN/store/index.cfm
weakness: Improper Access Control - Generic
team_handle: acronis
created_at: '2021-04-14T12:46:44.266Z'
disclosed_at: '2022-06-07T10:20:01.693Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Store Admin Page Accessible Without Authentication at http://www.grouplogic.com/ADMIN/store/index.cfm

## Metadata

- HackerOne Report ID: 1164854
- Weakness: Improper Access Control - Generic
- Program: acronis
- Disclosed At: 2022-06-07T10:20:01.693Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The store admin page is accessible without authentication at below URL:
```
http://www.grouplogic.com/ADMIN/store/index.cfm
```

The store admin page provides functionalities such as the following:
- Add Edit Items
- Search Products
- Search Results
- Search Orders
- Orders Search Results
- Add New Promo Code
- Promo Code
- Add New How Hear
- How Hear

## Steps To Reproduce
Navigate to below URL from a browser to access the store admin page.

```
http://www.grouplogic.com/ADMIN/store/index.cfm
```

## Recommendations
It is highly recommended to implement proper access controls on administrator functionalities. Only authenticated admin users are to be allowed to access admin pages.

## Impact

Access to admin functionalities without authentication.

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
