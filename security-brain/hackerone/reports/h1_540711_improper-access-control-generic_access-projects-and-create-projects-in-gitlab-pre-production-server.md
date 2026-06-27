---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '540711'
original_report_id: '540711'
title: Access Projects And create projects in gitlab pre production server
weakness: Improper Access Control - Generic
team_handle: gitlab
created_at: '2019-04-17T05:06:45.523Z'
disclosed_at: '2019-08-28T17:49:17.235Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Access Projects And create projects in gitlab pre production server

## Metadata

- HackerOne Report ID: 540711
- Weakness: Improper Access Control - Generic
- Program: gitlab
- Disclosed At: 2019-08-28T17:49:17.235Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Steps to reproduce

Go to https://pre.gitlab.com

Here any one can register and can view the pre production projects of gitlab developers.


I have registered in https://pre.gitlab.com/users/sign_in

and have created one test group and test project 

go to https://pre.gitlab.com/explore/groups

i have created one test group 

{F470509}

And i have created one test project

{F470510}

I went to look for gitlab project members https://pre.gitlab.com/qa-perf-testing/gitlabhq/project_members


I have seen it was created by your gitlab employee Ramya Authappan 

https://pre.gitlab.com/rauthappan


The attacker not only access the internal projects of gitlab but he can also create groups and projects in pre production server of gitlab.

## Impact

Attacker will access the pre production server of gitlab and he access the groups and projects created by gitlab employees.

Attacker will also create the projects and groups in pre production server of gitlab.

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
