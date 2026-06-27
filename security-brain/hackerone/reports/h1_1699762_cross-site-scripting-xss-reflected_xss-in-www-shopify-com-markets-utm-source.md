---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1699762'
original_report_id: '1699762'
title: XSS in www.shopify.com/markets?utm_source=
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2022-09-14T08:30:04.081Z'
disclosed_at: '2022-10-18T07:14:46.052Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 147
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in www.shopify.com/markets?utm_source=

## Metadata

- HackerOne Report ID: 1699762
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2022-10-18T07:14:46.052Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, hope you are having a good day :)

## Summary:
I found a reflected XSS in `www.shopify.com/markets` using the `utm_source` parameter

Reflected XSS vulnerabilities arise when the application accepts a malicious input script from a user and then it is executed in the victim's browser. Since the XSS is reflected, the attacker has to trick the victim into executing the payload, usually using another website or by sending a specially crafted link

##### URL: `https://www.shopify.com/markets`
##### INJECTION POINT: `utm_source` parameter
##### PAYLOAD: `injection%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)`

## Steps To Reproduce:
Visit this URL:  
```
https://www.shopify.com/markets?utm_source=INJECTION%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)
```

By visiting that link you'll get an alert on your screen, that demonstrates the existence of the vulnerability.

{F1925617}

The attack is unauthenticated

## Recommended Fix
Correctly escape special characters such as `<` `>` `"` `'` based on the context where the string gets reflected.

Thank you.

## Impact

An attacker could steal user cookies, create a trusted phishing page or bypass any CSRF protection mechanism.

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
