---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225901'
original_report_id: '225901'
title: Missing filteration of meta characters in full name field on registration page
  https://demo.weblate.org/accounts/register
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-05-03T18:12:13.436Z'
disclosed_at: '2017-05-22T12:38:16.209Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing filteration of meta characters in full name field on registration page https://demo.weblate.org/accounts/register

## Metadata

- HackerOne Report ID: 225901
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-22T12:38:16.209Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there

#Vulnerability Title:
>Meta characters are not filtered into full name on registration page

#Description
>You haven't filtered control meta characters such as %00 etc in full name field on registration page which allows an attacker to impersonate or hide their real identity within the application.
This one is not rejected. It  turns out that it is possible to register a user's full name with special sign %0a(appended in proxy).

#Impact
>Attacker can impersonate user by appending meta characters.

#Mitigation
>You should disallow nullbytes in the name(here full name field).

Happy to Help

Thanks
@smit

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
