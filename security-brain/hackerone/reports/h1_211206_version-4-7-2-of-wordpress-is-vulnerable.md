---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '211206'
original_report_id: '211206'
title: Version 4.7.2 of wordpress is vulnerable
team_handle: nextcloud
created_at: '2017-03-06T21:42:25.704Z'
disclosed_at: '2017-03-07T17:38:20.703Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Version 4.7.2 of wordpress is vulnerable

## Metadata

- HackerOne Report ID: 211206
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-03-07T17:38:20.703Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,

I observed that your website https://nextcloud.com still use wordpress 4.7.2

Version 4.7.2 of wordpress is vulnerable to :

Cross-site scripting (XSS)
Control characters can trick redirect URL validation
Cross-site scripting (XSS) via video URL in YouTube embeds
Cross-site scripting (XSS) via taxonomy term names
Cross-site request forgery (CSRF) in Press This leading to excessive use of server resources
Fix :

Upgrade to wordpress 4.7.3
More information : https://wordpress.org/news/2017/03/wordpress-4-7-3-security-and-maintenance-release/

Best regards
Rey Mark

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
