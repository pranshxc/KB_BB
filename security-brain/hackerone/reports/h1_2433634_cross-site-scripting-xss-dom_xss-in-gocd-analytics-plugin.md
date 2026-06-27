---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2433634'
original_report_id: '2433634'
title: XSS in GOCD Analytics Plugin
weakness: Cross-site Scripting (XSS) - DOM
team_handle: gocd
created_at: '2024-03-25T18:10:28.669Z'
disclosed_at: '2024-03-27T01:47:30.965Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
asset_identifier: GoCD (https://www.gocd.org/download)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS in GOCD Analytics Plugin

## Metadata

- HackerOne Report ID: 2433634
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: gocd
- Disclosed At: 2024-03-27T01:47:30.965Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

[gocd/gocd-analytics-plugin (info-message.js#L28)](https://github.com/gocd/gocd-analytics-plugin/blob/c9b5f776539b3eb68dc3177c87b99b40319f8b22/assets/js/pages/info-message.js#L28) is vulnerable to XSS via the `?msg=` parameter. 
By supplying an attack payload such as `?msg=%3Csvg%2Fonload%3Dalert%28%22XSS%22%29%20%3E`, `<svg/onload=alert("XSS") >` will be injected into the webpage.

```js
$(document).ready(function () {
  const msg = window.location.search.match(/[&?]msg=([^&]+)/);
  const msgText = msg ? decodeURIComponent(msg[1]) : "No data collected for this metric, cannot generate analytics.";

  $(document.body).html(Utils.infoMessage(msgText));
});
```
> `Utils.infoMessage` basically just wraps `msgText` in a `</p>`

## Impact

An attacker can run malicious code on servers running this plugin, comprising the integrity and confidentiality of such servers.

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
