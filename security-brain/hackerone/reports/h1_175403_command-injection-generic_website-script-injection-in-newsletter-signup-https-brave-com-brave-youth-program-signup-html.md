---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175403'
original_report_id: '175403'
title: '[website] Script injection in newsletter signup https://brave.com/brave_youth_program_signup.html'
weakness: Command Injection - Generic
team_handle: brave
created_at: '2016-10-12T15:09:20.163Z'
disclosed_at: '2016-11-03T08:58:20.582Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- command-injection-generic
---

# [website] Script injection in newsletter signup https://brave.com/brave_youth_program_signup.html

## Metadata

- HackerOne Report ID: 175403
- Weakness: Command Injection - Generic
- Program: brave
- Disclosed At: 2016-11-03T08:58:20.582Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

go to https://brave.com/brave_youth_program_signup.html
click become an ambasador
insert malicious payloads in the fields <a href='evil,com'>YOU JUST WON 1m$ </a>
you will receive a mail like in the image attached.

You can send phising emails and do other bad stuff.

If you need more details i'm here.

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
