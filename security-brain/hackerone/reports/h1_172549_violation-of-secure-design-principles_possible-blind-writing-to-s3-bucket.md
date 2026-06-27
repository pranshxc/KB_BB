---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172549'
original_report_id: '172549'
title: Possible Blind Writing to S3 Bucket
weakness: Violation of Secure Design Principles
team_handle: reverb
created_at: '2016-09-28T03:13:16.405Z'
disclosed_at: '2018-04-27T01:27:18.855Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- violation-of-secure-design-principles
---

# Possible Blind Writing to S3 Bucket

## Metadata

- HackerOne Report ID: 172549
- Weakness: Violation of Secure Design Principles
- Program: reverb
- Disclosed At: 2018-04-27T01:27:18.855Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
I noticed that you are using S3 and I believe I may have found one of your buckets and am able to write to it. However, I can not list the files in the bucket and such can not be 100% sure you own it. If you don't, I'd really appreciate being able to close this report myself or have you close it as informative to avoid the negative reputation/signal loss but respect your decision either way.

##Description
I noticed you are using the bucket reverb-files-staging. As such, I found reverb-ssh. Using the AWS CLI as an authenticated user, I am able to write to the bucket with the comment ```aws s3 cp teespring_buckets s3://reverb-ssh``` --- please excuse the file name, I uploaded the wrong test file.

After running the command I get ```upload: ./teespring_buckets to s3://reverb-ssh/teespring-buckets``` instead of an access denied message.

##Vulnerability
I'm reporting as I believe you likely own the bucket and if so, an attacker can write arbitrary files to the bucket which your team may trust seeing as the bucket appears to be for internal use. As a result, it could be possible to install malware on internal reverb machines to escalate an attack.

Please let me know if you have any questions.
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
