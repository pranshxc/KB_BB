---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1543770'
original_report_id: '1543770'
title: Moderators can send messages to users from banned subreddits via `oauth.reddit.com/api/mod/conversations`
weakness: Improper Input Validation
team_handle: reddit
created_at: '2022-04-18T19:29:02.904Z'
disclosed_at: '2022-07-04T12:59:33.089Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: oauth.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Moderators can send messages to users from banned subreddits via `oauth.reddit.com/api/mod/conversations`

## Metadata

- HackerOne Report ID: 1543770
- Weakness: Improper Input Validation
- Program: reddit
- Disclosed At: 2022-07-04T12:59:33.089Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It is possible for moderators to send messages to users from a banned subreddit.

I assume this is not intended considering that when trying to send a message as a banned subreddit via [reddit.com/message/compose](https://www.reddit.com/message/compose) (`from` field) you get a `200` response but the message is never delivered to the recipient.

## Steps To Reproduce:

1. While in [mod.reddit.com/mail/create](https://mod.reddit.com/mail/create), select a banned subreddit from the dropdown menu.
2. Fill in all other fields and send the message.

## Impact

Moderators can "officially" communicate with users even after the subreddit gets banned. This can be used to organize a new subreddit to migrate to in order to circumvent the ban.

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
