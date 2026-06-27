---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753399'
original_report_id: '753399'
title: Open redirect
weakness: Open Redirect
team_handle: nordsecurity
created_at: '2019-12-06T22:02:41.711Z'
disclosed_at: '2020-01-18T19:32:46.179Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 80
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect

## Metadata

- HackerOne Report ID: 753399
- Weakness: Open Redirect
- Program: nordsecurity
- Disclosed At: 2020-01-18T19:32:46.179Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following URL is vulnerable to an open redirect (it will redirect to google.com):
https://support.nordvpn.com/#/path///google.com
vulnerable code:
```
<script>
			if (window.location.href.indexOf('#/path') !== -1) {
				console.log("document.URL", document.URL)
				window.location.href = document.URL.slice(window.location.href.indexOf('#/path') + 6);
			}
		</script>
```

## Impact

Users could get redirected to malicious domain.

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
