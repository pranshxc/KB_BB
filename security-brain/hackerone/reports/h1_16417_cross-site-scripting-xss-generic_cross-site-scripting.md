---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '16417'
original_report_id: '16417'
title: Cross  Site Scripting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-06-14T10:44:30.270Z'
disclosed_at: '2016-03-10T15:21:09.480Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross  Site Scripting

## Metadata

- HackerOne Report ID: 16417
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-03-10T15:21:09.480Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team ,

Have found a bug in your main domain ".mail.ru"

Vulnerable URL:
http://deti.mail.ru/mama/

Vulnerable Parameter: Display text , URL links
Payload:"/><style/onload=alert(0)>

Steps to Reproduce:
1.Go to the vulnerable link.
2.Click on "Share experiences" , this will open a form.
3.Click on "Insert Link" , give the payload in vulnerable parameters as mentioned above. then click ok , payload will be executed.

e.g: in URL links  give payload as  :  http://www.xyz.com?p="/><style/onload=alert(document.domain)>

For your refference poc is attached below.

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
