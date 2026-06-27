---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '664161'
original_report_id: '664161'
title: Information disclosure (system username, server info) in the x-amz-meta-s3cmd-attrs
  response header on data.gov
weakness: Information Disclosure
team_handle: gsa_bbp
created_at: '2019-08-04T09:41:20.270Z'
disclosed_at: '2019-08-06T15:42:58.225Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Information disclosure (system username, server info) in the x-amz-meta-s3cmd-attrs response header on data.gov

## Metadata

- HackerOne Report ID: 664161
- Weakness: Information Disclosure
- Program: gsa_bbp
- Disclosed At: 2019-08-06T15:42:58.225Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi Team,

I noticed, that the x-amz-meta-s3cmd-attrs  response header returns sensitive information, like system username on data.gov

x-amz-meta-s3cmd-attrs: uid:0/gname:root/uname:root/gid:0/mode:33184/mtime:1513269652/atime:1513269652/md5:2049644b6b833f5dbb826f60a4721f64/ctime:1513269652

Server: AmazonS3

Steps to reproduce:

1. POST  https://www.data.gov/app/plugins/advanced-custom-fields/core/api.php
2. Intercept the request in burp and see the response header values with system username information



Suggested fix
This issue lies in the s3cmd repository: https://github.com/s3tools/s3cmd/issues/67
where suggested fix is adding the -- no-preserve command.

## Impact

The attacker can gain sensitive information about system username. In this case it was root, so i marked impact as Low. Still, the developers can have a good reason to not expose this information in the response header.

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
