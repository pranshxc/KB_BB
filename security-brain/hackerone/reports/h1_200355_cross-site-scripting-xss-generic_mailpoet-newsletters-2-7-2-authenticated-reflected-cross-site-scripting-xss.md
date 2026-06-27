---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200355'
original_report_id: '200355'
title: MailPoet Newsletters <= 2.7.2 - Authenticated Reflected Cross-Site Scripting
  (XSS)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2017-01-22T14:42:55.144Z'
disclosed_at: '2017-06-17T17:58:38.886Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# MailPoet Newsletters <= 2.7.2 - Authenticated Reflected Cross-Site Scripting (XSS)

## Metadata

- HackerOne Report ID: 200355
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2017-06-17T17:58:38.886Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__

__Abstract__:-
A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue allows an attacker to perform a wide variety of actions, such as stealing Administrators' session tokens, or performing arbitrary actions on their behalf. In order to exploit this issue, the attacker has to lure/force a logged on WordPress Administrator into opening a URL provided by an attacker.

__Introduction__:-
The MailPoet Newsletters plugin allows a WordPress administrator to create newsletters, automated emails, post notifications and autoresponders. A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue allows an attacker to perform a wide variety of actions, such as stealing Administrators' session tokens, or performing arbitrary actions on their behalf. In order to exploit this issue, the attacker has to lure/force a logged on WordPress Administrator into opening a URL provided by an attacker.

__Proof of concept__:-
Have an authenticated admin visit the URL:-

https://business-blog.zomato.com//?wysija-page=1&controller=subscribers&action=wysija_outter&encodedForm=eyJmb3JtIjoiUHduIiwiYWZ0ZXJfd2lkZ2V0IjoiPHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4ifQ==
The encodedForm parameter is the base64 encoded string:
{"form":"Pwn","after_widget":"<script>alert('XSS)</script>"}

A pop-up box should appear, meaning the JavaScript contained in the request_id request parameter was executed by the browser.

{F154227}

__Fix__:-
This issue is resolved in MailPoet Newsletters version 2.7.3.

__Regards__,
Santhosh

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
