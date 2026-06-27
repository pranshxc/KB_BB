---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '308158'
original_report_id: '308158'
title: '[html-janitor] Bypassing sanitization using DOM clobbering'
weakness: Business Logic Errors
team_handle: nodejs-ecosystem
created_at: '2018-01-23T12:47:54.192Z'
disclosed_at: '2018-02-05T17:54:24.558Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: html-janitor
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# [html-janitor] Bypassing sanitization using DOM clobbering

## Metadata

- HackerOne Report ID: 308158
- Weakness: Business Logic Errors
- Program: nodejs-ecosystem
- Disclosed At: 2018-02-05T17:54:24.558Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Module:**

Name: [html-janitor](https://www.npmjs.com/package/html-janitor)
Version: 2.0.2

**Summary:**

Arbitrary HTML can pass the sanitization process, which can be unexpected and dangerous (XSS) in case user-controlled input is passed to the clean function.

**Description:**

Proof of concept:

```javascript
var myJanitor = new HTMLJanitor({tags:{p:{}}});
var cleanHtml = myJanitor.clean("<form><object onmouseover=alert(document.domain) name=_sanitized></object></form>")
console.log(cleanHtml) // logs: <form><object onmouseover=alert(document.domain) name=_sanitized></object></form>
```
The following check can be leveraged to bypass the whole sanitization process:

```javascript
do {
  // Ignore nodes that have already been sanitized
  if (node._sanitized) {
      continue;
  }
...
```

As `node` is the first child in the created tree walker (i.e. in this case the `<form>` tag) `node._sanitized` will point to the inner `<object>` and the check passes.

To learn more about DOM clobbering see: https://www.youtube.com/watch?v=5W-zGBKvLxk (by Mario Heiderich)

**Recommendation:**

It should be enough to set `node._sanitized` to `false` every time a new node is being processed. 

*Note that I previously reported this issue at https://github.com/guardian/html-janitor/issues/35*

## Impact

Given the module's description I would assume it should be used to prevent XSS vulnerabilities. This is currently a very dangerous assumption given that the whole sanitization process can be bypassed.

Note that the author might have never intended to feed untrusted data into the clean() function. In that case this is *just* a regular issue. Furthermore, the fact that untrusted data is unexpected should be at least mentioned in the documentation, because other developers most certainly will use the package in such scenarios.

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
