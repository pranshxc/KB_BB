---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76307'
original_report_id: '76307'
title: Self XSS Protection not used , I can trick users to insert JavaScript
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gratipay
created_at: '2015-07-17T19:28:18.202Z'
disclosed_at: '2015-09-11T17:15:54.408Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS Protection not used , I can trick users to insert JavaScript

## Metadata

- HackerOne Report ID: 76307
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gratipay
- Disclosed At: 2015-09-11T17:15:54.408Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Self XSS Protection not used , I can trick users to insert JavaScript
I see that you have not enabled "Self XSS Protection not used" on gratipay.com This technique prevents user from getting tricked into injecting js themselves

For example, Facebook have : http://gyazo.com/3b448c200124053b60b622d0149e242d

But you don't have it, You should Have it to protect users , it tells users not to get tricked and be safe. Its a best practise every website should follow for a safer web!


This bug has been fixed by many websites including Facebook. So its strongly advised you to fix it.

One of my Reports: http://i.imgur.com/XugsNyz.jpg


DATE: 16/06/2015
HOUR: 07:13:28 am
IP: 127.6.47.129

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
