---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '474798'
original_report_id: '474798'
title: Subdomain takeover on healthyhackathon.khanacademy.org and hackweek.khanacademy.org
weakness: Improper Access Control - Generic
team_handle: khanacademy
created_at: '2019-01-04T17:57:56.717Z'
disclosed_at: '2019-08-25T07:02:41.660Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- improper-access-control-generic
---

# Subdomain takeover on healthyhackathon.khanacademy.org and hackweek.khanacademy.org

## Metadata

- HackerOne Report ID: 474798
- Weakness: Improper Access Control - Generic
- Program: khanacademy
- Disclosed At: 2019-08-25T07:02:41.660Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Summary :
healthyhackathon.khanacademy.org can be took over, since it points to a bucket in S3 but that bucket does not exists.

I know this domain is used to host information of healthyhackathon which is held by khanacademy, but you will not be able to do this anymore if someone is going to claim that bucket. 

#Reference :
[S3_takeover](https://github.com/EdOverflow/can-i-take-over-xyz/issues/36)

## Impact

Taking control of healthyhackathon.khanacademy.org and spoof khanacademy users that healthyhackathon is reopened/"archived for you to challenge" and collect their information.

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
