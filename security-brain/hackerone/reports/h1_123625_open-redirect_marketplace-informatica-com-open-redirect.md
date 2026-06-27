---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123625'
original_report_id: '123625'
title: '[marketplace.informatica.com] Open Redirect'
weakness: Open Redirect
team_handle: informatica
created_at: '2016-03-16T14:03:04.377Z'
disclosed_at: '2016-06-27T12:38:34.247Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- open-redirect
---

# [marketplace.informatica.com] Open Redirect

## Metadata

- HackerOne Report ID: 123625
- Weakness: Open Redirect
- Program: informatica
- Disclosed At: 2016-06-27T12:38:34.247Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

marketplace.informatica.com contains an open redirect due to a flawed URL rewrite rule. All requests containing a single quote: ' are met with a 302 redirect to the same URL, minus the single quote. As the Location header uses a protocol-relative URL, this can be abused to redirect people to arbitrary external sites.

To replicate this issue, load the following URL and observe that you land on google.com: https://marketplace.informatica.com//google.com?q=ohdear&a'b

GET //google.com?q=ohdear&a' HTTP/1.1
Host: marketplace.informatica.com
Connection: close

HTTP/1.0 302 Found
Location: //google.com?q=ohdear&a
Server: BigIP
Connection: close
Content-Length: 0

Open redirects are frequently used to make phishing attacks more effective.

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
