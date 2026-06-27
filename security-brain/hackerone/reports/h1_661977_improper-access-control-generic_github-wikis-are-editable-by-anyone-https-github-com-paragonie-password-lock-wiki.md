---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '661977'
original_report_id: '661977'
title: Github wikis are editable by anyone https://github.com/paragonie/password_lock/wiki
weakness: Improper Access Control - Generic
team_handle: paragonie
created_at: '2019-07-27T19:14:43.261Z'
disclosed_at: '2019-07-29T07:15:09.928Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: https://github.com/paragonie/password_lock
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Github wikis are editable by anyone https://github.com/paragonie/password_lock/wiki

## Metadata

- HackerOne Report ID: 661977
- Weakness: Improper Access Control - Generic
- Program: paragonie
- Disclosed At: 2019-07-29T07:15:09.928Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

submitted a misconfiguration in some of our GitHub repositories to us. Wikis are inherently editable for all users, but for some repositories an organization may want to restrict this access. In some cases it was possible for GitHub users .
Github wikis on the following project
https://github.com/paragonie/password_lock
can be edited by any logged in user in the system. This poses security and reputation risk for the company.
Steps To Reproduce:
1. Go to https://github.com/paragonie/password_lock/wiki and follow the wiki.
2. I can created a simple page in the wiki without be a collaborator of the repo, or and without any permission
3. Going on https://github.com/paragonie/password_lock/wiki you can add a new fake or phishing page clicking on the New page or edit buttons.

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.

attachment / reference
https://hackerone.com/reports/457032
https://hackerone.com/reports/459634

## Impact

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.
As wikis listed above can be edited by any person on the internet, a malicious actor can accurately craft a message or a note which would lead a user to download a malicious component in a natural way.

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
