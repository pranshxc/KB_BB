---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244958'
original_report_id: '244958'
title: No redirect uri for Twitter Oath resulting in token leak
weakness: Improper Authentication - Generic
team_handle: wakatime
created_at: '2017-07-01T01:01:13.790Z'
disclosed_at: '2017-07-03T08:22:40.325Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# No redirect uri for Twitter Oath resulting in token leak

## Metadata

- HackerOne Report ID: 244958
- Weakness: Improper Authentication - Generic
- Program: wakatime
- Disclosed At: 2017-07-03T08:22:40.325Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good afternoon,

There's an opportunity to steal Oath tokens upon the return uri in the following redirect.

https://wakatime.com/oauth/twitter/authorize?reason=tweet&next=/share/embeddable/5e22456d-9aae-4267-b1a9-4315c2605d89/0ed2e4de-f479-4e03-a8db-464a0696c08f.svg/tweet

If I change the &next= to my profile for example /@5e22456d-9aae-4267-b1a9-4315c2605d89

This results in an open redirect to my main profile leaking the Oauth token: 

#POC

https://wakatime.com/oauth/twitter/authorize?reason=tweet&next=/@5e22456d-9aae-4267-b1a9-4315c2605d89

results in F199105

Here's a video demonstrating the vulnerability. F199111

#Patch
Add a redirect uri that can't be tampered with.

#References

This is almost the exact same scenario that is in this report.
https://hackerone.com/reports/140432

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
