---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '880863'
original_report_id: '880863'
title: Todos are not redacted when membership changes - Access to (confidential) issues
  and merge requests
weakness: Information Disclosure
team_handle: gitlab
created_at: '2020-05-22T17:04:50.461Z'
disclosed_at: '2020-11-02T15:50:34.367Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Todos are not redacted when membership changes - Access to (confidential) issues and merge requests

## Metadata

- HackerOne Report ID: 880863
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2020-11-02T15:50:34.367Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

This vulnerability was fixed in https://gitlab.com/gitlab-org/gitlab-foss/-/issues/54349 , but it reappears maybe due to some new changes and one is able to reproduce the vulnerability to access confidential issues and MRs. 

 All issues and MRs used to get redacted after one hour grace period but it is not happening anymore.

The vulnerability only affects when user permissions changes from higher to lower. If user is removed from the project then the to-dos are getting redacted. 

### Steps to reproduce

* Owner of the project added a user with `Repository` access level.
* User adds issues and MRs to his to-dos list
* Owner changes user access level to `Guest`
*  Guest then use the api and  get access to all new changes to the issues and MRs.

`curl --header "PRIVATE-TOKEN: &lt;User A Token&gt;" https://mygitlab.example.com/api/v4/todos`



### Impact

User still has access to (confidential) issues and merge requests after permission was removed.


### What is the current *bug* behavior?

Bug still allows low access level user `Guest` to access confidential issues and MRs

### What is the expected *correct* behavior?

Redact the confidential issues and MRs


###PoC

In the image below, you can see MRs and issues are not redacted even after 2 hours.

{F839117}


### Output of checks

This bug happens on GitLab.com

## Impact

Todos are not redacted when membership changes - Access to (confidential) issues and merge requests

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
