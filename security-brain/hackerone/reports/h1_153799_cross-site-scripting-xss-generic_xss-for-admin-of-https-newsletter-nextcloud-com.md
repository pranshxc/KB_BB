---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153799'
original_report_id: '153799'
title: xss for admin of https://newsletter.nextcloud.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-07-25T20:50:10.156Z'
disclosed_at: '2017-02-17T11:03:59.020Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss for admin of https://newsletter.nextcloud.com

## Metadata

- HackerOne Report ID: 153799
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2017-02-17T11:03:59.020Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

a site https://newsletter.nextcloud.com to have phplist 3.2.5

steps to reproduce:

1. to use firefox browser, latest version
2. go to  https://newsletter.nextcloud.com/admin/?page=viewtemplate&id=123%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

3. log in as admin
4. alert box with name of domain

please, look at my poc video in attachment (has been installed phplist 3.2.5 on the localhost)

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
