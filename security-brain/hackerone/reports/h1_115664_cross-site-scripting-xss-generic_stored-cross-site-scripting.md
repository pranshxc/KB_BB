---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115664'
original_report_id: '115664'
title: Stored Cross site scripting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-06-16T21:14:49.750Z'
disclosed_at: '2016-06-28T05:06:54.681Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored Cross site scripting

## Metadata

- HackerOne Report ID: 115664
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-06-28T05:06:54.681Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

hello zomato team,

i have found a stored xss on https://www.zomato.com/beirut/garcias-dbayeh-metn

step to reproduce
--------------------------
1- write a review by this payload : >'>"><img src=x onmouseover =prompt(document.domain)>
2-click edit
3- xss will excute :)

video : https://youtu.be/ibawEBPQs3g

best regaeds,
Amir Ezat.

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
