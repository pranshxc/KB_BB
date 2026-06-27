---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '110801'
original_report_id: '110801'
title: Internal GET SSRF via CSRF with Press This scan feature
weakness: Cross-Site Request Forgery (CSRF)
team_handle: automattic
created_at: '2016-01-14T22:11:01.564Z'
disclosed_at: '2016-03-04T10:14:19.660Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Internal GET SSRF via CSRF with Press This scan feature

## Metadata

- HackerOne Report ID: 110801
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: automattic
- Disclosed At: 2016-03-04T10:14:19.660Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
-----------------------------------
The url `http://xxx.xxx.xxx.xxx/wp-admin/press-this.php?u=URL_TO_SCRAPE&url-scan-submit=Scan` does not validate that user intends to send a scrape request.
The filter does not validate for `0.0.0.0:PORT` and allows the attacker to make the victim send GET request to servers priate127.0.0.1:PORT, localhost:PORT or anything which can be accessed via 0.0.0.0

So basicly a wordpress installations can send unwanted scrape/scan requests on behalf of their user invoked by the attacker. Including private connections via 0.0.0.0


Example
--------------------------------------- 
Victim is owner of myWordpress.com

- Victim is logged into Wordpress.
- Victim visits bad site with a content of`<img src="//myWordpress.com/wp-admin/press-this.php?u=htto://0.0.0.0:8080&url-scan-submit=Scan" /> 
-  Victim sends a unwanted request to their server requesting a internal server address to be hit.
- Server sends get request to 0.0.0.0:8080
- Servers private 127.0.0.1 answers back.

This example is with a private address, but it could also be a public. address

  
Fix
----------------------------------------
The scan/scrape should be a POST request using a csrf token or etc. 
The address 0.0.0.0 should not be allowd for scanning/scraping.

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
