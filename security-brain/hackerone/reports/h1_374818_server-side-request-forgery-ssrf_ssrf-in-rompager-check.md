---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '374818'
original_report_id: '374818'
title: SSRF in rompager-check
weakness: Server-Side Request Forgery (SSRF)
team_handle: hannob
created_at: '2018-06-30T19:40:10.517Z'
disclosed_at: '2018-11-09T14:54:12.318Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: invalid.hboeck.de
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in rompager-check

## Metadata

- HackerOne Report ID: 374818
- Weakness: Server-Side Request Forgery (SSRF)
- Program: hannob
- Disclosed At: 2018-11-09T14:54:12.318Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary

The script `rompager.php` does not restrict which hosts can be requested. Thereby, an attacker can send HTTP requests to localhost and other servers of the same local network segment, on port 80 and 7547. 

## Description

In `rompager.php`, the value of `CURLOPT_URL` is fully controlled:

```php
<?php
// [...]
function checkHost($ip, $port) {
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "http://".$ip);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 1);
	curl_setopt($ch, CURLOPT_TIMEOUT, 1);
	curl_setopt($ch, CURLOPT_HEADER, TRUE);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
	curl_setopt($ch, CURLOPT_PORT, $port);
	$data = curl_exec($ch);
// [...]
	} else {
		$ip = $_GET['ip'];
	}
	output("<h4>Port 80</h4>\n");
	checkHost($ip, 80);
	output("<h4>Port 7547</h4>\n");
	checkHost($ip, 7547);
```

## Steps To Reproduce

  1. Access https://rompager.hboeck.de/?ip=localhost;
  1. Notice that *No RomPager found* is shown under *Port 80*.

## Impact

An attacker could force `rompager.hboeck.de` to perform HTTP requests to localhost or servers of the same local network segment.

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
