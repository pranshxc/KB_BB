---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423286'
original_report_id: '423286'
title: Sidekiq web UI (Ruby background processing) accessible unauthenticated via
  https://gift-test.starbucks.co.jp/sidekiq/busy
weakness: Improper Access Control - Generic
team_handle: starbucks
created_at: '2018-10-13T10:31:17.969Z'
disclosed_at: '2018-10-24T17:31:28.121Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Sidekiq web UI (Ruby background processing) accessible unauthenticated via https://gift-test.starbucks.co.jp/sidekiq/busy

## Metadata

- HackerOne Report ID: 423286
- Weakness: Improper Access Control - Generic
- Program: starbucks
- Disclosed At: 2018-10-24T17:31:28.121Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
I found the following URL, which appears to be running an Sidekiq web UI instance that is accessible unauthenticated: https://gift-test.starbucks.co.jp/sidekiq/busy

**Description:**
Sidekiq is used for Ruby background processing (as I've learned, I'm not really familiar with it). The web UI can be used to stop these processes, as can be seen here:

{F359897}

## Steps To Reproduce:

  1. Go to  https://gift-test.starbucks.co.jp/sidekiq/busy

## Supporting Material/References:

n.a.

## Impact

Unclear. As the domain name suggests it might be a staging/test environment. I cannot determine clearly what these running processes are, but I am able to stop them which might be undesired.

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
