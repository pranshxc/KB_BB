---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161935'
original_report_id: '161935'
title: Usernames ending in .json are not restricted
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-08-21T14:22:39.025Z'
disclosed_at: '2017-07-10T10:03:36.541Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Usernames ending in .json are not restricted

## Metadata

- HackerOne Report ID: 161935
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-07-10T10:03:36.541Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Desciption:
Username  in *.json   is not restricted.

disallowed *.json is allowed in username  restriction

URL   :  https://gratipay.com/robots.txt

User-agent: *
Disallow: /*.json
Disallow: /on/*

POC URL:
https://gratipay.com/~karthic.json/  and you will end up at my profile page.

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
