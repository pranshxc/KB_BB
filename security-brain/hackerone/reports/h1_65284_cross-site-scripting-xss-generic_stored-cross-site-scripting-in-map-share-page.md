---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65284'
original_report_id: '65284'
title: Stored Cross-Site Scripting in Map Share Page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mapbox
created_at: '2015-06-01T18:54:36.379Z'
disclosed_at: '2016-04-19T21:23:39.661Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored Cross-Site Scripting in Map Share Page

## Metadata

- HackerOne Report ID: 65284
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mapbox
- Disclosed At: 2016-04-19T21:23:39.661Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team Mapbox Security 
This is Copy From message email ( ‫security@mapbox.com‬ ) 

intro.
I'm Hussain Adnan Researcher Security,
Iam Have  Found  Vulnerability *Bug* in form project profile ( Map )

Type Vulnerability : Cross-Site Scripting ( Stored - Reflected ) 
Affected Domain : Affected Domain : mapbox.com - a.tiles.mapbox.com
link Demo to execute : Reflected 
~~~ 
https://a.tiles.mapbox.com/v4/ibmsecurity.ma91e43j/page.html?access_token=pk.eyJ1IjoiaWJtc2VjdXJpdHkiLCJhIjoiOWI0NDYxYjVmMjYzNjE2Yjc1ODM5NDgxOTBmMTFkODEifQ.EIBxJM1o7YiuI4pgZ7bsjg 
~~~
Code javascript  execute   in mapbox.com on form  search map edited.
and  execute    in a.tiles.mapbox.com on URL 

Steps to reproduce
-----
an attacker delete #  from  url  and  get  url  code  execute    Stored  - Reflected 
http://im54.gulfup.com/0gseLU.gif

----
POC   : https://youtu.be/N_4mqOtp07c - http://im54.gulfup.com/0gseLU.gif




Be Safe
Best Regards

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
