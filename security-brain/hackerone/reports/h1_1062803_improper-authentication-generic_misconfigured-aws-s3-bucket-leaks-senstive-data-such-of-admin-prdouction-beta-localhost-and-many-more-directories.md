---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1062803'
original_report_id: '1062803'
title: Misconfigured AWS S3 bucket leaks senstive data  such of  admin, Prdouction,beta,
  localhost and many more directories....
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2020-12-20T05:55:14.407Z'
disclosed_at: '2021-03-24T20:51:48.159Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Misconfigured AWS S3 bucket leaks senstive data  such of  admin, Prdouction,beta, localhost and many more directories....

## Metadata

- HackerOne Report ID: 1062803
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2021-03-24T20:51:48.159Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
It has been observed that the amazon s3 bucket which i believe belongs to DoD as it contains data related to Dod prod,admin,localhost documents and all is misconfigured as a result any unauthenticated users can access it without any restrictions

## Step-by-step Reproduction Instructions

1.Access following URL
https://██████.s3.amazonaws.com/
so the bucket name is "█████████"
2.And we can see that we are successfully able to see all the contents present on it.Which confirms s3 bucket is misconfigured.
3.And to access contents of different directories we can use following cmd in terminal

aws s3 ls s3://███/
aws s3 ls s3://████/██████/
aws s3 ls s3://███████/███████████████/
aws s3 ls s3://██████████/███████/
aws s3 ls s3://██████████/████/

and in a similar way ,we can access content of root or any directory which contains sensitive manuals , document and media files 

## Suggested Mitigation/Remediation Actions
configure s3 bucket properly to disable listing of such a sensitive files

## Impact

Any unauthenticated user can access and download sensitive files present on DoD s3 storage.

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
