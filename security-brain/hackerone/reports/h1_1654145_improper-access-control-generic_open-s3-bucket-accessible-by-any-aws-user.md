---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1654145'
original_report_id: '1654145'
title: Open S3 Bucket Accessible by any Aws User
weakness: Improper Access Control - Generic
team_handle: gocd
created_at: '2022-07-29T17:16:32.881Z'
disclosed_at: '2022-07-31T03:02:18.139Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: GoCD (https://www.gocd.org/download)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Open S3 Bucket Accessible by any Aws User

## Metadata

- HackerOne Report ID: 1654145
- Weakness: Improper Access Control - Generic
- Program: gocd
- Disclosed At: 2022-07-31T03:02:18.139Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Description:
It has been observed that the amazon s3 bucket which i believe belongs to GoCD as it contains data related to GoCD █████ documents and all is misconfigured as a result any unauthenticated users can access it without any restrictions
Step-by-step Reproduction Instructions
1.Access following URL
https://█████████.s3.amazonaws.com/ 
so the bucket name is "███"
2.And we can see that we are successfully able to see all the contents present on it.Which confirms s3 bucket is misconfigured.
3.And to access contents of different directories we can use following cmd in terminal
aws s3 ls s3://s3://███/binaries/
aws s3 ls s3://s3://█████/repodata/
aws s3 ls s3://s3://█████████/repoview/

and in a similar way ,we can access content of root or any directory which contains sensitive manuals , document and media files 
Suggested Mitigation/Remediation Actions : 
configure s3 bucket properly to disable listing of such a sensitive files

## Impact

Any unauthenticated user can access and download sensitive files present on GoCD s3 storage.

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
