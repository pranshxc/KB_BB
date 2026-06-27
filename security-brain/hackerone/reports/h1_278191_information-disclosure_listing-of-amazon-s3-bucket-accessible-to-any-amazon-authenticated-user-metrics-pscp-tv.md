---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '278191'
original_report_id: '278191'
title: Listing of Amazon S3 Bucket accessible to any amazon authenticated user (metrics.pscp.tv)
weakness: Information Disclosure
team_handle: x
created_at: '2017-10-17T12:58:16.375Z'
disclosed_at: '2017-11-19T18:39:49.558Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: '*.pscp.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Listing of Amazon S3 Bucket accessible to any amazon authenticated user (metrics.pscp.tv)

## Metadata

- HackerOne Report ID: 278191
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2017-11-19T18:39:49.558Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
It's possible to get a listing of every files in the S3 bucket metrics.pscp.tv

**Description:** 
The problem is using the AWS command line, it's possible to get a listing of files in the Amazon S3 Bucket with an AWS authentication. See screenshot F230035. 

This user authentication is easy to get and it's free from Amazon. 

The good news is that the ACL on the files are set the way that's impossible at moment to create, remove or download any file from the bucket using my authentication.

A secure amazon S3 bucket would show Access Denied like the hackerone-attachements bucket in screenshot F230036

## Steps To Reproduce:
With the AWS command line installed and configured :
```
aws s3 ls s3://metrics.pscp.tv
```
## Impact: 
This give more information about your buckets to an attacker that are looking to attack you. 

Also, considering that it's possible to set the wrong ACL on a file that you may upload and may be confidential in the bucket, a secure bucket will remove the possibly to access it without a proper authentication.

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
