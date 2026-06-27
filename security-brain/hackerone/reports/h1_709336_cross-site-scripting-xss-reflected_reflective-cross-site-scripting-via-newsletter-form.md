---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '709336'
original_report_id: '709336'
title: Reflective Cross-site Scripting via Newsletter Form
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2019-10-08T02:36:01.197Z'
disclosed_at: '2019-10-11T17:38:59.054Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflective Cross-site Scripting via Newsletter Form

## Metadata

- HackerOne Report ID: 709336
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2019-10-11T17:38:59.054Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

*.myshopify.com is vulnerable to a reflective cross-site scripting attack in the newsletter form. This can be crafted to trigger on a page load without any further user interaction.

The following example url shows this vulnerability:
```
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

This was tested on a newly registered store "testbuguser.myshopify.com"

If you require any additional details, please do not hesitate to bump.

## Impact

This attack could be leveraged to compromise administrative sessions or perform actions on behalf of users with the same level of privilege as the user.

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
