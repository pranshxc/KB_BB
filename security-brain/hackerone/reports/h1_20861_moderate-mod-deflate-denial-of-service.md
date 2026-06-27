---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20861'
original_report_id: '20861'
title: 'moderate: mod_deflate denial of service'
team_handle: ibb
created_at: '2014-02-19T00:00:00.000Z'
disclosed_at: '2014-07-14T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Apache (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# moderate: mod_deflate denial of service

## Metadata

- HackerOne Report ID: 20861
- Weakness: 
- Program: ibb
- Disclosed At: 2014-07-14T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A resource consumption flaw was found in mod_deflate. If request body decompression was configured (using the "DEFLATE" input filter), a remote attacker could cause the server to consume significant memory and/or CPU resources. The use of request body decompression is not a common configuration.

Acknowledgements: This issue was reported by Giancarlo Pellegrino and Davide Balzarotti

Resolved in Apache httpd 2.4.10-dev: http://httpd.apache.org/security/vulnerabilities_24.html

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
