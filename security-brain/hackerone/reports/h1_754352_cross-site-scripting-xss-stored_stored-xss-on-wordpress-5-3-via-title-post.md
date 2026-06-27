---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '754352'
original_report_id: '754352'
title: Stored XSS on Wordpress 5.3 via Title Post
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2019-12-09T13:22:18.762Z'
disclosed_at: '2019-12-10T09:58:14.881Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 9
asset_identifier: WordPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on Wordpress 5.3 via Title Post

## Metadata

- HackerOne Report ID: 754352
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2019-12-10T09:58:14.881Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I have identified a WordPress security vulnerability , a Stored XSS vulnerability that affects latest version of WordPress (5.3)

POC:
1) Login to wordpress website
2) Make a post with title payload xss like example <script>alert(document.domain);</script>
3) Publish then open the post, XSS Will trigger

## Impact

Can stealing cookie user

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
