---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152958'
original_report_id: '152958'
title: Multiple XSS in Camptix Event Ticketing Plugin
weakness: Cross-site Scripting (XSS) - Generic
team_handle: iandunn-projects
created_at: '2016-07-21T17:28:05.212Z'
disclosed_at: '2016-08-18T16:39:13.846Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple XSS in Camptix Event Ticketing Plugin

## Metadata

- HackerOne Report ID: 152958
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: iandunn-projects
- Disclosed At: 2016-08-18T16:39:13.846Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
As discussed in #151561 submitting the report here.

I have got some more bugs in Camptix Event Ticketing plugin.

Well, the first one is a ticket page xss caused by the **Ticket Title**
And the second one is kind of self-xss, caused by also the **Ticket title** of the plugin but in the coupons page.
I have added a video *PoC* for your clarification with step by step reproduction.
As I have seen in #9391 you've fixed self-xss, I have created this report.

I think both of the bugs should be fixed.

I expect you fix both of them.


https://drive.google.com/open?id=0B0Ah8VhxGMynZXUwbGlaMm5iVDQ


--------
Zawad

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
