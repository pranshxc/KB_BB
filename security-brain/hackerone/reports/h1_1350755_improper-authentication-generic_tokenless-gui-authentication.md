---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1350755'
original_report_id: '1350755'
title: Tokenless GUI Authentication
weakness: Improper Authentication - Generic
team_handle: kubernetes
created_at: '2021-09-24T21:19:56.193Z'
disclosed_at: '2021-11-04T20:09:05.966Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/kubernetes/dashboard
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Tokenless GUI Authentication

## Metadata

- HackerOne Report ID: 1350755
- Weakness: Improper Authentication - Generic
- Program: kubernetes
- Disclosed At: 2021-11-04T20:09:05.966Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
A person has the ability to bypass the login screen using the 401 error code produced from a failed token login.  The user is given the privileges of an system:anonymous user. 

## Kubernetes Version:
kubectl, kubeadm, kubelet 1.22.2
Ubuntu 20.04.3 - 64bit

## Component Version:
Dashboard v2.3.1+0.g8d9f8e76c

## Steps To Reproduce:

  1. Attempt to log in with a token (just put in gibberish)
  2. Cut and paste the entire 401 authentication error starting from the back, forwards.
  3. Paste the 401 error into the token password field 
  4. Hit enter to Submit

## Supporting Material/References:
Please refer to the demonstration.

## Impact

The user is given the privileges of an system:anonymous user and access to the GUI.

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
