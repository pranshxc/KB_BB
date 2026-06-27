---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165309'
original_report_id: '165309'
title: Subdomain Takeover in http://genghis-cdn.shopify.io/ pointing to Fastly
team_handle: shopify
created_at: '2016-09-02T15:25:15.655Z'
disclosed_at: '2016-09-06T15:46:49.314Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
---

# Subdomain Takeover in http://genghis-cdn.shopify.io/ pointing to Fastly

## Metadata

- HackerOne Report ID: 165309
- Weakness: 
- Program: shopify
- Disclosed At: 2016-09-06T15:46:49.314Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I've found a Shopifu cdn domain here which had an instance of fastly setup but did not remove the dns record when the service was cancelled. a subdomain takeover similar to that of https://hackerone.com/reports/32825 could be possible.

Vulnerable URL: http://genghis-cdn.shopify.io

Page Response: 
```
Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.
```

Which indicate that this domain is point to fastly but there is no app in fastly with that name allowing anyone to claim it.
The subdomain "http://genghis-cdn.shopify.io/" is currently pointing to Fastly (shopify-e.map.fastly.net), but is not registered to a service. 

```
$ host genghis-cdn.shopify.io
genghis-cdn.shopify.io is an alias for shopify-e.map.fastly.net.
shopify-e.map.fastly.net is an alias for prod.shopify-e.map.fastlylb.net.
prod.shopify-e.map.fastlylb.net has address 151.101.60.108
```


Thanks!

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
