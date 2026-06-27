---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329950'
original_report_id: '329950'
title: '[public] Stored XSS in the filename when directories listing'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nodejs-ecosystem
created_at: '2018-03-26T10:40:55.911Z'
disclosed_at: '2018-06-12T08:04:30.316Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: public
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [public] Stored XSS in the filename when directories listing

## Metadata

- HackerOne Report ID: 329950
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-12T08:04:30.316Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Stored XSS issue in module **public**
It allows executing malicious javascript code in the user's browser.

# Module
**module name:** public
**version:** 0.1.3
**npm page:** https://www.npmjs.com/package/public

# Module Description
Run static file hosting server with specified public dir & port. Support a "direcotry index" like Apache httpd.

# Vulnerability
## Vulnerability Description
This issue happens because of the lack of output sanitization here:

```
files.forEach(function(file) {
    list.push('<li><a href="', path.join(base, file),'">', file, '</a></li>');
});
```   

# Steps To Reproduce:
* Install the module

`$ npm i public`

* Run

`$ ./node_modules/public/bin/public ./ 6060`

* In the target directory, create a file with name `"><svg onload=alert(3);`

`bash$ touch '"><svg onload=alert(3);'`

* In the browser, go to http://127.0.0.1:6060/, the XSS popup will fire.

{F278745}

# Supporting Material/References:
* macOS High Sierra 10.13.3
* node v8.10.0
* npm 5.6.0
* Chrome Version 65.0.3325.181 (Official Build) (64-bit)

# Wrap up
* I contacted the maintainer to let them know: N
* I opened an issue in the related repository: N

# Impact
It allows executing malicious javascript code in the user's browser

## Impact

It allows executing malicious javascript code in the user's browser.

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
