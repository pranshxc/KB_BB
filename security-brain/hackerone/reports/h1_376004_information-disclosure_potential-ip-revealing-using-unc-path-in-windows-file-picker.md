---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '376004'
original_report_id: '376004'
title: Potential IP revealing using UNC Path in Windows File Picker
weakness: Information Disclosure
team_handle: torproject
created_at: '2018-07-03T12:09:11.404Z'
disclosed_at: '2023-11-28T09:09:48.364Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 22
tags:
- hackerone
- information-disclosure
---

# Potential IP revealing using UNC Path in Windows File Picker

## Metadata

- HackerOne Report ID: 376004
- Weakness: Information Disclosure
- Program: torproject
- Disclosed At: 2023-11-28T09:09:48.364Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This report is inspired by #294364. The release note says that after fixing [Bug 26424](https://trac.torproject.org/projects/tor/ticket/26424), UNC path is disabled in Tor. But I found that I can still type UNC path in Windows file picker dialog box, and that sends requests to remote servers without Tor proxy.

Some social engineering is required to exploit this trick though. Attackers can use <input type="file"> on their website, and trick users to click "Browse" and type an attacker-controlled IP address into file picker in UNC format.

Is it possible to disable UNC path in the Windows file picker? If not, how about showing a warning message?

## Impact

With some social engineering, attackers can know user's real IP address with <input type="file">.

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
