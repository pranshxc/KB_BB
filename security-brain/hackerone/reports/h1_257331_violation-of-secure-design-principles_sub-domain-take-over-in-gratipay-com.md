---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '257331'
original_report_id: '257331'
title: Sub domain take over in gratipay.com
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-08-07T08:18:08.540Z'
disclosed_at: '2017-08-08T16:04:50.362Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://gratipay.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Sub domain take over in gratipay.com

## Metadata

- HackerOne Report ID: 257331
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-08-08T16:04:50.362Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

# Summary

Sub domain take over in gratipay.com

# Description

I scanned gratipay.com using knockpy to find the sub domains. I found one subdomain
'www.gratipay.com.herokudns.com'. But this sub domain is not registered in heroku. An attacker can buy this sub domain from heroku. 

# Browsers Verified In

  * Firefox
  * Chrome

# Steps To Reproduce

  1. use the 'knockpy gratipay.com' command in  knockpy to find sub domains
       .
       You will get one domain like 'www.gratipay.com.herokudns.com'.
  1. Test this domain in browser. Then you will get error message from heroku. Please refer attached screen shot for more clarity.

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
