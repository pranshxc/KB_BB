---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4561'
original_report_id: '4561'
title: Stored XSS in Slackbot Direct Messages
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-22T10:54:27.583Z'
disclosed_at: '2014-05-04T18:38:21.252Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Slackbot Direct Messages

## Metadata

- HackerOne Report ID: 4561
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-05-04T18:38:21.252Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Whenever a new team is created, Slackbot uses automated profile completion by asking a few questions from the user like the first name, last name, skype account etc. But instead of providing the correct details we provide `<javascript:alert(document.cookie);>` as input then Slackbot will cause the data go inside the anchor tag `<a href=javascript:alert(document.cookie);>...</a>` so clicking on the link will trigger XSS.

Video POC: https://www.dropbox.com/s/7fmbe4jnd923pd0/Dumbbot-XSS.mov

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
