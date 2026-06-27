---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '803922'
original_report_id: '803922'
title: Missing resource identifier encoding may lead to security vulnerabilities
weakness: Information Disclosure
team_handle: rails
created_at: '2020-02-24T20:41:03.367Z'
disclosed_at: '2020-05-13T18:18:36.253Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Missing resource identifier encoding may lead to security vulnerabilities

## Metadata

- HackerOne Report ID: 803922
- Weakness: Information Disclosure
- Program: rails
- Disclosed At: 2020-05-13T18:18:36.253Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

(I initially submitted this to the GitHub repository because the ActiveResource repository is not listed in scope. I was redirected here by @rafaelfranca)

A number of methods in the ActiveResource library, such as `ActiveResource::Base#find` and `ActiveResource::Base#exists?` don't URL encode the resource identifier that is passed to them. Consider the following code:

```ruby
require 'activeresource'
 
 class Test < ActiveResource::Base
   self.site = 'http://127.0.0.1:8080'
end

Test.exists? '?a=1'
```

The code above is expected to make a request to `http://127.0.0.1:8080/tests/%3fa%3d1.json` by properly URL encoding the resource identifier. Instead, it makes a request to `http://127.0.0.1:8080/tests/?a=1.json`.

This was tested against ActiveResource 5.1.0 and 5.0.0, both have the same unexpected behavior.

## Impact

Because the index `/tests/` returns an array of objects, the code will throw an exception. However, due to the time difference that could be observed, an attacker could potentially exploit this by injecting a filter parameter to index endpoint of the resource. E.g.

| Resource identifier | Objects returned | RTT |
| ---- | ---- | ---- |
| `?type=a&` | 1 | 500ms |
| `?type=b&` | 0 | 100ms |

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
