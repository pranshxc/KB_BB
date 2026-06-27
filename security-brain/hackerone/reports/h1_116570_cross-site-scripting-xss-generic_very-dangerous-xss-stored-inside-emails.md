---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116570'
original_report_id: '116570'
title: VERY DANGEROUS XSS STORED inside emails
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-02-15T15:31:02.388Z'
disclosed_at: '2016-04-07T10:57:53.633Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# VERY DANGEROUS XSS STORED inside emails

## Metadata

- HackerOne Report ID: 116570
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-04-07T10:57:53.633Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,
This bug is very dangerous you should fix it as fast as you can 
######To reproduce:
Attach xss.eml file to a message and send it
when a user open the message the javascript will be executed and xss alert box will popup
this bug affect tel.mail.ru , m.mail.ru and light.mail.ru
but i couldn't reproduce it on e.mail.ru and touch.mail.ru
######Notes:
when a user attach an email (eml file) to a message 
your website changes the email file name automatically to the subject content in the email file
Eg:
if the file name is xss.eml
and the content is
Subject: <script>alert("XSS")</script>
your website will change the file name to
<script>alert("XSS")</script>.eml
and the javascript will be executed 
######POC:
I uploaded a video

Thank you!!

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
