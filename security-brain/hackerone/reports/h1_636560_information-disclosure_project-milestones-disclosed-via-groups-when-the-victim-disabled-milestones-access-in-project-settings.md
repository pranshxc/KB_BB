---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '636560'
original_report_id: '636560'
title: Project Milestones Disclosed Via Groups When the Victim disabled milestones
  access in project settings
weakness: Information Disclosure
team_handle: gitlab
created_at: '2019-07-05T18:43:37.166Z'
disclosed_at: '2019-12-13T13:28:37.470Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Project Milestones Disclosed Via Groups When the Victim disabled milestones access in project settings

## Metadata

- HackerOne Report ID: 636560
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2019-12-13T13:28:37.470Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Reproduction steps:


Create a public group and public project.


Go to public project settings and disable the project settings to members only.

{F522796}


If the attacker visits milestones via projects then may see 404 not found page.


https://gitlab.com/victim-waka-waka/test-group-for-sharing/-/milestones/1

{F522797}


But the attacker will view the project mile stones via groups.


{F522798}

## Impact

Attacker will view the project milestones which are disabled by the admin in project settings.

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
