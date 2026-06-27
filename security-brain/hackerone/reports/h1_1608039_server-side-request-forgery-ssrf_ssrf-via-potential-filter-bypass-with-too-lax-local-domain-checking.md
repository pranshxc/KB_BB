---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1608039'
original_report_id: '1608039'
title: SSRF via potential filter bypass with too lax local domain checking
weakness: Server-Side Request Forgery (SSRF)
team_handle: nextcloud
created_at: '2022-06-21T00:57:48.611Z'
disclosed_at: '2022-09-16T05:00:08.406Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF via potential filter bypass with too lax local domain checking

## Metadata

- HackerOne Report ID: 1608039
- Weakness: Server-Side Request Forgery (SSRF)
- Program: nextcloud
- Disclosed At: 2022-09-16T05:00:08.406Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi.
Reviewing the code for filtering for ssrf, in `preventLocalAddress`, we can see that it calls the function `ThrowIfLocalAddress()`. It has three common checks, first, it checks if the string is `localhost`, or if it ends in `.local` or `.localhost`
```php
		// Disallow localhost and local network
		if ($host === 'localhost' || substr($host, -6) === '.local' || substr($host, -10) === '.localhost') {
			$this->logger->warning("Host $host was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}
```
Second check, it checks if the provided url is only a host
```php
		// Disallow hostname only
		if (substr_count($host, '.') === 0 && !(bool)filter_var($host, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)) {
			$this->logger->warning("Host $host was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}
```
Lastly, it checks if the user input is an ip, if it is, it checks if it is not in the `FILTER_FLAG_NO_PRIV_RANGE`, or `FILTER_FLAG_NO_RES_RANGE`.
These checks lack something tho.  Checks for metadata. Specifically the Alibaba metadata, and google cloud metadata.    
Other metadata like aws and digital ocean uses 169.254.169.25 which is included in the `FILTER_FLAG_NO_RES_RANGE`. Google cloud metadata tho, can be accessed with http://metadata.google.internal  which is not in any checks from above. And the alibaba metadata can be accessed with `100.100.100.200`, this ip is neither in the `FILTER_FLAG_NO_PRIV_RANGE` or `FILTER_FLAG_NO_RES_RANGE` flags, also bypassing the check. 
This make it vulnerable to ssrf when the nextcloud host is hosted with either google cloud or alibaba

## Impact

SSRF filter bypass

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
