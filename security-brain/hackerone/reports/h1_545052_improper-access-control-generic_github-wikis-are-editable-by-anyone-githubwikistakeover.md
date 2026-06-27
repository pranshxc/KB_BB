---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '545052'
original_report_id: '545052'
title: 'Github wikis are editable by anyone #Githubwikistakeover'
weakness: Improper Access Control - Generic
team_handle: curl
created_at: '2019-04-22T07:32:14.553Z'
disclosed_at: '2019-05-25T21:13:37.317Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Github wikis are editable by anyone #Githubwikistakeover

## Metadata

- HackerOne Report ID: 545052
- Weakness: Improper Access Control - Generic
- Program: curl
- Disclosed At: 2019-05-25T21:13:37.317Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hey Curl,

Github wiki on the following project,

https://github.com/curl/curl/wiki

can be edited by any logged in user in the system. This poses security and reputation risk for the company.
As your policy i doesnot edited any of the wiki :-)


Regards,
@MSRC29

## Impact

As wikis listed above can be edited by any person on the internet, a malicious actor can accurately craft a message or a note which would lead a user to download a malicious component in a natural way.

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.

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
