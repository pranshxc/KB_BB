---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1428207'
original_report_id: '1428207'
title: 'Stored XSS in Question edit for product name (bypass #1416672)'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-12-15T21:24:16.572Z'
disclosed_at: '2022-03-31T14:01:04.420Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Question edit for product name (bypass #1416672)

## Metadata

- HackerOne Report ID: 1428207
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2022-03-31T14:01:04.420Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @judgeme!
Step to reproduce:
1. Log in to your shopify account and create product with name `&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;`
2. Go to our store and write question to our product with name `&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;`
3. Then delete our product from store (The product status must be (out of store) in questions.
4. Then go to Shopify admin/Judge.me Product Reviews/Questions and edit question. XSS triage


{F1547145}


POC video

{F1547181}

## Impact

session stealer

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
