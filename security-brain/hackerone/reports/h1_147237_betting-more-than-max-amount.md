---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147237'
original_report_id: '147237'
title: Betting more than max amount
team_handle: fantasytote
created_at: '2016-06-25T16:13:08.071Z'
disclosed_at: '2016-07-26T10:24:22.835Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Betting more than max amount

## Metadata

- HackerOne Report ID: 147237
- Weakness: 
- Program: fantasytote
- Disclosed At: 2016-07-26T10:24:22.835Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey Fantasytote,

This is not really a security issue since this won't leak any data of other users (or something like that) but i still wanted to tell you this because there must be a reason you guys limit the max bet to 150 euro (per bet).

You can reproduce this issue by betting 150 euro, intercepting the data and modifying it to 1000 euro.
I uploaded this video to youtube (unlisted so only you can watch it.)
Please watch my PoC video:
https://youtu.be/ny6dLtu-xV0

__**How can I fix this?**__
You can fix it by not only validating the bet amount client side but also validating it server side.

Could you please reopen my previous report since you can send the token to external websites. (Non Fantasytote websites.)

Ask me if you need anything,
Karel.

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
