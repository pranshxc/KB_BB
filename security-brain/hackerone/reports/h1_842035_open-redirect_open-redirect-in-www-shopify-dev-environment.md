---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '842035'
original_report_id: '842035'
title: Open Redirect in  www.shopify.dev Environment
weakness: Open Redirect
team_handle: shopify
created_at: '2020-04-06T23:24:23.133Z'
disclosed_at: '2021-11-18T19:12:15.693Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Shopify Third Party Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- open-redirect
---

# Open Redirect in  www.shopify.dev Environment

## Metadata

- HackerOne Report ID: 842035
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2021-11-18T19:12:15.693Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Reported vulnerability allows attacker for open/unknown redirect for victim user 

## Steps to reproduce

1) Go to https://shopify.dev/concepts/shopify-introduction
2) Click on search
3) Type ``` POC ``` in search box and hit enter 
4) Right click on first result displayed as ```POS``` and click on copy  link address which will look like below.
```
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=%2Ftools%2Fapp-bridge%2Factions%2Fpos&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false
```
5) Modify ```result_url``` parameter in link shown above to ```result_url=@www.facebook.com```

6) Final link will look like this
```
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false

```
7) alternatively You can also directly  access below link for your convenience
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false


Culprit for redirect is ``` @ ``` character which will bypass the logic implemented to redirect user to access resource on www.shopify.dev itself and follow url after ``` @ ``` 


Note: I am submitting this report as this bypass technique can be use to any other domain on Shopify if same logic is implemented and could leads attacker for wider attack scope.


Thanks you!

## Impact

Invalidated Redirect

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
