---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168104'
original_report_id: '1168104'
title: Weak password policy leading to exposure of administrator account access
weakness: Misconfiguration
team_handle: gsa_vdp
created_at: '2021-04-19T06:46:31.413Z'
disclosed_at: '2021-05-20T14:45:10.915Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 36
asset_identifier: mysmartplans.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# Weak password policy leading to exposure of administrator account access

## Metadata

- HackerOne Report ID: 1168104
- Weakness: Misconfiguration
- Program: gsa_vdp
- Disclosed At: 2021-05-20T14:45:10.915Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The login endpoint https://mysmartplans.gsa.gov/Marathon/Default.aspx is having weak password policy.

During the recon, I came across a mysmartplans overview document http://www.accentimaging.com/accent/pdfs/Accent%20MySmartPlans.pdf
. In this document few users are mentioned like - rick, ban, tim etc.I tried to login user password combination of these user-names & rick wass found a valid administrator username & password.

username- rick
password -rick

This user appears to be administrator user.
Hope GSA takes necessary measures to improve user account policies.

PoC

1) Open url https://mysmartplans.gsa.gov/Marathon/Default.aspx
2) Enter username  rick password rick
3) You will be logged into user account with administrative access. You can edit, create, update users.

## Impact

Admin account compromise.

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
