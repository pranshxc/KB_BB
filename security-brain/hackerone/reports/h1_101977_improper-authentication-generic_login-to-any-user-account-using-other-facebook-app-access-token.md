---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101977'
original_report_id: '101977'
title: Login to any user account using other facebook app access token
weakness: Improper Authentication - Generic
team_handle: imgur
created_at: '2015-11-25T09:31:18.682Z'
disclosed_at: '2017-07-24T04:27:12.727Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 66
tags:
- hackerone
- improper-authentication-generic
---

# Login to any user account using other facebook app access token

## Metadata

- HackerOne Report ID: 101977
- Weakness: Improper Authentication - Generic
- Program: imgur
- Disclosed At: 2017-07-24T04:27:12.727Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable Url: https://api.imgur.com/generatetoken/thirdpartynativeandroid?type=facebook
Vulnerable Param: access_token

Attck:
Hacker can build own facebook app and get victim's facebook access token and use that access token to login into imgur account 

POC: https://drive.google.com/file/d/0B9bnr9ZtF2QsYktlRVFPUDB2SmM/view?usp=sharing

Prevention: Validate access token and check app id is equal to 127621437303857

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
