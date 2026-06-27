---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '470287'
original_report_id: '470287'
title: Inadequate cache control in gitter allows to view private chat room
weakness: Improper Authentication - Generic
team_handle: gitlab
created_at: '2019-02-11T07:07:32.178Z'
disclosed_at: '2019-03-08T18:41:50.920Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 12
asset_identifier: '*.gitter.im'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- improper-authentication-generic
---

# Inadequate cache control in gitter allows to view private chat room

## Metadata

- HackerOne Report ID: 470287
- Weakness: Improper Authentication - Generic
- Program: gitlab
- Disclosed At: 2019-03-08T18:41:50.920Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi Gitlab,

**Summary:**
I have found a inadequate cache control vulnerability in Gitter.

**Description:**
You can use the backspace button to get the full access to the account. There is no cache control and the browser saves sensitive information of a private chat room.
This report is influenced by the disclosed report #407763. The impact and attack scenario is also the same.

## Steps To Reproduce:

1. Sign in to Gitter
2. Go to a private room
3. Sign-out from the device
4. Click on backspace
5. Chat in the private room

You can access the private room without actually being logged in. You can also chat from the logged out account.

## Impact

Sensitive information can get disclosed through a single backspace.

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
