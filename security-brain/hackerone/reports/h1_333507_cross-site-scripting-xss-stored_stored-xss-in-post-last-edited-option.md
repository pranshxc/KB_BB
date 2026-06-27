---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '333507'
original_report_id: '333507'
title: Stored XSS in "post last edited" option
weakness: Cross-site Scripting (XSS) - Stored
team_handle: discourse
created_at: '2018-04-04T18:48:34.636Z'
disclosed_at: '2018-07-09T16:04:37.753Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in "post last edited" option

## Metadata

- HackerOne Report ID: 333507
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: discourse
- Disclosed At: 2018-07-09T16:04:37.753Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. There are two users: **Attacker** and **Victim**.
2. **Attacker** starts a private talk via private message with the **Victim**.
3. **Attacker** send a message to **Victim**, then he edits it or deletes it.
4. **Victim** sees the *yellow pencil*, symbol of the edit.
5. **Victim** clicks on *yellow pencil* to see the edit and the XSS runs.

Other info: the XSS also runs on topic (video PoC #2). You can find my XSS message on this URL:
https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278
It is very dangerous because it can hit many users at the same time.

## Impact

XSS can use to steal cookies, password or to run arbitrary code on victim's browser

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278

**Verified**
Yes

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
