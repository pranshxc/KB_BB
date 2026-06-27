---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '231041'
original_report_id: '231041'
title: Session not expired When logout [partners.uber.com]
team_handle: uber
created_at: '2017-05-23T08:52:02.974Z'
disclosed_at: '2017-05-26T22:56:44.653Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 11
tags:
- hackerone
---

# Session not expired When logout [partners.uber.com]

## Metadata

- HackerOne Report ID: 231041
- Weakness: 
- Program: uber
- Disclosed At: 2017-05-26T22:56:44.653Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi,

Summary
=========
partners.uber.com website is not expiring the user's session immediately after logout.

when user logout, the session not expired, and still can send request and the server respond response with OKAY

__Steps to Reproduce:__

- Log into the website - partners.uber.com
- Capture any request. For ex, profile edit page using burp proxy.
- Logout from the website.
- Replay the request captured in step 2 and notice it displays the proper response.

Thanks, 
tell me if you need video, i will create one !

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
