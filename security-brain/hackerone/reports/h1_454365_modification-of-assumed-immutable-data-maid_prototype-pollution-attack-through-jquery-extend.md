---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '454365'
original_report_id: '454365'
title: Prototype pollution attack through jQuery $.extend
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2018-12-03T15:53:20.718Z'
disclosed_at: '2019-04-02T15:53:17.576Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: jQuery
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# Prototype pollution attack through jQuery $.extend

## Metadata

- HackerOne Report ID: 454365
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2019-04-02T15:53:17.576Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report prototype pollution in jQuery.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** jquery
**version:** 3.3.1
**npm page:** `https://www.npmjs.com/package/jquery`

## Module Description

jQuery is a fast, small, and feature-rich JavaScript library.

## Module Stats

1.6M NPM downloads in the last week

But this is jQuery, so I'd expect there are quite a few more downloads outside of NPM.

# Vulnerability

## Vulnerability Description

`$.extend` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects. Note that only the "deep" version of `$.extend` is affected.

Users sometimes use `$.extend` for things like cloning an object or filling in defaults in an object with some options in it. It is not at all obvious that this is an unsafe operation.

It is a variant of this vulnerability:
https://hackerone.com/reports/310443

## Steps To Reproduce:

Craft an object with a named `__proto__` property, usually through `JSON.parse`, and pass it to `$.extend`:

```javascript
$.extend(true, {}, JSON.parse('{"__proto__": {"devMode": true}}'))
console.log({}.devMode); // true
```

## Supporting Material/References:

Tested on jQuery 3.3.1 (and a few older versions), using Chrome 70 and Firefox 63.

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

How to escalate this depends on the application. After obtaining prototype pollution, an attacker can generally change the default value for any option provided to a function that takes an "options" argument, which is a fairly common pattern in JavaScript.

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
