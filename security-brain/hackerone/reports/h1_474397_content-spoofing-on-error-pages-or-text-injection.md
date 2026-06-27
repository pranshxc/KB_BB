---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '474397'
original_report_id: '474397'
title: Content spoofing on error pages or text injection
team_handle: cfptime
created_at: '2019-01-04T15:36:29.541Z'
disclosed_at: '2019-01-08T20:04:04.794Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
asset_identifier: www.cfptime.org
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Content spoofing on error pages or text injection

## Metadata

- HackerOne Report ID: 474397
- Weakness: 
- Program: cfptime
- Disclosed At: 2019-01-08T20:04:04.794Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

###Poc:

[https://www.cfptime.org/%20is%20not%20available%20anymore%20,%20pls%20go%20to%20WWW.EVIL.COM%20because%20this%20site](https://www.cfptime.org/%20is%20not%20available%20anymore%20,%20pls%20go%20to%20WWW.EVIL.COM%20because%20this%20site).

###Steps to reproduce:

1: Just browse this target on any browser 
2: Target: http://www.cfptime.org/
3: add any content after For example: this is not available anymore pls check WWW.EVIL.COM because this site
4: Now browser reflect the content or text .

###Fix :
Use Predefined 404 page , with fixed error content 
It can be fixed by adding the following to the web server config:
ErrorDocument 404 "File not found."

## Impact

Application allows users to inject any content on the 404 not found webpage
The issue is not critical , as it is only possible to inject plain text, no links or active content, to the error page.

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
