---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78012'
original_report_id: '78012'
title: Sensitive server-side/application information disclosure
weakness: Information Disclosure
team_handle: keybase
created_at: '2015-07-23T02:38:19.517Z'
disclosed_at: '2015-10-30T18:55:32.741Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Sensitive server-side/application information disclosure

## Metadata

- HackerOne Report ID: 78012
- Weakness: Information Disclosure
- Program: keybase
- Disclosed At: 2015-10-30T18:55:32.741Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is an Information disclosure vulnerability present  in Keybase API request whenever an exception occurs.

Steps to reproduce:
Open the following URL in any browser - https://keybase.io/_/api/1.0/user/lookup.json?twitter=john&github=john&usernames=john&usernames=rock

Observe that when we add multiple parameter in the query string, an exception occurs. In a result, Keybase throws the server side error message with all details about the exception which contains application specific sensitive information.

PoC: refer the attached image
The Keybase application structure, Back-end program names, Events, Methods everything is getting displayed in the error message.

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
