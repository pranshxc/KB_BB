---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50379'
original_report_id: '50379'
title: Open redirect and reflected xss in http://youthvoices.adobe.com/community?return_url=[payload
  her]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: adobe
created_at: '2015-03-06T16:14:42.073Z'
disclosed_at: '2015-05-20T17:48:29.760Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Open redirect and reflected xss in http://youthvoices.adobe.com/community?return_url=[payload her]

## Metadata

- HackerOne Report ID: 50379
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: adobe
- Disclosed At: 2015-05-20T17:48:29.760Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, 
there is a xss vulnerability and open redirect vulnerability in the return_url parameter for the following component:
http://youthvoices.adobe.com/community?return_url=
If a users tries to register or login after following this url:
http://youthvoices.adobe.com/community?return_url=javascript:alert(1)
http://youthvoices.adobe.com/community?return_url=//www.google.com
he will be redirected to google or will trigger the xss vulnerability.

Please see the poc videos below:
https://app.box.com/s/hvjnqyaka1jjarcswltru3qa6sizwz6i
https://app.box.com/s/ntppftcz10v9okwd5xa5wm6h68cjjdzb

I would use this vulnerability to steal users session tokens or to redirect them to a fake login page where i could steal their passwords.
Please let me know what if you think and if you need more details

Kind regards,

nico

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
