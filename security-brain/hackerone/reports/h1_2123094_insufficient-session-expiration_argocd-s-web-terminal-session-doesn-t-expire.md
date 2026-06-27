---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2123094'
original_report_id: '2123094'
title: Argocd's web terminal session doesn't expire
weakness: Insufficient Session Expiration
team_handle: ibb
created_at: '2023-08-25T05:24:05.670Z'
disclosed_at: '2023-09-09T13:15:30.125Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- insufficient-session-expiration
---

# Argocd's web terminal session doesn't expire

## Metadata

- HackerOne Report ID: 2123094
- Weakness: Insufficient Session Expiration
- Program: ibb
- Disclosed At: 2023-09-09T13:15:30.125Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The vulnerability is that  web terminal sessions do not expire, even if the argocd's web session has expired.

Step 1: Log in to ArgoCD.

Step 2: Open a web terminal session in ArgoCD, which is used to operate a machine.

Step 3: Wait until the web session expires, but the web terminal session does not expire.

## Impact

All versions of Argo CD starting from v2.6.0 have a bug where open web terminal sessions do not expire. This bug allows users to send any websocket messages even if the token has already expired. The most straightforward scenario is when a user opens the terminal view and leaves it open for an extended period. This allows the user to view sensitive information even when they should have been logged out already.

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
