---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '382612'
original_report_id: '382612'
title: Potential SSRF and disclosure of sensitive site on *shopifycloud.com
weakness: Server-Side Request Forgery (SSRF)
team_handle: shopify
created_at: '2018-07-17T14:01:13.005Z'
disclosed_at: '2018-07-19T20:47:58.912Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Potential SSRF and disclosure of sensitive site on *shopifycloud.com

## Metadata

- HackerOne Report ID: 382612
- Weakness: Server-Side Request Forgery (SSRF)
- Program: shopify
- Disclosed At: 2018-07-19T20:47:58.912Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

*Note: I am reporting this after talking with @shopify-peteryaworski*

**Summary**
There is a staging/testing site for payment cancellations and refunds at shopifycloud.com. This site allows sending post request and fetching the response back to the user. This leads to SSRF because it allows fetching potential internal clients and servers. 

**Description**
https://offsite-gateway-sim.shopifycloud.com/notification allows sending test request to a user supplied `x_url_callback` url. In such request it is allowed to submit Google metadata IPs and get a response back. Thankfully it seems that after the last SSRF report on Shopify, you guys have completely stripped the server from having any access to Google Metadata because for `v1beta1` this server responds with `This metadata api is not allowed in the metadata proxy`. Additionally for the regular `v1` it returns 403 because the header is missing. The only potential exploit here is that if there is any internal site only Google IP is able to access then someone can call that site and see its details. 

**Reproduction**
1. Go to https://offsite-gateway-sim.shopifycloud.com/notification and put http://metadata/computeMetadata/v1beta1/ as a test request.

## Impact

SSRF. The repo for this is private so I am assuming this has to be private too?

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
