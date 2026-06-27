---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '179164'
original_report_id: '179164'
title: Stored XSS in community.ubnt.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-10-31T19:06:59.850Z'
disclosed_at: '2017-04-28T09:55:44.934Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in community.ubnt.com

## Metadata

- HackerOne Report ID: 179164
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2017-04-28T09:55:44.934Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have created two accounts
one attacker account: vibhuti123_i
other victim account: John_victim

 attacker account:vibhuti123_i who will create a malicious link after uploading svg file embeded with script and doing stored xss.Now attacker vibhuti123_i will send this  stored xss malicious link to victim:john_victim by posts,message,reply of ubnt community features or anyother way of communication.After this John_victim will believe this link as it is saved on community.ubnt.com server.It's no way look dangerous so john_victim will click this link and xss gets executed.

This stored xss link created by attacker will execute in every account and also it is accessible without login.
http://community.ubnt.com/t5/image/serverpage/image-id/0iA7662344C5BC7B7E/image-size/thumb/is-preview/true?v=v2&px=100

Please go through Video POC:--
https://youtu.be/Z0UCmv-Tpqs 


PLease read the Document of OWASP.org about svg xss below:

https://www.owasp.org/images/0/03/Mario_Heiderich_OWASP_Sweden_The_image_that_called_me.pdf

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
