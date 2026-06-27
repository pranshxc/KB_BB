---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1173684'
original_report_id: '1173684'
title: index.php/apps/files_sharing/shareinfo endpoint is not properly protected
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2021-04-24T10:20:40.783Z'
disclosed_at: '2021-08-11T09:18:40.381Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# index.php/apps/files_sharing/shareinfo endpoint is not properly protected

## Metadata

- HackerOne Report ID: 1173684
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2021-08-11T09:18:40.381Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When federated shares between two Nextclouds are created they do not use standard webdav to communciate. But to obtain the filelist they seem to use the `SERVER/index.php/apps/files_sharing/shareinfo` endpoint.

Unlike the other endpoint for tokens (like public link shares). There is no brute force protection here. So this could be used as enumeration endpoint for available tokens. This is not likely to generate a hit due to the search space. But considering you do limit this on the public link endpoint for example it still seems relevant.

Now this brings me to the second part that struck me on this endpoint. It is essentially sending back the entire file tree below it. Meaning if this is a big file tree it you could just keep sending requests to the server keeping it quite busy. (and all requests are valid and won't be flagged). There is no rate limiting at all.

Then this brings me to the final part This endpoint accepts all token shares. Even link share tokens (meaning you don't even have to use the 'add to your Nextcloud'),  (and there is no check if federation is enabled). So in short. If you have a link share with a big file tree (or you create it yourself if there is write access).

## Impact

Possible to perform denial of service attacks by sending a lot of valid request that could lead to a significant number of queries and memory usage on the system.

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
