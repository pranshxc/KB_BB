---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '975047'
original_report_id: '975047'
title: User sensitive information disclosure
weakness: Privacy Violation
team_handle: shopify
created_at: '2020-09-05T04:41:57.593Z'
disclosed_at: '2020-10-22T17:28:16.842Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
asset_identifier: Shopify Third Party Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- privacy-violation
---

# User sensitive information disclosure

## Metadata

- HackerOne Report ID: 975047
- Weakness: Privacy Violation
- Program: shopify
- Disclosed At: 2020-10-22T17:28:16.842Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1、open  shopify指南 Applets
2、click  个人中心
3、click 编辑资料 (微信图片_20200905123248.png)
4、https://api-wechat.shopify.cn/api/sp/customer/id    (1.png) 
5、Modify the ID value to traverse the user information

## Impact

User sensitive information disclosur

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
