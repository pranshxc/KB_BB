---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1847140'
original_report_id: '1847140'
title: Argo CD reconciles apps outside configured namespaces when sharding is enabled
weakness: Improper Access Control - Generic
team_handle: ibb
created_at: '2023-01-25T19:04:04.242Z'
disclosed_at: '2023-03-05T16:49:51.098Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: https://github.com/argoproj/argoproj
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Argo CD reconciles apps outside configured namespaces when sharding is enabled

## Metadata

- HackerOne Report ID: 1847140
- Weakness: Improper Access Control - Generic
- Program: ibb
- Disclosed At: 2023-03-05T16:49:51.098Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The Application CRD outside configured namespace in Argo CD will be reconciled.

The following is how to reproduce the vulnerability:

* Enable `apps-in-any-namespace` and `sharding` features.
* Create an Application CRD in namespace not configured in Argo CD.
* Update the Application CRD, and Argo CD will reconcile the Application CRD, despite not in configured namespace.

## Impact

Attacker can use Argo CD permission to deploy resources in Kubernetes.

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
