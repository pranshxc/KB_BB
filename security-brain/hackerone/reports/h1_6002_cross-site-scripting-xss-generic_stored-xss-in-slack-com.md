---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6002'
original_report_id: '6002'
title: Stored XSS in Slack.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-04-06T02:40:01.137Z'
disclosed_at: '2015-03-09T18:52:47.846Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Slack.com

## Metadata

- HackerOne Report ID: 6002
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2015-03-09T18:52:47.846Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps: 

Go to your respective URL Mine is https://dezignburg.slack.com/account/photo

now Change your photo using Facebook

But before that create a Album in your Facebook naming it as "><img src=x onerror=alert(document.cookie)>

And you will get this error: http://prntscr.com/37eecd

If you need a video just tell me

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
