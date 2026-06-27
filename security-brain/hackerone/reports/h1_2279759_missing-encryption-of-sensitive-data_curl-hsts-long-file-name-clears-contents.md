---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2279759'
original_report_id: '2279759'
title: curl HSTS long file name clears contents
weakness: Missing Encryption of Sensitive Data
team_handle: ibb
created_at: '2023-12-10T13:40:42.322Z'
disclosed_at: '2024-01-20T17:17:39.985Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- missing-encryption-of-sensitive-data
---

# curl HSTS long file name clears contents

## Metadata

- HackerOne Report ID: 2279759
- Weakness: Missing Encryption of Sensitive Data
- Program: ibb
- Disclosed At: 2024-01-20T17:17:39.985Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## VULNERABILITY
When saving HSTS data to an excessively long file name, curl could end up removing all contents, making subsequent requests using that file unaware of the HSTS status they should otherwise use.

## INFO
The reason for this bug is that save function appended a suffix to the file name, created a temporary file and then in the last step renamed that to the final name. When the file name length was close to the limit of what is allowed on the file system, adding the extension would make it too long and then trigger this bug.

## Hackerone ticket #2236133

## Impact

HSTS bypass

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
