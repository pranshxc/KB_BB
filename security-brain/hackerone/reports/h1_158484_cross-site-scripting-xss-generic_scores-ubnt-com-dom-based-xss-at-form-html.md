---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158484'
original_report_id: '158484'
title: '[scores.ubnt.com] DOM based XSS at form.html'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-08-11T14:53:50.729Z'
disclosed_at: '2017-02-24T11:33:20.888Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [scores.ubnt.com] DOM based XSS at form.html

## Metadata

- HackerOne Report ID: 158484
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2017-02-24T11:33:20.888Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I would like to report that the #130889 bug hasn't been fixed completely.

The removeTags function has been added, however an attacker is still able to inject Javascript as parameter values without any HTML tags:

> https://scores.ubnt.com/form.html?uid=1&p=%27%20onmouseover=alert(document.domain)//

The script is triggered by the onmouseover event on the header.

Tested with latest Firefox and Chrome.

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
