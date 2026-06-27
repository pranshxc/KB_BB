---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1032468'
original_report_id: '1032468'
title: Read-only application can publish/delete fleets
weakness: Privilege Escalation
team_handle: x
created_at: '2020-11-12T12:32:59.699Z'
disclosed_at: '2021-01-04T17:05:39.356Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 395
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Read-only application can publish/delete fleets

## Metadata

- HackerOne Report ID: 1032468
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2021-01-04T17:05:39.356Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Twitter released [Fleet](https://blog.twitter.com/ja_jp/topics/product/2020/ntroducing-fleets-new-way-to-join-the-conversation-jp.html) yesterday. This feature is working with few APIs, and these APIs are missing permission checks.

## Description:
In `/fleets/v1/create` of `https://api.twitter.com`, there is no check to whether if the application has permission to write to the account. `/fleets/v1/delete` has also this issue.


## Steps To Reproduce:

  1. Install [twurl](https://github.com/twitter/twurl).
  1. Authenticate as a read-only application.
  1. Execute following command: `twurl /fleets/v1/create -X POST --header 'Content-Type: application/json' -d '{"text":"Hey yo"}'`
  1. A fleet with `Hey yo` text will be created.

## Supporting Material/References:
{F1075380}

## Impact

The read-only application can publish fleets without getting Write permission. This issue has a similar impact to #434763

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
