---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128088'
original_report_id: '128088'
title: AWS S3 bucket writeable for authenticated aws users
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2016-04-04T02:56:49.136Z'
disclosed_at: '2016-04-05T13:06:28.383Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
tags:
- hackerone
- improper-authentication-generic
---

# AWS S3 bucket writeable for authenticated aws users

## Metadata

- HackerOne Report ID: 128088
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2016-04-05T13:06:28.383Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
I know that hackerone-attachments is used for file uploads on reports and so I did a quick scan for similar buckets and found &#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;. While I can't confirm if you own it or not, it appears that it is publicly writable using the aws cli.

When I tried to write to hackerone-attachments, I get:
"move failed: ./test.txt to s3://hackerone-attachements/test.txt A client error (AccessDenied) occurred when calling the PutObject operation: Access Denied.

However, when I write to &#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;, I get:
move: ./test.txt to s3://&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;/test.txt

Hopefully the bucket is yours and this isn't a waste of time. If you do own it, a good thing is the bucket is not publicly readable and the file appears private by default after being written. However, assuming you own it, the security issue would be someone writing something malicious and someone on your team unknowingly opening it.

Pete

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
