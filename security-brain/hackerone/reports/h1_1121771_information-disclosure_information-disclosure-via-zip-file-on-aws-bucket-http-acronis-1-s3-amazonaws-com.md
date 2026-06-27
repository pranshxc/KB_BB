---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1121771'
original_report_id: '1121771'
title: Information Disclosure via ZIP file on AWS Bucket [http://acronis.1.s3.amazonaws.com]
weakness: Information Disclosure
team_handle: acronis
created_at: '2021-03-09T20:14:50.996Z'
disclosed_at: '2022-02-08T09:08:38.182Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Information Disclosure via ZIP file on AWS Bucket [http://acronis.1.s3.amazonaws.com]

## Metadata

- HackerOne Report ID: 1121771
- Weakness: Information Disclosure
- Program: acronis
- Disclosed At: 2022-02-08T09:08:38.182Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary

Hello, @acronis Team I hope you all doing well.

during My recon, I found OPEN S3 BUCKET  http://acronis.1.s3.amazonaws.com and this BUCKET has an ZIP file .
and this file contains sensitive information about the internal system of Acronis.

This Zip file Is from  2018.  And it looks like it was in the development environment. but some employees uploaded this backup to OPEN S3 BUCKET.
and An attacker can download this file and read it .


## Steps To Reproduce

  1. go to http://acronis.1.s3.amazonaws.com/sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip and download The Zip file .

by Extracting this Zip file you can see the sensitive information about the internal system.

### POC 

{F1224411}

## Recommendations

delete `sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip` file from this OPEN S3 BUCKET.

## Impact

Information Disclosure About internal system.
HTTP logs Disclosure.
leak Admin JWT token 
{F1224410}

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
