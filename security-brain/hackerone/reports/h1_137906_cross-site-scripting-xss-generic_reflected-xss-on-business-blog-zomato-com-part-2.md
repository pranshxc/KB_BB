---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137906'
original_report_id: '137906'
title: Reflected XSS on business-blog.zomato.com - Part 2
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-05-11T15:26:22.450Z'
disclosed_at: '2017-06-18T08:44:03.973Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on business-blog.zomato.com - Part 2

## Metadata

- HackerOne Report ID: 137906
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2017-06-18T08:44:03.973Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

I would like to report a reflected XSS on business-blog.zomato.com.

1. Open Chrome and Firefox (latest versions)
2. Open https://business-blog.zomato.com/wp-includes/js/plupload/plupload.flash.swf?target%g=alert&uid%g=hello&
3. Payload is executed

Check the attached screenshot.

Solution:
- Update WordPress to 4.5.2
- Update Plupload to latest version once released

Feel free to contact me if you need further assistance.

Best,
-David Sopas

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
