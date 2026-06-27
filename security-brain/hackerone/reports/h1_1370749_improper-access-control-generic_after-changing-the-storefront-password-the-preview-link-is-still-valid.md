---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1370749'
original_report_id: '1370749'
title: After changing the storefront password, the preview link is still valid
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2021-10-15T06:20:01.690Z'
disclosed_at: '2022-04-21T22:38:45.570Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# After changing the storefront password, the preview link is still valid

## Metadata

- HackerOne Report ID: 1370749
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2022-04-21T22:38:45.570Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description:

1. The user needs to know the storefront password to generate the preview link.
2. After the administrator changes the storefront password, users can still access the storefront through the preview link. 

3.reason:
（1）User can generate preview link.
（2）Simply changing the password will not invalidate the preview link. Only after closing and restarting the storefront password, the previous preview link will become invalid.

##Step：

1. Visit the storefront and enter the password.

2.Search ```shopify.theme``` in the web development tool of the browser to get the theme ID value.
{F1482354}

3.Replace the value of the ```preview_theme_id parameter```.
```
https://your-store.myshopify.com.myshopify.com/?_ab=0&_fd=0&_sc=1&preview_theme_id=xxxxxxxx
```

4. Access the preview link, when the storefront password is changed, the preview link is still valid.

5.Video:
{F1482355}

## Impact

After changing the storefront password, the preview link is still valid

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
