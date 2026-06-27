---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200419'
original_report_id: '200419'
title: Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: pushwoosh
created_at: '2017-01-22T21:28:26.362Z'
disclosed_at: '2017-02-02T11:32:17.453Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking

## Metadata

- HackerOne Report ID: 200419
- Weakness: UI Redressing (Clickjacking)
- Program: pushwoosh
- Disclosed At: 2017-02-02T11:32:17.453Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Steps to reproduce:

create index.html file with following content:
<iframe sandbox="allow-scripts allow-forms" src="https://go.pushwoosh.com/register" width="1000" height="600"></iframe>

Open index.html in browser

Actual result: Pushwoosh viewed in iframe.
Expected result: do not allow clickjacking
Root cause:

```
var isInIFrame = (function () {
			try {
				return window.self !== window.top;
			} catch (e) {
				return true;
			}
		})();
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
