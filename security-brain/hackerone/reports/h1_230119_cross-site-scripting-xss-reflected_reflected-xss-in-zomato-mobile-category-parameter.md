---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230119'
original_report_id: '230119'
title: Reflected XSS in Zomato Mobile - category parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: zomato
created_at: '2017-05-20T09:46:48.105Z'
disclosed_at: '2017-06-26T13:03:21.975Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in Zomato Mobile - category parameter

## Metadata

- HackerOne Report ID: 230119
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: zomato
- Disclosed At: 2017-06-26T13:03:21.975Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there. I have found a reflected XSS in Zomato.com mobile. This XSS affects mobile users of Zomato. Steps to reproduce:

1. Go to Zomato.com and change your user agent to mobile *(iPhone/Android user agent)*
2. Go to a certain restaurant/place and their photos *(e.g. site: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=ambience)*
3. Change the value in the ```category``` parameter to an XSS payload: ```
"--><%2Fscript><svg%2Fonload%3D'%3Balert(document.domain)%3B'>```
4. Final URL will look like this: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E

XSS will execute. POC attached.

Thanks and I hope you consider and fix this

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
