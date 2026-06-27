---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1285598'
original_report_id: '1285598'
title: s3 bucket takeover presented in https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh
weakness: Business Logic Errors
team_handle: reddit
created_at: '2021-07-31T17:51:58.721Z'
disclosed_at: '2021-10-21T19:48:20.227Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 82
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# s3 bucket takeover presented in https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh

## Metadata

- HackerOne Report ID: 1285598
- Weakness: Business Logic Errors
- Program: reddit
- Disclosed At: 2021-10-21T19:48:20.227Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey team,

## Summary:
 I have found that in the code of full-build-macos.sh in rpanstudio on github(https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/install-dependencies-osx.sh) contains a  s3 bucket which was unclaimed i.e (https://obs-nightly.s3-us-west-2.amazonaws.com)

## Steps To Reproduce:
1. Create a s3 bucket with name obs-nightly and us west 2 region
2. Upload files  with the name same as given in the code  (e.g. cef_binary_${1}_macosx64.tar.bz2)
3. Make the settings and change it as a static website 
4. You have successfully taken the s3 bucket and now when any user runs the code the url with s3 get executed and an attacker can spread dangerous malware.

## POC:

1. Link for the s3 bucket takenover :- https://obs-nightly.s3-us-west-2.amazonaws.com/index.html
{F1395337}

2. Github link that shows the s3 bucket :- https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/install-dependencies-osx.sh
{F1395340}
3. Github link that shows the s3 bucket :- https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh
{F1395338}

##Remediaton
You should remove the unclaimed s3 bucket as soon as possible from both the codes as it possess a critical risk

## Impact

An attacker can takeover the s3 bucket and can host his malicious content with the name (cef_binary_${1}_macosx64.tar.bz2) as presented in the code and can spread ransomware and many malicious files. This bug has a critical impact because the code of the tool that many people uses, contains unclaimed s3 bucket.

Regards,
Gaurav Bhatia

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
