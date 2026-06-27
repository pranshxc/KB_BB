---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125849'
original_report_id: '125849'
title: XSS found on Snapchat website
weakness: Cross-site Scripting (XSS) - Generic
team_handle: snapchat
created_at: '2016-03-25T03:11:04.743Z'
disclosed_at: '2018-05-26T10:10:01.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS found on Snapchat website

## Metadata

- HackerOne Report ID: 125849
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: snapchat
- Disclosed At: 2018-05-26T10:10:01.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Snapchat Team,

I've found a reflected XSS vulnerability on this page:
https://www.snapchat.com/add/snapchat

Example:
https://www.snapchat.com/add/%22%3E%3Ch1%3EXSS%3C%2Fh1%3E

Note: you should visit the page with a mobile user-agent since the server displays different information based on the User-Agent HTTP header sent by the browser.

There are 6 places where the username isn't protected against XSS attacks:
- 4 `meta` tags: twitter:title, twitter:image, og:title, og:image
- 1 `object` tag: snapcode
- 1 `h2` tag: username

This could lead to JavaScript execution, UI redressing or open redirects.

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
