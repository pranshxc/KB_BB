---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1672459'
original_report_id: '1672459'
title: Cross-site scripting on api.collabs.shopify.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2022-08-17T13:49:53.453Z'
disclosed_at: '2022-10-13T18:12:46.766Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Cross-site scripting on api.collabs.shopify.com

## Metadata

- HackerOne Report ID: 1672459
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2022-10-13T18:12:46.766Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Shopify collabs (collabs.shopify.com) is a new platform for content creators / influencers to discover and advertise the millions of brands of Shopify. The content creators can apply for different brands on this platform and get paid (affiliate marketing).
I discovered a cross-site scripting vulnerability on this quite new domain. 

## Steps To Reproduce:

  1. Visit https://www.shopify.com/collabs/find-brands and click on "Apply for early access"
  2. Create a new Shopify ID / account
  3. You get redirected to https://collabs.shopify.com/onboarding:  
{F1871170}
  4. Connect your social media account to your profile (e.g. Instagram), edit your content, etc.
  5. You should now be successfully registered  (early bird access - waiting list):  
{F1871169}
  6. As you are logged in, open the URL `https://api.collabs.shopify.com/creator/auth/login?creator_redirect=javascript:alert(document.domain)` and you will see that the JavaScript has triggered:  
{F1871171}



## Supporting Material:
[list any additional material (e.g. screenshots, video, etc)]

  * [attachment / reference]

## Impact

* Execution of JavaScript code in the victim's browser => Execution of any future API functions of api.collabs.shopify.com in the name of the victim
* Exfiltration of confidential data
* etc.

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
