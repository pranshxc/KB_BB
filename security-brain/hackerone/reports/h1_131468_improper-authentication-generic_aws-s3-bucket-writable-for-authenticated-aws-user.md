---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131468'
original_report_id: '131468'
title: AWS S3 bucket writable for authenticated aws user
weakness: Improper Authentication - Generic
team_handle: udemy
created_at: '2016-04-17T03:20:50.710Z'
disclosed_at: '2017-01-05T01:34:01.511Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# AWS S3 bucket writable for authenticated aws user

## Metadata

- HackerOne Report ID: 131468
- Weakness: Improper Authentication - Generic
- Program: udemy
- Disclosed At: 2017-01-05T01:34:01.511Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I found an open S3 Amazon bucket udemy-maven. While I can’t confirm if you own it or not, it appears that it is publicly writable using the aws cli.

When I write to udemy-maven, I get:
move: ./test.txt to s3://udemy-maven/test.txt

And also when I remove file, I get:
delete: s3://udemy-maven/test.txt

Assuming you own it, the security issue is that someone could delete files or write something malicious into the bucket and someone on your team unknowingly opening it.

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
