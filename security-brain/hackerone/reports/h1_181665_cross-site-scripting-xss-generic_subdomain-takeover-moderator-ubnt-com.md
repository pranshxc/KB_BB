---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181665'
original_report_id: '181665'
title: Subdomain Takeover (moderator.ubnt.com)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-11-11T22:43:02.878Z'
disclosed_at: '2017-02-06T08:31:51.441Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Subdomain Takeover (moderator.ubnt.com)

## Metadata

- HackerOne Report ID: 181665
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2017-02-06T08:31:51.441Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__

This report is same as #179110

One of your subdomain http://moderator.ubnt.com is pointing towards
```
216.58.203.243    moderator.ubnt.com
216.58.203.243    ghs.google.com
216.58.203.243    ghs.l.google.com
```
{F134183}
And it is unclaimed

When I open it 
it is showing 

{F134184}

__Impact__ :-
An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.

And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.

I Recommend removing  the Cname and DNS connecting to it.

You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm

To clarify your doughs I just added video POC

>1ST Video Is about how I am able to claim it https://youtu.be/51Ku4cGbijE
>2ND Video is proof when trying to claim it for the second time https://youtu.be/GJcWsHJj8aE

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
