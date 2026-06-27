---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115219'
original_report_id: '115219'
title: Information Disclosure in Error Page
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-02-07T16:12:20.544Z'
disclosed_at: '2016-04-29T13:38:51.730Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Information Disclosure in Error Page

## Metadata

- HackerOne Report ID: 115219
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2016-04-29T13:38:51.730Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

Here's an crafted URL which discloses web server used and version of same. 
> https://paragonie.com/%PI  

Even-though most error pages are handled by generic pages in paragonie.com, above given ```400 Bad Request``` sample is not handled. 
It seems this error page is because of Invalid URL Encoded (%PI) Value given in the request.

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
