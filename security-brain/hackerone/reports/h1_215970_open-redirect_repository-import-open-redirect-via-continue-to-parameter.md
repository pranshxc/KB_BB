---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215970'
original_report_id: '215970'
title: '[Repository Import] Open Redirect via "continue[to]" parameter'
weakness: Open Redirect
team_handle: gitlab
created_at: '2017-03-25T08:44:49.387Z'
disclosed_at: '2017-04-06T04:27:32.522Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- open-redirect
---

# [Repository Import] Open Redirect via "continue[to]" parameter

## Metadata

- HackerOne Report ID: 215970
- Weakness: Open Redirect
- Program: gitlab
- Disclosed At: 2017-04-06T04:27:32.522Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While experimenting with Repository Import functionality on a fresh GitLab 9.0 CE install, I noticed that the `continue[to]` parameter can be used to perform an Open Redirect through the inclusion of a double-slash prefix. 

## Proof of Concept
The following Proof of Concept URL enables a malicious actor to execute this redirect against any user – as long as they have permissions to view a certain repository. 

```
http://<instance>/<user>/<repository>/import?continue[to]=//google.com
```

## Observation
I first noticed the `continue[to]` parameter while receiving the `You're not allowed to make changes to this project directly` message – demonstrating that edit-level access to the repository in question is not required.

Thanks!

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
