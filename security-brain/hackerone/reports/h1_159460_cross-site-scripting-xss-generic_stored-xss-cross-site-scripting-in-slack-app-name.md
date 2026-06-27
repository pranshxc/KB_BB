---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159460'
original_report_id: '159460'
title: Stored XSS(Cross Site Scripting) In Slack App Name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-08-15T10:48:36.405Z'
disclosed_at: '2016-11-22T22:04:56.590Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS(Cross Site Scripting) In Slack App Name

## Metadata

- HackerOne Report ID: 159460
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2016-11-22T22:04:56.590Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Slack,

This vulnerability is about a Stored Cross Site Scripting

Slack Stored XSS In App(App Name)

Vulnerable URL(Edit App Page)
https://api.slack.com/apps/[appid]/general

https://api.slack.com/apps/A21B3V9GA/general

Vulnerable Parameter = name

Note -Its also work on other user as well.

Send this link to victim

===================

Reproduction Steps
POC Video - https://youtu.be/3jAbPjfPW1o
Screen shot is also attached.

1) Go to app edit page
https://api.slack.com/apps/[appid]/general
https://api.slack.com/apps/A21B3V9GA/general
2) In app name parameter enter the following payload
"/><script>alert(/Bhati/)</script>
3) Now open the app page in any other tab
https://bhativictim.slack.com/apps/A21B3V9GA--scriptalert-bhati-script
4) You will get a Alert Box
5) We can also send this same link to other user(victim).

Thanks,
Narendra

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
