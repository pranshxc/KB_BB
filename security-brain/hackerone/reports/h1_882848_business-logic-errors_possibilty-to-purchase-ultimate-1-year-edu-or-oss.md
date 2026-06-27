---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '882848'
original_report_id: '882848'
title: Possibilty to purchase Ultimate - 1 Year (EDU or OSS)
weakness: Business Logic Errors
team_handle: gitlab
created_at: '2020-05-26T13:58:38.644Z'
disclosed_at: '2020-11-02T15:42:28.298Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: customers.gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Possibilty to purchase Ultimate - 1 Year (EDU or OSS)

## Metadata

- HackerOne Report ID: 882848
- Weakness: Business Logic Errors
- Program: gitlab
- Disclosed At: 2020-11-02T15:42:28.298Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Any user can purchase Ultimate - 1 Year (EDU or OSS) which is for educational institutions or open source projects.I have found here https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/860 list of Gitlab plan id and found  Ultimate - 1 Year which is  free and purchased.

Steps to reproduce:

Login in to your account https://customers.gitlab.com/
And go to  https://customers.gitlab.com/subscriptions/new?plan_id=2c92a0fd63afe3fd0163d87aecee230a&transaction=create_subscription

Best,
@steppe

## Impact

Attacker can bypass GitLab for Education Program Requirements.

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
