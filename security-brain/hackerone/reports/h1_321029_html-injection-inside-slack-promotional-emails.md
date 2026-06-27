---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321029'
original_report_id: '321029'
title: HTML Injection inside Slack promotional emails
team_handle: slack
created_at: '2018-03-01T12:00:30.324Z'
disclosed_at: '2018-07-30T13:50:03.067Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# HTML Injection inside Slack promotional emails

## Metadata

- HackerOne Report ID: 321029
- Weakness: 
- Program: slack
- Disclosed At: 2018-07-30T13:50:03.067Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There's a HTML injection vulnerability present inside emails sent from slack when the FIRST name on the account contains HTML. The html is stored in the backend database and when emails are sent (promotional, etc), the HTML is sent along with the rest of the email.

In my PoC, which is provided below, i inserted a <img> tag to prove this vulnerability exists. 

F268173

## Impact

This vulnerability can lead to the reformatting/editing of emails from an official slack email address, which can be used in targeted phishing attacks. 

This could lead to users being tricked into giving logins away to malicious attackers.

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
