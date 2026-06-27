---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90980'
original_report_id: '90980'
title: 'owncloud.com: WP Super Cache plugin is outdated'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2015-09-29T22:31:51.900Z'
disclosed_at: '2015-10-30T09:41:14.452Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# owncloud.com: WP Super Cache plugin is outdated

## Metadata

- HackerOne Report ID: 90980
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2015-10-30T09:41:14.452Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I know it might be out of scope, but I report it to be sure
https://owncloud.org/wp-content/plugins/wp-super-cache/readme.txt shows version 1.4.4

and this version is prone to XSS and  PHP Object injection
http://z9.io/2015/09/25/wp-super-cache-1-4-5/

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
