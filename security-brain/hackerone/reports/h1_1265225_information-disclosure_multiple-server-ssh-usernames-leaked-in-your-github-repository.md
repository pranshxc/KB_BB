---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1265225'
original_report_id: '1265225'
title: Multiple server ssh usernames leaked in your github repository
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2021-07-16T10:17:09.094Z'
disclosed_at: '2021-07-19T19:37:30.463Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 7
asset_identifier: GitHub repositories
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Multiple server ssh usernames leaked in your github repository

## Metadata

- HackerOne Report ID: 1265225
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2021-07-19T19:37:30.463Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

hi  security team,while searching on github,I have found multiple ssh usernames that belongs to your organization are exposed in the organization github repository

STEPS TO REPRODUCE:-
     1.Go to this repository. you will see the leaked multiple server ssh usernames.
          *https://github.com/iandunn/dotfiles/blob/31f4009ddfde9176ba5880687a5119f59183c267/.ssh/config


POC:-
    I have attached a screenshot.Have a look at this

## Impact

By knowing the valid usernames, an attacker can easily bruteforce the password and he can get access to your servers

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
