---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1589847'
original_report_id: '1589847'
title: Heap overflow via HTTP/2 PUSH_PROMISE
weakness: Heap Overflow
team_handle: curl
created_at: '2022-06-02T15:29:52.702Z'
disclosed_at: '2022-06-05T20:59:34.216Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- heap-overflow
---

# Heap overflow via HTTP/2 PUSH_PROMISE

## Metadata

- HackerOne Report ID: 1589847
- Weakness: Heap Overflow
- Program: curl
- Disclosed At: 2022-06-05T20:59:34.216Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
libcurl HTTP/2 support processes incoming `PUSH_PROMISE` headers by storing them in an array. The code initially allocates storage for 10 headers and then keeps doubling the array size as needed: 
```
      stream->push_headers_alloc *= 2;
      headp = Curl_saferealloc(stream->push_headers,
                               stream->push_headers_alloc * sizeof(char *));
```
(https://github.com/curl/curl/blob/07a9b89fedaec60bdbc254f23f66149b31d2f8da/lib/http2.c#L1053)

On 32-bit platforms after receiving 10 << 26 headers the the allocation size will overflow, resulting in too little memory being allocated (`(10 << 27) * sizeof(char *)` will be truncated to lower 32-bit resulting in 1 GB storage being allocated) for the array. Subsequently the pointers will be written to unallocated memory by `stream->push_headers[stream->push_headers_used++] = h;`

## Steps To Reproduce:
  1. Have HTTP2 server  that sends more than 1 << 26 `PUSH_PROMISE` headers
  2. `curl https://targetsite`

The fix is to limit the amount of promise headers that are accepted and return error if too many are received.

## Impact

Heap overflow.

This issue is likely very hard to trigger as it requires a system where realloc for `(1 << 26) * sizeof(char *)` bytes is successful.  This is rather rare. In addition to be exploitable in other than denial of service capacity the attacker would need to find out some way  way to obtain code execution by the array overflow. This would  likely work by having some object get  allocated to the newly released heap memory and then get overwritten by this array pointer write. An example would be an object that has pointer to command to execute.

As such the practical impact of this vulnerability is low.

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
