---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '439912'
original_report_id: '439912'
title: Stored XSS on demo app link
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-11-13T12:17:08.575Z'
disclosed_at: '2020-06-12T14:15:31.908Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: apps.shopify.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on demo app link

## Metadata

- HackerOne Report ID: 439912
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-06-12T14:15:31.908Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found stored XSS in apps.shopify.com in the `DEMO` URL of the apps you create.

#POC

1. go to your partner account and create a new app
2. go to DEMO link in https://apps.shopify.com/services/app_submissions/edit# of your app 

put the payload you see below:

{F374863}

and when pressing on `preview changes` button and then pressing on `view example store` xss will fire as follows:

{F374865}


thanks!

## Impact

Stored XSS on apps.shopify.com

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
