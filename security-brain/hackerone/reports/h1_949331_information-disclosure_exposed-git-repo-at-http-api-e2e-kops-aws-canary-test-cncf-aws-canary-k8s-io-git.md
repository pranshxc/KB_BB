---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '949331'
original_report_id: '949331'
title: exposed Git Repo at http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/
weakness: Information Disclosure
team_handle: kubernetes
created_at: '2020-08-30T03:34:57.580Z'
disclosed_at: '2021-01-07T18:33:23.911Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# exposed Git Repo at http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/

## Metadata

- HackerOne Report ID: 949331
- Weakness: Information Disclosure
- Program: kubernetes
- Disclosed At: 2021-01-07T18:33:23.911Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Dear Security team,

If this report is out of scope,  please let me know and I will close the report myself

I found a git repository on http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/.git. This endpoint allows an attacker to retrieve much of the source code and git history for this service which could potentially reveal sensitive information, it all depends what is stored there.

Example:
http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/logs/HEAD
http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/config
Mitigation
The restrict access (403 forbidden) are enabled only on /.git and not their subfolders. You just need to add all the git subfolders to the same rule.


Best Regards,
Daniel

## Impact

An attacker can get information just dumping data using  .git repository.

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
