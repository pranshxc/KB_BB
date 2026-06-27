---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229690'
original_report_id: '229690'
title: Amazon S3 bucket misconfiguration (share)
weakness: Improper Access Control - Generic
team_handle: zomato
created_at: '2017-05-18T17:46:35.997Z'
disclosed_at: '2017-05-18T17:57:47.078Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- improper-access-control-generic
---

# Amazon S3 bucket misconfiguration (share)

## Metadata

- HackerOne Report ID: 229690
- Weakness: Improper Access Control - Generic
- Program: zomato
- Disclosed At: 2017-05-18T17:57:47.078Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,


## Description

I have discovered one of your Amazon S3 bucket and tested it via the AWS command line tool on Linux. It looks like permissions are not well configured and allow dangerous actions to everyone.

The vulnerable bucket is:
`zomato-share`


## PoC:

`aws s3 ls s3://zomato-share`
`aws s3 cp test s3://zomato-share`
`aws s3 rm s3://zomato-share/test`

See the attached screenshots.

{F185826}


## Risk:

- Company impersonation, serve datas using your name
- Illegal file hosting (like movies, mp3 or whatever...)
- Files can be deleted
- Files can be overwritten by shitty content (like porn)
- Files can be infected by malicious content in an attempt to infect users or staff

Since the bucket doesn't host any critical files, the impact is very low but still something you have to fix for the reasons previously mentionned.


## Remediation:

Check all buckets owned by your company and the ACL to forbid dangerous actions to unauthorized users.


## Additional note:

Since there is no way to check the owner of a bucket, it's possible that those buckets don't belong to you. In that case, I strongly apologize for the disturbance.



Best regards,

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
