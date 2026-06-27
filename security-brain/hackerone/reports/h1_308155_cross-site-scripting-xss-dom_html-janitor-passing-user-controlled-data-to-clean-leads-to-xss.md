---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '308155'
original_report_id: '308155'
title: '[html-janitor] Passing user-controlled data to clean() leads to XSS'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: nodejs-ecosystem
created_at: '2018-01-23T12:34:13.662Z'
disclosed_at: '2018-02-09T15:00:45.549Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: html-janitor
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [html-janitor] Passing user-controlled data to clean() leads to XSS

## Metadata

- HackerOne Report ID: 308155
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: nodejs-ecosystem
- Disclosed At: 2018-02-09T15:00:45.549Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Module:**

* Name: [html-janitor](https://www.npmjs.com/package/html-janitor)
* Version: 2.0.2

**Summary:**

Passing user-controlled data to the module's clean() function can result in arbitrary JS execution, because of unsafe DOM operations. 

The description "*Cleans up your markup and allows you to take control of your HTML. HTMLJanitor uses a defined whitelist to limit HTML it is given to a defined subset.*" implies that "dirty" HTML is expected and therefore I would assume the clean method should never result in arbitrary JS being executed.

**Description:**

The following will result in JS execution:
```javascript
var myJanitor = new HTMLJanitor({tags:{p:{}}});
var cleanHtml = myJanitor.clean("<p><img src onerror=alert()><p>")
```

because [of this code](https://github.com/guardian/html-janitor/blob/master/src/html-janitor.js#L44):

```js
HTMLJanitor.prototype.clean = function (html) {
    var sandbox = document.createElement('div'); // This is not a safe way to create a sandbox.
    sandbox.innerHTML = html; // At this point, the onerror in the img is triggered.
```

**Recommendation:**

The "sandbox" should be created using safe browser APIs such as `document.implementation.createHTMLDocument();`.

*Note that I previously reported this issue at https://github.com/guardian/html-janitor/issues/34*

## Impact

Given the module's description I would assume it should be used to prevent XSS vulnerabilities. This is currently a very dangerous assumption given that the module itself has a XSS vulnerability. 

Note that the author might have never intended to feed untrusted data into the clean() function. However, in that case this should be at least mentioned in the documentation, because other developers most certainly will use the package in such scenarios.

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
