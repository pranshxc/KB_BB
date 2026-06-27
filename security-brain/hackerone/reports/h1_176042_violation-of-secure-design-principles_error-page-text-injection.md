---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176042'
original_report_id: '176042'
title: Error Page Text Injection
weakness: Violation of Secure Design Principles
team_handle: yelp
created_at: '2016-10-15T19:43:55.206Z'
disclosed_at: '2017-11-09T20:11:37.669Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Error Page Text Injection

## Metadata

- HackerOne Report ID: 176042
- Weakness: Violation of Secure Design Principles
- Program: yelp
- Disclosed At: 2017-11-09T20:11:37.669Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Yelp team,

Description :

An attacker is able to inject his own text into error page and can fool the victim to visit his own malicious site.
Please take a look at attached document, it contains POC as well as attack scenario about how the attacker can exploit this vulnerability and mitigation.

POC URL: 

https://biz.yelp.com/%0A%0D*%20The%20web%20page%20you%20are%20trying%20to%20access%20has%20been%20moved%20to%20https://login.yelp.biz%20*/

OR

https://biz.yelp.com@goo.gl/LBwo5y

Regards,
Rohit

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
