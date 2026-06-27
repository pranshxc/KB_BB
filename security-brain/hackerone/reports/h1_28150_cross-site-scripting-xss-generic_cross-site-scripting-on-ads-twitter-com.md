---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28150'
original_report_id: '28150'
title: Cross site scripting on ads.twitter.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-09-15T16:03:30.235Z'
disclosed_at: '2014-10-16T09:51:19.275Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross site scripting on ads.twitter.com

## Metadata

- HackerOne Report ID: 28150
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-10-16T09:51:19.275Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Steps to reproduce the issue:
1) Go to this link https://ads.twitter.com/accounts/XXXX/tweets where is XXXX is your account id.

2) Click on Compose Tweet option and enter "><svg/onload=prompt(123);>

3) Click on "Tweet" Button now.

You will prompt dialog box with "123" in it.

POC video: https://www.dropbox.com/s/64li7wv7gq2brlz/twitterxss.mov?dl=0

Please fix this.

Best Regards,
Anand Prakash

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
