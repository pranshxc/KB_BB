---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '63537'
original_report_id: '63537'
title: XSS in https://app.mavenlink.com/workspaces/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mavenlink
created_at: '2015-05-23T12:34:09.730Z'
disclosed_at: '2015-06-22T22:57:42.457Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in https://app.mavenlink.com/workspaces/

## Metadata

- HackerOne Report ID: 63537
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mavenlink
- Disclosed At: 2015-06-22T22:57:42.457Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

My name of mavelink account causes cross site scripting vulnerability

my name="><img src=x onerror=prompt(31);>

go to  https://app.mavenlink.com/workspaces/8591867/gantt

and click "save snapshot" button  than save it

When You save it you will get javascrip alert from "Can be viewed by ">" area beucae my mavelink name ("><img src=x onerror=prompt(31);>)

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
