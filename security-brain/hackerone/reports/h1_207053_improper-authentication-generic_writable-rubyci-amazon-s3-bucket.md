---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '207053'
original_report_id: '207053'
title: Writable RubyCi Amazon s3 bucket
weakness: Improper Authentication - Generic
team_handle: ruby
created_at: '2017-02-17T06:43:02.543Z'
disclosed_at: '2017-02-27T02:05:26.852Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Writable RubyCi Amazon s3 bucket

## Metadata

- HackerOne Report ID: 207053
- Weakness: Improper Authentication - Generic
- Program: ruby
- Disclosed At: 2017-02-27T02:05:26.852Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, I have discovered that the bucket:
http://rubyci.s3.amazonaws.com/
is able to be written to by authenticated aws users. This is due to the current permissions configurations
I have added a file here:
http://rubyci.s3.amazonaws.com/test.html
for proof of concept. This can be potentially dangerous to your users and website, as any of the web content in this bucket may be replaced with malicious files. 
More info about these permissions can be found here: http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html

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
