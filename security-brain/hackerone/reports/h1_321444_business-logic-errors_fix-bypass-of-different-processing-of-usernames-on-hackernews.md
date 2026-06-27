---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321444'
original_report_id: '321444'
title: Fix bypass of different processing of usernames on Hackernews
weakness: Business Logic Errors
team_handle: keybase
created_at: '2018-03-02T17:59:55.844Z'
disclosed_at: '2018-04-08T11:15:52.332Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- business-logic-errors
---

# Fix bypass of different processing of usernames on Hackernews

## Metadata

- HackerOne Report ID: 321444
- Weakness: Business Logic Errors
- Program: keybase
- Disclosed At: 2018-04-08T11:15:52.332Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
In report https://hackerone.com/reports/307670 the reported identified a flow which abuses parsing differences between Keybase and Hackernews. Also the original reports is resolved there appears to be a bypass having the same impact by abusing upper-case letters.

## Steps to reproduce
1. Browse to: https://news.ycombinator.com/user?iD=rbanffy&id=blaa
2. Click on the Keybase Extension icon.
3. Notice that the pop-up shows the username blaa while thehackernews page shows the username: rbanffy (See attached image).

## Root cause
Keybase only searches for lower-case letters, however thehackernews allows upper-case ones to.

## Impact

Users attempting to send a secure, sensitive message to a Keybase user can be tricked into sending that message to a malicious user instead.

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
