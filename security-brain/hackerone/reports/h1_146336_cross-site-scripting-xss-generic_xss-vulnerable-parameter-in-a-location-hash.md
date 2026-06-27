---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146336'
original_report_id: '146336'
title: XSS vulnerable parameter in a location hash
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-06-22T00:31:15.340Z'
disclosed_at: '2019-10-16T09:47:48.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 443
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS vulnerable parameter in a location hash

## Metadata

- HackerOne Report ID: 146336
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2019-10-16T09:47:48.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi!

There is a vulnerability on your pages, using convertro.

Vulnerable parameter from location hash (cvo_sid1), used in your live.js to call convertro code without sanitizing. On the convertro side it is sanitized, but with help of this parameter you could push another parameter (typ), that leads to generating malformed javascript answer with XSS injection ability. Like this : cvo_sid1=111\u0026;typ=[code injection] , where \u0026; is an ampersand symbol.
See screenshots below.
There is a restriction on a semicolon use, so i replaced it with %3b.

To reproduce vulnerability, you could try this safe example:
https://slack.com/is#?cvo_sid1=111\u0026;typ=55577]")%3balert(document.cookie)%3b//

This vulnerability provides a great opportunity for victim to lose not only cookies, but also control over the account after stealth forwarding to porposely generated link like this. I think, you know ;)

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
