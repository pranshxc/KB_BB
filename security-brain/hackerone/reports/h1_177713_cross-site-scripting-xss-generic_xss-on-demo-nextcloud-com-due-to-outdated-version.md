---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '177713'
original_report_id: '177713'
title: xss on demo.nextcloud.com due to outdated version
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-10-23T23:03:06.861Z'
disclosed_at: '2016-11-26T14:05:06.899Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss on demo.nextcloud.com due to outdated version

## Metadata

- HackerOne Report ID: 177713
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-11-26T14:05:06.899Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello. I found the possibility of introducing "html-tag" and of xss attack in the form of adding comments. Details video.
Payload: </textarea><img src=x onmouseover=alert(document.domain)>
Browser: Firefox 49.0
OS: Ubuntu 16.04

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
