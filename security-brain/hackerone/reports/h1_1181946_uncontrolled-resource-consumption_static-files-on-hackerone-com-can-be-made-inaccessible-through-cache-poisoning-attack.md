---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1181946'
original_report_id: '1181946'
title: Static files on HackerOne.com can be made inaccessible through Cache Poisoning
  attack
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2021-05-01T13:20:16.400Z'
disclosed_at: '2021-12-22T23:36:39.112Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 212
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Static files on HackerOne.com can be made inaccessible through Cache Poisoning attack

## Metadata

- HackerOne Report ID: 1181946
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2021-12-22T23:36:39.112Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi,

The host hackerone.com uses cloudlfare to cache static files. The header x-forwarded-scheme can be used to cause a redirect loop, which will be cached by cloudflare. By taking down a JS file, it is possible to  cause a total loss of availability on hackerone.com 

### Disclaimer

No actual denial of service attack was caused in my testing. All the testing used cache-busters, meaning it did not affect the live website in any way

## Steps To Reproduce

1.  Send the following request:

```http
GET /assets/static/js/8.9572d249.chunk.js?hackerone=poc HTTP/2
Host: hackerone.com
x-forwarded-scheme: http

```

make sure to use a get parameter as a cachebuster

2.  You should notice a 301 redirect to the same page. Since the redirect poins to the same exact page, it will not be a redirect loop. The 301 is cached and removing the header will show the same redirect loop. 


### Video PoC

 ████

## Impact

The same attack that was reproduced on `/assets/static/js/8.9572d249.chunk.js?hackerone=poc` could be reproduced on the actual file without any random parameter. This would cause the file to no longer be accessible, hence causing a DoS on any pages relying on that js file. This works on any file that is cached on hackerone.com/*, including images, css files, js files  etc. Other than js files that would make the page unusuable, an attacker could also make images unavailable, etc.

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
