---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7441'
original_report_id: '7441'
title: Dangerous Persistent xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: irccloud
created_at: '2014-04-13T10:02:31.500Z'
disclosed_at: '2014-05-13T10:20:33.389Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Dangerous Persistent xss

## Metadata

- HackerOne Report ID: 7441
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: irccloud
- Disclosed At: 2014-05-13T10:20:33.389Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If a person is an op in a channel, it is possible to make all the users inside the irc channel execute javascript code.
Steps to repoduce:
1.Go to a random channel where you are op.
2.Enter the following command:
/ban <script>alert(2)</script>
3.The script will execute an alert box containing 2 in all the browsers of the users inside the irc channel.

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
