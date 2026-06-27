---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '396370'
original_report_id: '396370'
title: 'XSS: Group search terms'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: vanilla
created_at: '2018-08-17T07:14:52.920Z'
disclosed_at: '2019-05-01T18:02:42.252Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 105
asset_identifier: '*.vanillastaging.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS: Group search terms

## Metadata

- HackerOne Report ID: 396370
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: vanilla
- Disclosed At: 2019-05-01T18:02:42.252Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The sub domain https://kentico.vanillastaging.com has a DOM XSS can be executed on any user browser by a simple get request.

**Description:**
The search param in the get request has been set in it's text value and the response has been reflected in the DOM response.
Request:
GET /groups/browse/search?Search=e<WJFJRC>1M2OQ[!%2b!]</WJFJRC> HTTP/1.1
Referer: https://kentico.vanillastaging.com/
Cookie: __cfduid=da777cec228cb1d941f54d1e059d96a1b1534336176; vf_kentico_QPFNH-Vv=1534336219; ARRAffinity=73b72a809b9ab033e2f42e73d768c48b345f903bbe17688e3758d2fd3fa0bf8a; __vnOz0=1534336231; __vnOz1=1534336231
Host: kentico.vanillastaging.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

## Steps to reproduce:

1. Filter all input for the search param
2. Remove the spcial chars when the application render the results

## Impact

Account Hijacking, Stealing Credentials.

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
