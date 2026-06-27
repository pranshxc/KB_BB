---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300812'
original_report_id: '300812'
title: Stored XSS in www.learnboost.com via ZIP codes.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2017-12-27T15:32:34.344Z'
disclosed_at: '2018-04-22T20:55:04.376Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in www.learnboost.com via ZIP codes.

## Metadata

- HackerOne Report ID: 300812
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2018-04-22T20:55:04.376Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary
---

www.learnboost.com is vulnerable to stored XSS via ZIP codes stored alongside school names in the *Network* panel. 

# Browsers Verified In
---

* Mozilla Firefox 58.0b12 (64-bit)

# PoC
---

Visit https://www.learnboost.com/settings/network/search and search for `fro`. My entry will trigger the XSS payload.

```html
"><img src=x onerror=alert(document.domain)>
```

{F249746}

## Impact

I now have stored XSS that triggers whenever someone searches for `fro`. If I were to map the payload to a very common search term (e.g. `aa`) that would increase the likelihood that my payload would fire.

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
