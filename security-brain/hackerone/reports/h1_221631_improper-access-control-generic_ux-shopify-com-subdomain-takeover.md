---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221631'
original_report_id: '221631'
title: '[ux.shopify.com] Subdomain takeover'
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2017-04-17T18:45:14.594Z'
disclosed_at: '2018-10-19T13:55:29.578Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- improper-access-control-generic
---

# [ux.shopify.com] Subdomain takeover

## Metadata

- HackerOne Report ID: 221631
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2018-10-19T13:55:29.578Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The subdomain ux.shopify.com points to domains.tumblr.com, but this subdomain is not used by anyone on Tumblr. Any user can register his blog for this subdomain.
```
ux.shopify.com.	3600	IN	CNAME	domains.tumblr.com.
```
{F176574}

As an PoC, I registered a blog for this subdomain. It is available only with the password **c7gBX6gELPFLhYOeYxQD**.

http://ux.shopify.com/

{F176578}

You need to remove the DNS entry ux.shopify.com. Or I can release this subdomain so that you can register it.

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
