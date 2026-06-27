---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '253076'
original_report_id: '253076'
title: XSS on about:tbupdate
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: torproject
created_at: '2017-07-24T17:06:31.710Z'
disclosed_at: '2023-11-28T09:02:55.223Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 42
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on about:tbupdate

## Metadata

- HackerOne Report ID: 253076
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: torproject
- Disclosed At: 2023-11-28T09:02:55.223Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
It appears that there is an XSS vulnerability on the about:tbupdate page.

Steps to reproduce:
1. Visit: about:tbupdate?javascript:alert(1)
2. Click on 'visit our website'

Because the page is a privileged one (given it cannot be opened from a normal web page) this XSS may lead to a more severe issue. I will post a reply if I find a way to to do either of two things, first being finding a way to open privileged about: pages from normal content and secondly, I will check to see if there are any privileged javascript functions I could execute to achieve a bigger issue.

Thank you

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
