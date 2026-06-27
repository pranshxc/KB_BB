---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1276733'
original_report_id: '1276733'
title: S3 bucket Upload on studio.redditinc.com (s3-r-w.ap-east-1.amazonaws.com)
weakness: Improper Access Control - Generic
team_handle: reddit
created_at: '2021-07-24T14:50:52.097Z'
disclosed_at: '2021-10-21T20:00:28.449Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: '*.redditinc.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# S3 bucket Upload on studio.redditinc.com (s3-r-w.ap-east-1.amazonaws.com)

## Metadata

- HackerOne Report ID: 1276733
- Weakness: Improper Access Control - Generic
- Program: reddit
- Disclosed At: 2021-10-21T20:00:28.449Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings team,

Found a s3 bucket that belongs to studio.redditinc.com and properly not configured.

bucket name:- s3-r-w.ap-east-1.amazonaws.com
Bucket Source:-studio.redditinc.com

Steps To reproduce:-

In terminal , " dig studio.redditinc.com "
will get the CNAME as d326d3e45wj426.cloudfront.net

Then, "host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com"
will get 
d326d3e45wj426.s3.ap-east-1.amazonaws.com is an alias for s3-r-w.ap-east-1.amazonaws.com.
s3-r-w.ap-east-1.amazonaws.com name server ns-1885.awsdns-43.co.uk.
s3-r-w.ap-east-1.amazonaws.com name server ns-192.awsdns-24.com.
s3-r-w.ap-east-1.amazonaws.com name server ns-908.awsdns-49.net.
s3-r-w.ap-east-1.amazonaws.com name server ns-1338.awsdns-39.org.

So, I came to know that d326d3e45wj426.s3.ap-east-1.amazonaws.com is an alias for "s3-r-w.ap-east-1.amazonaws.com" 

Got the bucket name. Now I tried to upload by using command in authenticated  AWS CLI Machine
" aws s3 cp <path/filename> s3://s3-r-w

Uploaded was successful! Two files( dinesh.jpg and dinesh.html )

" aws s3 ls s3://<The_bucket_name> "
By this command I can list out  all the files in the bucket

I don't know is it possible or not. Attacker can delete the bucket using this command:-
" aws s3 rb s3://<The_bucket_name> "
and claim the bucket again to takeover the bucket.

Thanks team

## Impact

I can see every files present in the bucket .
I can upload any files . 
I can delete any file .

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
