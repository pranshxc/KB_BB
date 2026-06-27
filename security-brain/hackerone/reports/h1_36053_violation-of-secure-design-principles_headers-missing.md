---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36053'
original_report_id: '36053'
title: Headers Missing
weakness: Violation of Secure Design Principles
team_handle: x
created_at: '2014-11-14T23:56:56.549Z'
disclosed_at: '2014-11-15T00:37:09.515Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Headers Missing

## Metadata

- HackerOne Report ID: 36053
- Weakness: Violation of Secure Design Principles
- Program: x
- Disclosed At: 2014-11-15T00:37:09.515Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hellow Twiiter,

i found that some of the headers are missing on the domain ads.twitter,com!

                Name                               Actual Value                                   My Recommendation

strict-transport-security         max-age=631138519          Use 'max-age=31536000; includeSubDomains'
set-cookie                    guest_id=v1%3A141600...ov-2016 23:50:40 UTC                 Add 'secure; httponly;'
cache-control                       must-revalidate, private, max-age=0                     Add 'no-cache, no-store'
Pragma                                                                                                                            Use 'no-cache'
Expires                                                                                                                                   Use '-1'
X-Permitted-Cross-Domain-Policies                                                                                   Use 'master-only'
Content-Security-Policy                                Try Content-Security-Policy-Report-Only to start. Include default-                                      src 'self', avoid 'unsafe-inline' and 'unsafe-eval'    

content-security-policy-report-only          default-src 'self'; ...Y3PMNVQ%3D%3D%3D%3D;          Avoid 'unsafe-inline'. Avoid 'unsafe-eval'. Include default-src 'self', avoid 'unsafe-inline' and 'unsafe-eval'

Thanks

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
