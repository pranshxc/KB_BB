---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '303390'
original_report_id: '303390'
title: remote access to localhost daemon, can issue jsonrpc commands
weakness: Cross-Site Request Forgery (CSRF)
team_handle: monero
created_at: '2018-01-08T23:33:57.253Z'
disclosed_at: '2018-02-22T00:08:19.199Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# remote access to localhost daemon, can issue jsonrpc commands

## Metadata

- HackerOne Report ID: 303390
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: monero
- Disclosed At: 2018-02-22T00:08:19.199Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [Remotely use jsonrpc on localhost wallets]

**Description:** [its possible to execute jsonrpc calls as monerod does not pay strict attention to origin or content-type client headers]

## Releases Affected:

  * [monerod] port 18081

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

1. run monerod
2. visit http://bugbound.co.uk/test42/bert.html for POC (html form)
3. Click submit and view request/response


## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

potentially empy wallet by calling jsonrpc sendrawtransaction

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
