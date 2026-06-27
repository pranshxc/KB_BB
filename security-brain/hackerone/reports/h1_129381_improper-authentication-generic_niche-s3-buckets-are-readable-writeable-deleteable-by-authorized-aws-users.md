---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129381'
original_report_id: '129381'
title: niche s3 buckets are readable/writeable/deleteable by authorized AWS users
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2016-04-08T23:08:55.724Z'
disclosed_at: '2017-04-02T14:48:02.066Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- improper-authentication-generic
---

# niche s3 buckets are readable/writeable/deleteable by authorized AWS users

## Metadata

- HackerOne Report ID: 129381
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2017-04-02T14:48:02.066Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
I've discovered that the AWS buckets by niche, niche-s3-production,  is accessible for authorized AWS users using the AWS command line tools.

##Issue
As such, I have confirmed:
- I can list all files in the bucket with the command ``` aws s3 ls s3://niche-s3-production```
- I can copy files from the server with the command ``` aws s3 cp s3://niche-s3-production/[PATH]/[FILE] ./```
- I can copy to the server with ```aws s3 cp test.txt s3://niche-s3-production```
- I can remove files with ``` aws s3 rm s3://niche-s3-production/[PATH]/[FILE]```

You will see that I have left the empty file test.txt in the bucket root.

This also impacts the niche-s3-development and niche-s3-staging buckets.

##Vulnerability
- Authorized AWS users can access any content in the publics (I only tested downloading one file from the compaign_posts path because files can have their own permissions)
- People can host and serve viruses from your buckets
- Twitter staff may unknowingly download a virus from what they think is a trusted bucket when they think files may have been placed in specific locations by other coworkers

##Remediation
Remediation is to review, audit and update all buckets owned by niche and the access control lists so this is not available to authorized users, only via the web through an authorized account controlled by the site.

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
