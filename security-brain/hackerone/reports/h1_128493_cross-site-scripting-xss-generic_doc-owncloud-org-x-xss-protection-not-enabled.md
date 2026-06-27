---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128493'
original_report_id: '128493'
title: 'doc.owncloud.org: X-XSS-Protection not enabled'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-04-05T18:29:02.755Z'
disclosed_at: '2016-04-09T05:17:36.745Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# doc.owncloud.org: X-XSS-Protection not enabled

## Metadata

- HackerOne Report ID: 128493
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-04-09T05:17:36.745Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

X-Xss-Protection @https://doc.owncloud.org/ has not been set. 

This header is used to configure the built in reflective XSS protection found in Internet Explorer, Chrome and Safari (Webkit). Valid settings for the header are 0, which disables the protection, 1 which enables the protection and 1; mode=block which tells the browser to block the response if it detects an attack rather than sanitising the script.

 

NginX: add_header X-Xss-Protection "1; mode=block" always;

Apache: Header always set X-Xss-Protection "1; mode=block"

IIS:

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
