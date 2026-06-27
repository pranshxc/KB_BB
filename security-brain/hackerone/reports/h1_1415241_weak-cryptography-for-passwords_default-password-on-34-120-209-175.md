---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1415241'
original_report_id: '1415241'
title: Default password on 34.120.209.175
weakness: Weak Cryptography for Passwords
team_handle: elastic
created_at: '2021-12-02T09:31:38.115Z'
disclosed_at: '2022-11-18T08:14:54.089Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: Other
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Default password on 34.120.209.175

## Metadata

- HackerOne Report ID: 1415241
- Weakness: Weak Cryptography for Passwords
- Program: elastic
- Disclosed At: 2022-11-18T08:14:54.089Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is  a default password on 34.120.209.175, I can log in successfully.It has 500 Server Error, But we can confirm default password is vaild.

**Summary:**

The IP has a SSL certificate pointing to ElasticSearch.
curl -kv https://34.120.209.175



## Steps To Reproduce:

  1. access https://34.120.209.175/user/login,and log in with admin/admin
  2. it response the  version of  rundeck and error alert
  3. get Physical path and Class name.

## Impact

Get the Default password.

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
