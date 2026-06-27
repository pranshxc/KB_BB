---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155690'
original_report_id: '155690'
title: Arbitrary File Upload in Logo & Log in image Theming setting.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-07-31T21:57:59.882Z'
disclosed_at: '2016-10-05T12:34:55.184Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Arbitrary File Upload in Logo & Log in image Theming setting.

## Metadata

- HackerOne Report ID: 155690
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-10-05T12:34:55.184Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team

First I think this vulnerability doesn't fall at your bug bounty program but this is a bad design that should fix right now cause if an attacker get admin access he still can upload a malicious file in client server side.

I saw that Logo & Log in image allow to upload other files type example *.html and it'll execute in client server.
Other case,I created an html code and saved it as image file,server still executed it as html file.
The Logo & Log in image will upload it into ../data/themedinstancelogo & ../data/themedbackgroundlogo

Good news,I tried to upload an php file but server executed that file as text.

PoC:
Upload an html file through logo upload and Log in image and you will see that file will execute.

http://example.com/nextcloud/data/themedinstancelogo
http://example.com/nextcloud/data/themedbackgroundlogo

Regards,

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
