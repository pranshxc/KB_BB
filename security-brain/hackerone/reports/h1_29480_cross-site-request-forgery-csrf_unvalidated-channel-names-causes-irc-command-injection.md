---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '29480'
original_report_id: '29480'
title: Unvalidated Channel names causes IRC Command Injection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-09-30T14:12:25.005Z'
disclosed_at: '2014-10-01T13:47:16.521Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Unvalidated Channel names causes IRC Command Injection

## Metadata

- HackerOne Report ID: 29480
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-10-01T13:47:16.521Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

IRCCloud does not validate the channel names created by a user causing it to be parsed as an IRC command such as QUIT.

This means the user can have their clients force-closed by a malicious channel name.

This could also lead to other command injections such as forcing the handover of channels to other users for example (not tested).

Here is my PoC of a malicious channel name:
``#treehouse'){%0a%0dQUIT``

``15:03:49  ⇐ SySTeM quit (sid12267@reid-aqa3e3.irccloud.com) Client exited
15:04:02  → SySTeM joined #treehouse'){%0a%0dQUIT (sid12267@reid-aqa3e3.irccloud.com)
15:04:04  ⇐ SySTeM quit (sid12267@reid-aqa3e3.irccloud.com) Client exited``

If you require any further information, please let me know.

All the best,
Richard Clifford

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
