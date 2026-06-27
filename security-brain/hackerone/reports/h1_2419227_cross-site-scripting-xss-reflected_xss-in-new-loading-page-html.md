---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2419227'
original_report_id: '2419227'
title: XSS in new.loading.page.html
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: gocd
created_at: '2024-03-16T22:27:20.147Z'
disclosed_at: '2024-03-17T14:06:19.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 58
asset_identifier: GoCD (https://www.gocd.org/download)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in new.loading.page.html

## Metadata

- HackerOne Report ID: 2419227
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: gocd
- Disclosed At: 2024-03-17T14:06:19.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Overview
The vulnerability arises from inadequate handling of query parameters, enabling attackers to insert `javascript:` URIs as redirectors within the `new.loading.page.html` file.

```js
var redirectToLanding = function() {
  var locationData = window.location.search.match(/(\?|&)redirect_to=([^&]+)(&|$)/);
  if (locationData === null) {
    window.location.reload(true);
  } else {
    window.location = decodeURIComponent(locationData[2]);
  }
}
```

[View Permalink](https://github.com/gocd/gocd/blob/0199f22311c83c88ee249a3a71907ce6f58ebd9f/jetty/src/main/resources/loading_pages/new.loading.page.html#L397-L404)

When the URL's query is `?redirect_to=javascript:alert("XSS")`, `locationData[2]` equals `'javascript:alert("XSS")'`. Subsequently, triggering `redirectToLanding` leads to XSS exploitation.

## Impact

Attackers can inject javascript: URIs to execute unauthorized scripts, potentially stealing sensitive information such as session cookies or performing actions on behalf of the user.

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
