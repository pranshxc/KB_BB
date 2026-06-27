---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173412'
original_report_id: '173412'
title: Full Sub Domain Takeover at s3.websummit.net
team_handle: websummit
created_at: '2016-10-01T19:21:41.653Z'
disclosed_at: '2017-02-02T11:10:45.859Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Full Sub Domain Takeover at s3.websummit.net

## Metadata

- HackerOne Report ID: 173412
- Weakness: 
- Program: websummit
- Disclosed At: 2017-02-02T11:10:45.859Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey

The sub domain at `s3.websummit.net` is pointing to `dws-content.s3-website-eu-west-1.amazonaws.com.`

> http://s3.websummit.net/

````
404 Not Found

    Code: NoSuchBucket
    Message: The specified bucket does not exist
    BucketName: s3.websummit.net
    RequestId: DB4C92F0D805D3F3
    HostId: NdSB/5EgNAiQz7B2pjzfBy5QwA6977cvAroA5vCyqfSsPR3nZLgdEyv4vQA4NCISzpILKP0WddM=
````

This means that the bucket has now expired and this  can now be claimed and content can be hosted on behalf of `http://s3.websummit.net/`

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
