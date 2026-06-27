---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '353'
original_report_id: '353'
title: Session not expired on logout
team_handle: security
created_at: '2013-11-09T05:54:35.279Z'
disclosed_at: '2014-04-19T20:59:16.332Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
---

# Session not expired on logout

## Metadata

- HackerOne Report ID: 353
- Weakness: 
- Program: security
- Disclosed At: 2014-04-19T20:59:16.332Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hackerone.com website is not expiring the user's session immediately after logout. 

Steps to verify:
1. Log into the website - hackerone.com.
2. Capture any request. For ex, profile edit page using burp proxy.
3. Logout from the website.
4. Replay the request captured in step 3 and notice it displays the proper response.

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
