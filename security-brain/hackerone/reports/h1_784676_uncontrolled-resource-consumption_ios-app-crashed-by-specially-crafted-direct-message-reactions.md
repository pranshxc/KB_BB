---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '784676'
original_report_id: '784676'
title: iOS app crashed by specially crafted direct message reactions
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2020-01-28T11:08:28.835Z'
disclosed_at: '2020-02-21T21:09:38.699Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: com.atebits.Tweetie2
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# iOS app crashed by specially crafted direct message reactions

## Metadata

- HackerOne Report ID: 784676
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2020-02-21T21:09:38.699Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** iOS app crashed by specially crafted direct message reactions

**Description:**
Twitter does not properly sanitize direct message reactions, making it possible for arbitrary reaction text to be shown to the user via the message preview in the direct message list. Special characters such as `\r` and `\n` are not stripped, and it is even possible to crash the app by inserting a `\0` character into the reaction text.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Start a direct message conversation with the victim (this can also be yourself).
  1. Make a request to https://api.twitter.com/1.1/dm/reaction/new.json with an appropriate `conversation_id` and `dm_id` parameter, and `reaction_key` set to `\0` (an actual NUL byte).
  1. Notice that the iOS app crashes, even on any subsequent attempts to reopen it.

## Impact

This makes it trivial for an attacker to make the Twitter iOS app unusable for any user they can send a direct message to. The only recourse for the victim is to log in via twitter.com and delete the affected message or conversation.

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
