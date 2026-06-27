---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163464'
original_report_id: '163464'
title: User Information sent to client through websockets
weakness: Information Disclosure
team_handle: legalrobot
created_at: '2016-08-26T02:16:20.127Z'
disclosed_at: '2016-09-12T18:47:42.285Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# User Information sent to client through websockets

## Metadata

- HackerOne Report ID: 163464
- Weakness: Information Disclosure
- Program: legalrobot
- Disclosed At: 2016-09-12T18:47:42.285Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I noticed when monitoring the websocket requests that the account information of many users, including email address, is sent to the client. For example:

```
██████

██████████

█████████

████████

███████

```

There's hundreds of these requests, each containing user information. Please let me know if this is meant to be happening, but I didn't see a list of users on the site.

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
