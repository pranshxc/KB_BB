---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1474017'
original_report_id: '1474017'
title: Open S3 Bucket Accessible by any  User
weakness: Information Disclosure
team_handle: omise
created_at: '2022-02-08T06:17:56.311Z'
disclosed_at: '2022-04-13T07:12:58.436Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- information-disclosure
---

# Open S3 Bucket Accessible by any  User

## Metadata

- HackerOne Report ID: 1474017
- Weakness: Information Disclosure
- Program: omise
- Disclosed At: 2022-04-13T07:12:58.436Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi team,
here i found Open S3 Bucket Accessible by any  User

vulnerable URL:
https://cdn2.omise.co/

bucket name  : `omise-cdn-2`

I haven't tried this yet as it may delete the bucket. (it is possible)
an Attacker can delete the bucket using this command:-
$ aws s3 rb s3://<The_bucket_name>
and claim the bucket again to takeover the bucket 

https://cdn2.omise.co/. (S3 misconfiguration), that allow to any user listing/read/download all folders/files.



i think somthing misconfiguration is happaening here, u cant read the bucket using Aws Cli but u can read it via browser.
and also u can download the file using both Aws Cli and Browser.

████████

download:

██████

## Impact

Sensitive information Leakage.
an Attacker can delete the bucket .and claim the bucket again to takeover the buckaet

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
