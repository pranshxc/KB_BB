---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245236'
original_report_id: '245236'
title: Missing filteration of meta characters in all full name field on wakatime.com
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-07-02T02:13:23.768Z'
disclosed_at: '2017-07-04T01:57:20.555Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing filteration of meta characters in all full name field on wakatime.com

## Metadata

- HackerOne Report ID: 245236
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-04T01:57:20.555Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there

Vulnerability Title:

Meta characters are not filtered into full name

Description

You haven't filtered control meta characters such as %00 etc in full name field which allows an attacker to impersonate or hide their real identity within the application.
This one is not rejected. It turns out that it is possible to register a user's full name with special sign %0a(appended in proxy).

Impact

Attacker can impersonate user by appending meta characters.

Mitigation

You should disallow nullbytes in the name(here full name field).

Happy to Help

Thanks
Piyush kumar

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
