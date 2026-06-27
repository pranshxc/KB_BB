---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197786'
original_report_id: '197786'
title: User Information Disclosure via REST API
weakness: Information Disclosure
team_handle: owncloud
created_at: '2017-01-12T10:20:10.906Z'
disclosed_at: '2017-04-19T14:08:17.176Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# User Information Disclosure via REST API

## Metadata

- HackerOne Report ID: 197786
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2017-04-19T14:08:17.176Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

REST-API, allows anonymous access to functionality that allows a hacker to list all users who have published a post on a WordPress site. Unfortunately, this generally includes the admin account

POC: https://owncloud.com/wp-json/wp/v2/users/
https://owncloud.com/wp-json/wp/v2/users/1/


Kind Regards,
Alex.

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
