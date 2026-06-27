---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '568832'
original_report_id: '568832'
title: No rate limit on app.crowdsignal.com (Finish quiz)
weakness: Business Logic Errors
team_handle: automattic
created_at: '2019-05-06T14:58:23.144Z'
disclosed_at: '2019-07-27T09:01:50.681Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- business-logic-errors
---

# No rate limit on app.crowdsignal.com (Finish quiz)

## Metadata

- HackerOne Report ID: 568832
- Weakness: Business Logic Errors
- Program: automattic
- Disclosed At: 2019-07-27T09:01:50.681Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello team
[https://hackerone.com/reports/488923 ]--> vulnerability resolved maybe you can compare the report to start this, but this vulnerability has been closed.this is a separate no-rate limit error.this is not a duplicate bug.
No rate limit on app.crowdsignal.com (Finis quiz)
POC step:
1.https://app.crowdsignal.com/quizzes/new
2.example (https://testedtestsdasad1404.survey.fm/untitled-quiz-1)
3.Finish quiz send it to Intruder.(Burp suite)
4.get the payloads ready. Attack with null payloads.
5.POC video and screenshot:

## Impact

an attacker could send a large number of requests to terminate the victim. there is a limit.(quiz finish)
solution:
a limit must be added.

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
