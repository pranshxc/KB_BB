---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507097'
original_report_id: '507097'
title: Open AWS S3 bucket leaks all Images uploaded to Zomato chat
weakness: Improper Authentication - Generic
team_handle: zomato
created_at: '2019-03-09T09:18:14.362Z'
disclosed_at: '2019-05-01T14:28:37.047Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Open AWS S3 bucket leaks all Images uploaded to Zomato chat

## Metadata

- HackerOne Report ID: 507097
- Weakness: Improper Authentication - Generic
- Program: zomato
- Disclosed At: 2019-05-01T14:28:37.047Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

**Summary:** 
The vulnerable bucket is `████images` and we can use 

`aws s3 ls s3://$bucketname/2019/1/` to retreive all images uploaded in 2019 and in January. Similarly we can use different years and months to retreive all images uploaded to Zomato Chat!

The images can be accessed at https://s3-ap-southeast-1.amazonaws.com/████████images/2019/1/{imageid}

## Supporting Material/References:
- {F438150}

Thanks,
Yash :)

## Impact

It could have contained User PII too, I haven't checked all the contents. Most of them are food photos :P, but it could easily have been PII if user uploaded some bill or something else that sort of.

An attacker can download all images in mass. Please secure the AWS bucket

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
