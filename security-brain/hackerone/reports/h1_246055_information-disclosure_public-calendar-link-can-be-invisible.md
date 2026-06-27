---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246055'
original_report_id: '246055'
title: Public calendar link can be invisible
weakness: Information Disclosure
team_handle: mixmax
created_at: '2017-07-05T10:51:50.168Z'
disclosed_at: '2017-08-07T01:15:58.463Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- information-disclosure
---

# Public calendar link can be invisible

## Metadata

- HackerOne Report ID: 246055
- Weakness: Information Disclosure
- Program: mixmax
- Disclosed At: 2017-08-07T01:15:58.463Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, 
I was working on the calendar settings. Where I saw, there is a public calendar link creator box. Usually people put their username in that box. But I was tired to do something. I know the calendar link can be unlisted as public. But the things I found, I can make my calendar link public and invisible at the same time. 
Here's my PoC:
1. Search for a existing file in https://cal.mixmax.com. (for testing purpose, I choosed robots.txt)
2. Now I have put my username as robots.txt {F200314}
3. Now click on View, https://cal.mixmax.com/robots.txt will open, which is a existing file link. But main purpose was viewing my calendar. But in this situation, my calendar is totally hidden by that existing robots.txt file. 

Already existing filename should be unavailable for the calendar link creation. 
NB: I am removing my link as robots.txt because I want you to investigate in this issue. 
Thanks, 
Faisal Ahmed

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
