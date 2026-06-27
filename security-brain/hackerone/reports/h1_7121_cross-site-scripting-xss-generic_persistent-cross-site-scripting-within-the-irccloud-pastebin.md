---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7121'
original_report_id: '7121'
title: Persistent Cross Site Scripting within the IRCCloud Pastebin
weakness: Cross-site Scripting (XSS) - Generic
team_handle: irccloud
created_at: '2014-04-11T11:31:46.703Z'
disclosed_at: '2014-10-01T13:47:10.420Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent Cross Site Scripting within the IRCCloud Pastebin

## Metadata

- HackerOne Report ID: 7121
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: irccloud
- Disclosed At: 2014-10-01T13:47:10.420Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The HTML within a paste does not get correctly sanitized after an initial new line. So the following code gets executed: \r\n<script>alert(1);</script> 

https://www.irccloud.com/pastebin/FADYQPrO

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
