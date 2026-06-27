---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222040'
original_report_id: '222040'
title: Reflected XSS at https://da.wordpress.org/themes/?s= via "s=" parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: wordpress
created_at: '2017-04-18T23:43:15.856Z'
disclosed_at: '2017-07-26T18:16:55.372Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://da.wordpress.org/themes/?s= via "s=" parameter

## Metadata

- HackerOne Report ID: 222040
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: wordpress
- Disclosed At: 2017-07-26T18:16:55.372Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello - 

You have a reflected XSS vulnerability located at this domain:

https://da.wordpress.org/themes/?s=

This was tested on the latest version of Chrome (Version 57.0.2987.133 (64-bit)

By entering this payload in the URL, you are able to execute a script to fire:

`1%3C!%27/*%22/*\%27/*\%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm`1`%20//%3E#`

Note that the "1" in the confirm is enclosed in backticks, the HackerOne editor just makes it difficult to show. I have attached a screenshot to show the full URL, as well as included it below: 

https://da.wordpress.org/themes/?s=1%3C!%27/*%22/*\%27/*\%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm`1`%20//%3E#

Please let me know if you have any other questions, thanks!

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
