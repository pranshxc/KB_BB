---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '727870'
original_report_id: '727870'
title: '[www.yoti.com] Wordpress user admin information discloure'
weakness: Information Disclosure
team_handle: yoti
created_at: '2019-11-02T15:35:03.103Z'
disclosed_at: '2020-08-14T19:56:58.712Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: www.yoti.com
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# [www.yoti.com] Wordpress user admin information discloure

## Metadata

- HackerOne Report ID: 727870
- Weakness: Information Disclosure
- Program: yoti
- Disclosed At: 2020-08-14T19:56:58.712Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary
This website using Wordpress CMS, so developer forget to disable the link that can view information of admin user.
By access to this link, attacker can get all username and other information of user admin:
```
https://www.yoti.com/wp-json/wp/v2/users
```

████

Admin user list:

1. ███████
1. █████
1. █████████
1. ████████
1. █████
1. ██████
1. ██████
1. ███████
1. █████
1. ██████

## Impact

With this vulnerability, attacker can get username of user admin and only brute-force the password for logging in the system.

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
