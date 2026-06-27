---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142709'
original_report_id: '142709'
title: Fetching external resources through svg images
weakness: Information Disclosure
team_handle: shopify
created_at: '2016-06-02T17:29:07.599Z'
disclosed_at: '2016-06-21T06:19:16.999Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- information-disclosure
---

# Fetching external resources through svg images

## Metadata

- HackerOne Report ID: 142709
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2016-06-21T06:19:16.999Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found the exactly same bug #97501 at ``https://app.shopify.com/services/partners/api_clients/<APP-ID>`` when uploading the svg image on app icon.

###Steps to reproduce it

+ Make a new app at https://app.shopify.com/services/partners/api_clients
+ Goto app setting ``https://app.shopify.com/services/partners/api_clients/<APP-ID>``
+ Now upload the attached svg image and change the xlink with your owner.
+ Save changes and check your server log. 

{F97509}

Thanks

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
