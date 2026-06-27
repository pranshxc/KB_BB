---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1353200'
original_report_id: '1353200'
title: text injection and content spoofing
weakness: Phishing
team_handle: oneweb
created_at: '2021-09-28T05:30:47.567Z'
disclosed_at: '2022-02-03T11:12:41.164Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.oneweb.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- phishing
---

# text injection and content spoofing

## Metadata

- HackerOne Report ID: 1353200
- Weakness: Phishing
- Program: oneweb
- Disclosed At: 2022-02-03T11:12:41.164Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

SUMMARY:
Their is a vulnerability  TEXT INJECTION and content inejction. in your website.
An attacker can use text injection vulnerability to present a customized message on the application that can phish users into believing that the .

steps:
1: https://█████████.oneweb.net
2: ADD payload !!!!!ATTENTION!!!!"website under contruction, website moved to attacker.com.please visit WWW.EVIL.COM"" you can login EVIL.COM this is trusted website.

Website Look Like

Access Error: 404 -- Not Found
Can't locate document: /!!!!!ATTENTION!!!!"website under contruction, website moved to attacker.com.please visit WWW.EVIL.COM"" you can login EVIL.COM this is trusted website.


FIX:
The error page was changed to not echo user input.blocked user input

## Impact

An attacker can use text injection vulnerability to present a customized message on the application that can phish users into believing that the message is legitimate

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
