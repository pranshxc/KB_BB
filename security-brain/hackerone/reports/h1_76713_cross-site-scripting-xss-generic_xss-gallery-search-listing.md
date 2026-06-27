---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76713'
original_report_id: '76713'
title: XSS - Gallery Search Listing
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zaption
created_at: '2015-07-19T09:28:07.837Z'
disclosed_at: '2015-08-12T17:13:16.483Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS - Gallery Search Listing

## Metadata

- HackerOne Report ID: 76713
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zaption
- Disclosed At: 2015-08-12T17:13:16.483Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI.
If you upload video having title with XSS payload. and search for the video, the dropdown listing will execute the payload.

https://www.zaption.com/gallery/search?q=%3E%3Cimg

I need not to upload the payload, I utilized already uploaded videos.


You can also execute the payload by just start typing into the search box with
"><img

That's it, XSS will be executed.

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
