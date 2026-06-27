---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215384'
original_report_id: '215384'
title: '[Subgroups] Unprivileged User Can Disclose Private Group Names'
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gitlab
created_at: '2017-03-22T16:14:59.742Z'
disclosed_at: '2017-03-30T06:18:52.225Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# [Subgroups] Unprivileged User Can Disclose Private Group Names

## Metadata

- HackerOne Report ID: 215384
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gitlab
- Disclosed At: 2017-03-30T06:18:52.225Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi @briann and team,

Congratulations on the launch of GitLab 9.0! While exploring Subgroup functionality, I noticed that an unprivileged user can disclose private group names by incrementing the `parent_id` parameter. 

## Proof of Concept
To reproduce this issue, I set up a fresh GitLab 9.0 CE server and created a Private Group using the `root` account. Afterwards, I created an unprivileged user (no group or project assignments) and visited the below URL, disclosing the name of `PrivateGroup`.

Attempting to access the `PrivateGroup` via the standard routes (e.g. Group Page) presents the unprivileged user with the expected 404 page.

```
http://<instance>/groups/new?parent_id=2
```

### Screenshot
{F170581}

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
