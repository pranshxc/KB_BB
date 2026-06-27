---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115560'
original_report_id: '115560'
title: Two XSS vulns in widget parameters (all_collections.php and o2.php)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-02-09T16:17:29.588Z'
disclosed_at: '2016-08-02T03:50:50.352Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Two XSS vulns in widget parameters (all_collections.php and o2.php)

## Metadata

- HackerOne Report ID: 115560
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-08-02T03:50:50.352Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have found two additional possibilities of XSS attacks via the widget API endpoints: `https://www.zomato.com/widgets/all_collections.php` and `https://www.zomato.com/widgets/o2.php`

`https://www.zomato.com/widgets/all_collections.php` has a vulnerable `city_id` parameter that does not filter html or javascript:

https://www.zomato.com/widgets/all_collections.php?city_id=%22%3E%3Cimg%20src=http://goo.gl/JPx2sV%3E%3Cscript%3Ealert%28document.domain%29;%3C/script%3E%3Ca%20href=&language_id=alert%281%29&theme=red&csrf_token=bcac41f373322e378a299618228ad23b

The `https://www.zomato.com/widgets/o2.php` endpoint has a vulnerable `language_id` parameter, which does not filter html or js:

https://www.zomato.com/widgets/o2.php?theme=redar&sort=popularityo&csrf_token=bcac41f373322e378a299618228ad23b&language_id=%22}%27%29;alert%28document.domain%29;console.log%28%27

These URLs can be placed in <iframe> elements in an attacker-controlled website and any Zomato users visiting that site are open to executing arbitrary javascript in the zomato.com origin, which opens them to CSRF attacks and others. 

I have tested the other parameters and have found them to be sanitized.

These two parameters should be sanitized. 

Cheers!

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
