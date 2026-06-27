---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '169759'
original_report_id: '169759'
title: Open redirect in bulk edit
weakness: Open Redirect
team_handle: shopify
created_at: '2016-09-16T05:46:18.316Z'
disclosed_at: '2016-12-04T12:54:10.843Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- open-redirect
---

# Open redirect in bulk edit

## Metadata

- HackerOne Report ID: 169759
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2016-12-04T12:54:10.843Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , 
I have found an open redirection issue when bulk editing resources.
#PoC:
Go to `https://<shop>.myshopify.com/admin/bulk?resource_name=Product&return_to=/..//evil.com` then click the **Close** button and you'll go to *evil.com* 

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
