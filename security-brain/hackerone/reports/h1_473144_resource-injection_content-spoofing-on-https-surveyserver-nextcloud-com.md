---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '473144'
original_report_id: '473144'
title: Content spoofing on https://surveyserver.nextcloud.com
weakness: Resource Injection
team_handle: nextcloud
created_at: '2018-12-29T14:54:19.769Z'
disclosed_at: '2021-02-14T15:57:12.701Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: surveyserver.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- resource-injection
---

# Content spoofing on https://surveyserver.nextcloud.com

## Metadata

- HackerOne Report ID: 473144
- Weakness: Resource Injection
- Program: nextcloud
- Disclosed At: 2021-02-14T15:57:12.701Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi NextCloud team,
the `https://surveyserver.nextcloud.com` domain is vulnerable against `content spoofing` in the `forbidden page` due to the fact that the `request URI` is reflected without validation inside the aforementioned page.

1. Go on https://surveyserver.nextcloud.com/.htaccess%20because%20the%20webserver%20has%20been%20moved%20on%20http://evil.com%20and%20only%20an%20old%20version%20is%20present
2. Text injected successfully {F398692}

## Impact

Insert arbitrary text inside the `forbidden page` via `request URI`

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
