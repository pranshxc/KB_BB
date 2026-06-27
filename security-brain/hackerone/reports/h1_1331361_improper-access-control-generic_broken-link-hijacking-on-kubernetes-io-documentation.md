---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1331361'
original_report_id: '1331361'
title: Broken Link Hijacking on kubernetes.io Documentation
weakness: Improper Access Control - Generic
team_handle: kubernetes
created_at: '2021-09-06T17:19:27.723Z'
disclosed_at: '2021-11-06T18:04:26.463Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Broken Link Hijacking on kubernetes.io Documentation

## Metadata

- HackerOne Report ID: 1331361
- Weakness: Improper Access Control - Generic
- Program: kubernetes
- Disclosed At: 2021-11-06T18:04:26.463Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Kubernetes docs has Spanish translation available. One of the page of spanish doc has an external reference to a confluence page.
The confluence account was not registered on Atlassian.
So I was able to takeover the page and host the PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes.io/es/docs/concepts/workloads/controllers/daemonset/
  2. Search for `Sysdig Agent`
  3. Click on the atlassian link next to that text
  4. You will be redirected to `https://sysdigdocs.atlassian.net/wiki/spaces/Platform),/overview`
  5. Now try opening the confluence account with this url https://sysdigdocs.atlassian.net/wiki/spaces/TAKEOVER/overview
  6. You will see the takeover message

## Supporting Material/References:

- https://sysdigdocs.atlassian.net/wiki/spaces/TAKEOVER/overview

{F1438785}

## Impact

As an attacker, I can host malicious content on the confluence page to misguide the user.
I can also, host details about installing malicious sdk or softwares, which user will think is part of the deployment docs as its referreded in kubernetes.io, this can lead to RCE for users who are referring to this doc

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
