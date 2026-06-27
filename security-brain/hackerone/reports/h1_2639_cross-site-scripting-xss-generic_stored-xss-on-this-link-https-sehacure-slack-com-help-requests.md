---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2639'
original_report_id: '2639'
title: Stored XSS on this link https://sehacure.slack.com/help/requests/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-01T23:35:15.765Z'
disclosed_at: '2014-08-30T07:19:46.154Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on this link https://sehacure.slack.com/help/requests/

## Metadata

- HackerOne Report ID: 2639
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-08-30T07:19:46.154Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This is a little tricky one.

First of all go to your profile page and change your name to "><img src=x onerror=prompt(12);>
Save it.
Wait!!! You will not see a javascript pop up there because there is proper input validation on the profile page.

Now to see the prompt box

1) Go to this link  https://sehacure.slack.com/help/requests/new
2) Add a new ticket. Now submit it. 
3) Now view your ticket.You will now be shown a prompt box.
4) Please have a look at the attached screenshot the inputs are not validated over there.

I have changed my name to }') ">ppp>
and i am attaching the source code view of the same.No, input encoding is done there.

Please have a check.

Best,
Anand

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
