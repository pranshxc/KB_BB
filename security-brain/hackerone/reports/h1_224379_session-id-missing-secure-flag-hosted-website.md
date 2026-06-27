---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224379'
original_report_id: '224379'
title: session id missing secure flag - Hosted Website
team_handle: weblate
created_at: '2017-04-27T15:17:42.858Z'
disclosed_at: '2017-05-17T16:31:11.951Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# session id missing secure flag - Hosted Website

## Metadata

- HackerOne Report ID: 224379
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T16:31:11.951Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey folks,

Looks like the `sessionid` cookie handles session id but misses `Secure` flag. Cookies without this flag will transmitted over unencrypted channel and let's the man in the middle attackers to grab the value.

### Attack Vector
- Attacker passes a http:// hosted website link
- Victim clicks the link
- Browser passes the session cookie over http
- MITIM attacker gets the value and take over the account
With the #224287, this made more simpler.

### Suggested Fix
Set the Secure flag true for the session id and any other sensitive cookies.

Example h1 reports:
https://hackerone.com/reports/58679
https://hackerone.com/reports/6877

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
