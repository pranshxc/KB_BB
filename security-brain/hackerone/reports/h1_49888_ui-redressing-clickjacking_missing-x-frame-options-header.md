---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49888'
original_report_id: '49888'
title: Missing X-Frame-Options header
weakness: UI Redressing (Clickjacking)
team_handle: yelp
created_at: '2015-03-03T11:06:04.726Z'
disclosed_at: '2017-11-09T20:28:08.895Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
tags:
- hackerone
- ui-redressing-clickjacking
---

# Missing X-Frame-Options header

## Metadata

- HackerOne Report ID: 49888
- Weakness: UI Redressing (Clickjacking)
- Program: yelp
- Disclosed At: 2017-11-09T20:28:08.895Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

URL https://staging.seatme.us/

Vulnerability:
The server didn't return an X-Frame-Options header which means that this website could be at 
risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate 
whether or not a browser should be allowed to render a page in a <frame> or <iframe>. 
Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded 
into other sites.

Impact:
The impact depends on the affected web application.

Remedy:
Configure your web server to include an X-Frame-Options header.

Reference:
https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options

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
