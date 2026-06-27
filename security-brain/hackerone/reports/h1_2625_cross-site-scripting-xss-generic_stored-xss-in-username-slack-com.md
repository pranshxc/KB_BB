---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2625'
original_report_id: '2625'
title: Stored XSS in username.slack.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-01T22:11:51.624Z'
disclosed_at: '2014-08-07T18:20:45.404Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in username.slack.com

## Metadata

- HackerOne Report ID: 2625
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-08-07T18:20:45.404Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi 

There is a stored XSS in username.slack.com.

Steps to reproduce:

1. Login to your Slack
2. Goto "Create Private Group" and with any name and purpose
3. Goto https://manish.slack.com/messages/group/files/
4. Upload a file hitting upload icon (^)  filename shall be "><img src=x onerror=alert(1);>.jpeg
5. After file is uploaded click on the image or file title, JS will execute as the filename is considered as payload

I've attached the image showing XSS.

Thanks!

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
