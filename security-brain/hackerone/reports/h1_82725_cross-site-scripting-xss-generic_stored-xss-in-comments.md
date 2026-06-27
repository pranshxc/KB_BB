---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '82725'
original_report_id: '82725'
title: Stored XSS in comments
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2015-08-16T06:14:48.821Z'
disclosed_at: '2015-11-13T22:07:11.539Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in comments

## Metadata

- HackerOne Report ID: 82725
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2015-11-13T22:07:11.539Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found an XSS vulnerability in commenting on articles.
Steps to reproduce:
1. Go to an article on your website for example: https://testingthatweb.zendesk.com/hc/en-us/articles/204094081 
2. Type this in the comment box: `[Click here](javascript:alert(1))`
3. after the comment is posted , you'll see your comment , press on the link `Click Here` and you got your XSS 

Thanks , Please tell me if you are having any problems reproducing this bug.
M.

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
