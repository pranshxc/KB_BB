---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222870'
original_report_id: '222870'
title: IRC-Bot exposes information
weakness: Information Disclosure
team_handle: phabricator
created_at: '2017-04-21T19:35:58.500Z'
disclosed_at: '2017-04-21T20:36:32.951Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# IRC-Bot exposes information

## Metadata

- HackerOne Report ID: 222870
- Weakness: Information Disclosure
- Program: phabricator
- Disclosed At: 2017-04-21T20:36:32.951Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

You can setup the IRC-Bot, and set it into private channels, so that it posts only information about tasks into private channels. Example:
<Human> T698
<Bot> T698: Task title - https://url.example.org/T698

The problem is, that, if the bot is online in IRC, you can send him task numbers via private messages, and then he exposes the title of tasks without access control.

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
