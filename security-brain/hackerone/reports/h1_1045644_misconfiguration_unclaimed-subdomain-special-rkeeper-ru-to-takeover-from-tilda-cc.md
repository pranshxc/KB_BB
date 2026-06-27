---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1045644'
original_report_id: '1045644'
title: unclaimed subdomain special.rkeeper.ru  to takeover from tilda.cc
weakness: Misconfiguration
team_handle: mailru
created_at: '2020-11-27T13:54:49.164Z'
disclosed_at: '2022-03-05T08:15:50.024Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
asset_identifier: Foodplex
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# unclaimed subdomain special.rkeeper.ru  to takeover from tilda.cc

## Metadata

- HackerOne Report ID: 1045644
- Weakness: Misconfiguration
- Program: mailru
- Disclosed At: 2022-03-05T08:15:50.024Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
http://special.rkeeper.ru/

Testing environment
--
*OS version, browser information, settings and prerequisites to reproduce vulnerability, testing tools used, etc*

Steps to reproduce: 
1. create account on tilda.cc
1. create a aproject then a domain will be assigned to your project like that `http://project3087915.tilda.ws` 
1. then go to settings and add domain special.rkeeper.ru 

POC :
http://special.rkeeper.ru/

--
Expected results, security impact description and recommendations
--



regards ^^

## Impact

can be used to bypass CORS and steal user data  
bypass SSO

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
