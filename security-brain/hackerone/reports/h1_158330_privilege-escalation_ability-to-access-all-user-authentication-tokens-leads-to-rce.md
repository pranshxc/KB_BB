---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158330'
original_report_id: '158330'
title: Ability to access all user authentication tokens, leads to RCE
weakness: Privilege Escalation
team_handle: gitlab
created_at: '2016-08-11T01:21:05.379Z'
disclosed_at: '2016-11-03T22:28:43.639Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 57
tags:
- hackerone
- privilege-escalation
---

# Ability to access all user authentication tokens, leads to RCE

## Metadata

- HackerOne Report ID: 158330
- Weakness: Privilege Escalation
- Program: gitlab
- Disclosed At: 2016-11-03T22:28:43.639Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Vulnerability details
The project export feature serializes the user objects of team members and stores it in the `project.json` file. This object contains the `authentication_token` for every user, meaning that an attacker can simply go ahead and create a project on GitLab.com, add one of the admins of GitLab.com, create an export, and obtain the authentication token for that user.

# Proof of concept
Follow these steps to reproduce the issue:

 - create a test account on a GitLab instance and create a temporary repository
 - invite an admin of the GitLab instance as a team member to the repository
 - go to the repository settings and create an export
 - wait a few minutes until you received the export email
 - now go to http://gitlab-instance/account/repo/download_export
 - unzip the downloaded file and examine `projects.json` - the `project_members` will contain the user object that contains the `authentication_token`

Here's the first few bytes of `rspeicher` (sorry Robert) his authentication token on GitLab.com: `ZyhqJr4XJZ...`. Someone could get access to GitLab's admin panel by extracting the token of an admin and go to https://gitlab.com/admin/users?authentication_token=<token>. From what I've seen on my own GitLab instance, this leads to RCE and gives me access to all code in private repositories. Let me know if you need more information!

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
