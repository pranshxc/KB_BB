---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176076'
original_report_id: '176076'
title: Javascript confirm() crashes Brave on PC
team_handle: brave
created_at: '2016-10-16T01:31:53.695Z'
disclosed_at: '2016-10-19T01:32:26.931Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
---

# Javascript confirm() crashes Brave on PC

## Metadata

- HackerOne Report ID: 176076
- Weakness: 
- Program: brave
- Disclosed At: 2016-10-19T01:32:26.931Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Brave, https://hackerone.com/smelt and I found a glitch for Brave on Windows.
## Summary:

If you run the javascript code confirm(), Brave will crash. This is major for a glitch, because people may be visiting
websites that have confirm messages and Brave will suddenly and unexpectedly crash for them.

## Products affected: 

Doesn't effect Mobile
Tested and crashed Windows Brave browser

## Steps To Reproduce:

1. Open Brave
2. Run the JS code confirm() somehow (Ex. go to my website I made that runs it: pentesting.x10host.com)
3. Brave will crash

If you have questions or comments please reply here.



Thanks,
kicker and smelt

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
