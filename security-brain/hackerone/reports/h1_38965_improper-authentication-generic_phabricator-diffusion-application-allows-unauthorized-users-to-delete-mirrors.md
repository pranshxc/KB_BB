---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38965'
original_report_id: '38965'
title: Phabricator Diffusion application allows unauthorized users to delete mirrors
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-12-10T15:33:37.117Z'
disclosed_at: '2015-01-09T23:26:33.210Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Phabricator Diffusion application allows unauthorized users to delete mirrors

## Metadata

- HackerOne Report ID: 38965
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2015-01-09T23:26:33.210Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have succesfully reproduced this issue following these steps:
 
- Creating a repository with an administrator user
 
- Checking that my "guest" user hasn't access to the newly created repository:
 
  http://phabricator/diffusion/TEST/edit/
 
- However, the guest user does have access to delete the mirror:
 
  http://phabricator/diffusion/TEST/mirror/delete/1/
 
 You can review the lack of permission-checks in the file: applications/diffusion/controller/DiffusionMirrorDeleteController.php

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
