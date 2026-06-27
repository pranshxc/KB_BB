---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '809212'
original_report_id: '809212'
title: No ACL on S3 Bucket in [https://www.██████████/]
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-03-03T03:51:49.031Z'
disclosed_at: '2020-05-14T17:56:32.379Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-access-control-generic
---

# No ACL on S3 Bucket in [https://www.██████████/]

## Metadata

- HackerOne Report ID: 809212
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2020-05-14T17:56:32.379Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team!,
* i was able to move and download all file in s3 bucket that's under ████ control cuz it didn't has ACL

## Step-by-step Reproduction Instructions
*  first we will try to access all files via browser by go to this `s3.amazonaws.com/files.████████`

## Now We Will try to download all files on the s3 bucket via aws cli:
1.  type this in ur terminal `aws s3 sync s3://files.█████████/ . --no-sign-request --region ██████`
1.  u will see that all files and folders starts to download!

## Now We will try to move a file into s3 bucket
1. i created a file and called the file `yghonem14.html`
1. now we will type this in terminal `aws s3 mv yghonem14.html s3://files.██████/  --no-sign-request --region ███████`

### PoC
* For more Proof i uploaded a file and u can access it by this url `https://s3.amazonaws.com/files.███/yghonem14.html` ████████

## Impact

* Attacker will be able to delete or move or access any file on the s3 bucket, Thanks!.

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
