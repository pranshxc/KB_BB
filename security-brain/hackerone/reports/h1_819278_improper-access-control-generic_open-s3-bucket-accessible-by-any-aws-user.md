---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '819278'
original_report_id: '819278'
title: Open S3 Bucket Accessible by any Aws User
weakness: Improper Access Control - Generic
team_handle: greenhouse
created_at: '2020-03-14T16:00:00.651Z'
disclosed_at: '2020-05-01T07:24:01.976Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: www.greenhouse.io
asset_type: URL
max_severity: high
tags:
- hackerone
- improper-access-control-generic
---

# Open S3 Bucket Accessible by any Aws User

## Metadata

- HackerOne Report ID: 819278
- Weakness: Improper Access Control - Generic
- Program: greenhouse
- Disclosed At: 2020-05-01T07:24:01.976Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi team,

vulnerable URL: http://grnhse-marketing-site-assets.s3.amazonaws.com/

There is no authentication required to access the AWS bucket of the website.
As your site was associated with AWS, any AWS user can view the content , navigate through directories and download files, public access is allowed.

proof of concept: Please refer the screenshots attached.

[ note: I haven't modified any existing resources or harm any content ]

## Impact

Impact
1.      Sensitive information Leakage.
2.      Information disclosure about all the data in the cloud.

I haven't tried this yet as it may delete the bucket. (it is possible)
an Attacker can delete the bucket using this command:-
$ aws s3 rb s3://<The_bucket_name>
and claim the bucket again to takeover the bucket 

solution:
secure the login access

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
