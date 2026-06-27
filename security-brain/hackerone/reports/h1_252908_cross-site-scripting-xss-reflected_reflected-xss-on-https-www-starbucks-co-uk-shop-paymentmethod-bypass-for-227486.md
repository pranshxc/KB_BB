---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '252908'
original_report_id: '252908'
title: Reflected XSS on https://www.starbucks.co.uk/shop/paymentmethod/ (bypass for
  227486)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: starbucks
created_at: '2017-07-24T08:14:25.062Z'
disclosed_at: '2020-06-16T21:19:02.783Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: www.starbucks.co.uk
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://www.starbucks.co.uk/shop/paymentmethod/ (bypass for 227486)

## Metadata

- HackerOne Report ID: 252908
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: starbucks
- Disclosed At: 2020-06-16T21:19:02.783Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

I am now able to prove my concerns from #227486 (see my last comment). `"`s are still not correctly encoded when rendered into the page in the `<link rel="canonical" href="current_full_url" />` element on almost any https://starbucks.co.uk/ page.

The WAF is bypassed by encoding `"`s as `%2522` in the URL path. This won't work when the payload is part of the query string.

**Description**

Take a look on the source code of https://www.starbucks.co.uk/shop/card/egift/anthing%2522. You can see a quote is injected to break the `href` attribute context.

```html
<link rel="canonical" href="https://www.starbucks.co.uk/shop/card/egift/anthing"" />
```

**Exploitation**

Using the same tricks as described in #227486 this injection can be leveraged to achieve arbitrary JS execution on `/shop/paymentmethod/`. Also note that this is just **one** example and more ways may exist to achieve JS execution. Steps to reproduce (use **Firefox**):

1. Login at https://www.starbucks.co.uk and add a card into basket on https://www.starbucks.co.uk/shop/card/egift/birthday
2. Visit https://www.starbucks.co.uk/shop/paymentmethod/hkjhk%2522onclick=%2522confirm(/-/g+this.ownerDocument.domain)%2522id=%2522checkoutButton
3. Click somewhere around the Checkout header. 
4. An alert showing the current domain pops up.

**Recommendation**

Again, correctly encode the URL before reflecting it back in the response. 

In #227486 the fix was blocking requests containing `%u0022` in the query string. This was shown to be bypassable so fixing this issue by blocking `%2522` in URL paths could be bypassed again in future.

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
