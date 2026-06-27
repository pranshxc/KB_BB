---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141244'
original_report_id: '141244'
title: XSS in zendesk.com/product/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2016-05-26T17:21:14.256Z'
disclosed_at: '2016-12-15T00:56:43.041Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in zendesk.com/product/

## Metadata

- HackerOne Report ID: 141244
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-12-15T00:56:43.041Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable urls:
https://www.zendesk.com/product/tour/
https://www.zendesk.com/product/pricing/
or just https://www.zendesk.com/product/

Vulnerable parameter is a **cvo_sid1**, used in **live.js**  to call convertro code (without sanitizing). This leads to generating malformed javascript answer with XSS injection ability. (See screenshots below).
There is a restriction on a semicolon use, so i replaced it with %3b.

To reproduce vulnerability, you could try this safe example:
`https://www.zendesk.com/product/tour/#?cvo_sid1=1")%3balert(document.cookie%2b"`

This vulnerability provides a great opportunity for victim to lose not only cookies, but also control over the account after stealth forwarding to porposely generated link like this :))

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
