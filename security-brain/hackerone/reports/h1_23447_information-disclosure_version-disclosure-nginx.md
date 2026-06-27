---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23447'
original_report_id: '23447'
title: Version Disclosure (NginX)
weakness: Information Disclosure
team_handle: mailru
created_at: '2014-08-10T12:09:20.498Z'
disclosed_at: '2014-09-10T09:13:13.427Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Version Disclosure (NginX)

## Metadata

- HackerOne Report ID: 23447
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2014-09-10T09:13:13.427Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

POC :

url : https://calendar.mail.ru

Open up your google chrome browser.
Click right mouse button and choose Inspect Element.
Put website url in address bar. (https://calendar.mail.ru)
Now choose network option from Inspect Element menu.

Response Headers
Connection:close
Content-Security-Policy:default-src *.mail.ru *.imgsmail.ru *.yadro.ru *.facebook.com *.vk.com *.odnoklassniki.ru *.tns-counter.ru *.youtube.com; script-src 'unsafe-inline' 'unsafe-eval' *.mail.ru *.imgsmail.ru *.yadro.ru *.facebook.com *.vk.com *.odnoklassniki.ru *.tns-counter.ru *.youtube.com *.twitter.com; style-src 'unsafe-inline' 'unsafe-eval' *.mail.ru *.imgsmail.ru *.youtube.com; img-src data: *; report-uri https://cspreport.mail.ru/calendar/;
Content-Type:text/html; charset=utf-8
Date:Sun, 10 Aug 2014 12:03:02 GMT
Location:https://calendar.mail.ru/login/?page=/
Server:nginx/1.5.11
Strict-Transport-Security:max-age=31556926
Transfer-Encoding:chunked
X-Content-Type-Options:nosniff
X-Frame-Options:SAMEORIGIN
X-XSS-Protection:1; mode=block

Details : An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Solution : Add the following line to your nginx.conf file to prevent information leakage from the SERVER header of its HTTP response : server_tokens off

The attached image is a demonstration of the proof of concept as well.

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
