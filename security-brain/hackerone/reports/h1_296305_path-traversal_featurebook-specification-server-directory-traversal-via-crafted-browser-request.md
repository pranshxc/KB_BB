---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '296305'
original_report_id: '296305'
title: '[featurebook] Specification Server Directory Traversal via Crafted Browser
  Request'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2017-12-08T17:26:43.462Z'
disclosed_at: '2018-01-10T20:43:30.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: featurebook
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [featurebook] Specification Server Directory Traversal via Crafted Browser Request

## Metadata

- HackerOne Report ID: 296305
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-01-10T20:43:30.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

A crafted request can be leveraged to traverse the directory structure of a host using the `featurebook` server package, and request arbitrary files outside of the specified web root.

## Module specification
* **Name**: [featurebook](https://www.npmjs.com/package/featurebook)
* **Version**: 0.0.32 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS

## Proof of concept

Please globally install the `featurebook` package and `cd` to a chosen directory (in this case, `/root`) on your test server. Run `featurebook serve --port 8081` to start serving from this location.

Substituting the `<server-IP>` value as appropriate, please browse to the following URL in Chrome. This will request the target `/etc/passwd` file and echo it line-by-line into an error message:

```
http://<server-IP>:8081/#/viewer/..%2f..%2fetc/passwd
```

{F245294}

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system configuration data.

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
