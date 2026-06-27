---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273557'
original_report_id: '273557'
title: ability to install paid themes for free
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2017-10-01T07:24:01.328Z'
disclosed_at: '2018-05-16T15:10:43.906Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: themes.shopify.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# ability to install paid themes for free

## Metadata

- HackerOne Report ID: 273557
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2018-05-16T15:10:43.906Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

#Discription
while searching for access control issues on shopify I noticed a subdomain of shopify https://themes.shopify.io which gave me the opportunity to install and download paid 
themes for free.

#POC

1. go to https://themes.shopify.io/login and login
2. select one of the paid themes and press on ``buy theme`` button
3. you will be facing this screen on your shop:
 {F225469}
4. press on ``apporve charge`` button and the theme will be installed after getting to this screen:
{F225470}

#IMPACT

any user can download any paid themes and also can save them and modify them to upload them again 

#FIX

you should limit the access to  https://themes.shopify.io/ since it is for testing only.

thanks.

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
