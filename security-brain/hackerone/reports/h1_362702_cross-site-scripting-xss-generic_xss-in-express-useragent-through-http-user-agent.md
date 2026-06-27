---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '362702'
original_report_id: '362702'
title: XSS in express-useragent through HTTP User-Agent
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nodejs-ecosystem
created_at: '2018-06-06T11:28:49.469Z'
disclosed_at: '2018-07-06T13:34:36.850Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: express-useragent
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in express-useragent through HTTP User-Agent

## Metadata

- HackerOne Report ID: 362702
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-07-06T13:34:36.850Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello, 

I would like to report an XSS in express-useragent  module  due  a lack of validating User-Agent header. Please note I already created an [Github issue](https://github.com/biggora/express-useragent/issues/98) and asked for CVE ( [CVE-2018-9863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-9863)). I did not know about Node.js third-party modules on hackerone.

## Description
express-useragent is simple NodeJS/ExpressJS middleware exposing User-Agent details to your application and views. Basically it parses User-Agent and return it in structured JSON format.

## The issue
while parsing User-Agent there are no escaping or sanitization mechanism. User-Agent header is controlled by the user. An attacker can craft a malicious script and inject it through the HTTP header.

## Steps to reproduce
* git clone https://github.com/biggora/express-useragent 
* cd express-useragent
* ```node test/http.js```  (an HTTP server should listen on 3000 tcp)
* ```curl "http://localhost:3000" -H 'User-Agent: <script>alert("XSS")</script>' > poc.html```
* open poc.html with your favorite web browser
* you should see an alertbox popup 

### Proof of concept (screenshots)
{F305913}
{F305914}

### Proof of concept with a fix (video) {F305912}

## Mitigation
Correctly escape and sanitize user input ( HTTP User-Agent ). Please note I proposed a fix in the video

## Impact

An attacker could execute javascript code that could lead to XSS.

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
