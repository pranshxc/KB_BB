---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1416672'
original_report_id: '1416672'
title: Stored XSS in Question edit from product name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-12-04T09:47:34.480Z'
disclosed_at: '2022-03-31T14:02:29.856Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Question edit from product name

## Metadata

- HackerOne Report ID: 1416672
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2022-03-31T14:02:29.856Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @judgeme!

Step to reproduce:

1. Log in to your shopify account and create product with name `">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`
2. Go to our store and write question to our product with name `">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`
3. Then go to Shopify admin/Judge.me Product Reviews/Questions and edit question. XSS triage

{F1533755}


POC video:

{F1533757}

## Impact

Cookie stealer

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
