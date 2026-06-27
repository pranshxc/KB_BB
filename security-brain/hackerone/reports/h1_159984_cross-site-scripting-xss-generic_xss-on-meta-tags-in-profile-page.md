---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159984'
original_report_id: '159984'
title: XSS On meta tags in profile page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gitlab
created_at: '2016-08-17T08:37:30.104Z'
disclosed_at: '2016-08-21T18:39:30.071Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS On meta tags in profile page

## Metadata

- HackerOne Report ID: 159984
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gitlab
- Disclosed At: 2016-08-21T18:39:30.071Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The profile page (https://gitlab.com/u/<user>) does not properly sanitize quotation marks, allowing for injection of attributes into the meta tags. This allows for redirection to phishing sites and other various nefarious things. I've managed to get my [profile page](https://gitlab.com/u/Plazmaz) to redirect to Bing by setting my bio to 
`0;url=http://www.bing.com" http-equiv="refresh`

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
