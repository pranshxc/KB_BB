---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '35036'
original_report_id: '35036'
title: XSS in Tagregator plugin
weakness: Cross-site Scripting (XSS) - Generic
team_handle: iandunn-projects
created_at: '2014-11-09T01:08:39.052Z'
disclosed_at: '2016-08-18T01:19:00.020Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Tagregator plugin

## Metadata

- HackerOne Report ID: 35036
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: iandunn-projects
- Disclosed At: 2016-08-18T01:19:00.020Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

This is a XSS in Tagregator plugin that affect on wordpress users
i'm making my test on alwaysdata host
target: http://diaa.alwaysdata.net/wordpress/wp-admin/post-new.php?post_type=tggr-flickr
infected input: post_title
payload: <script>alert("a7a");</script>
then get the Permalink that is generated for public user: http://diaa.alwaysdata.net/wordpress/?tggr-tweets=alerta7a
alerted !!!
 
tell me if you wanna any information
thank you

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
