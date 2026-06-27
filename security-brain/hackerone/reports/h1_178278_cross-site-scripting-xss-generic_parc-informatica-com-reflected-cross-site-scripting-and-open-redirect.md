---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178278'
original_report_id: '178278'
title: '[parc.informatica.com] Reflected Cross Site Scripting and Open Redirect'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-10-26T19:40:50.097Z'
disclosed_at: '2017-04-29T15:08:23.233Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [parc.informatica.com] Reflected Cross Site Scripting and Open Redirect

## Metadata

- HackerOne Report ID: 178278
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-29T15:08:23.233Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi !
I just want to report you a vulnerability in your subdomain ,,parc''

**Description**

In this link *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=* the vulnerable parameter is ,,endpoint''. Once the parameter takes the value of a XSS vector or a website link the code is executed after we complete the form.

**Steps to reproduce**

Go to *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=javascript:alert(document.domain)*

After you complete the form, alert executed document.domain .

and Open redirect: *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=http://evil.com* after you complete the form, you are redirected to evil.com

I think it's valid because in your scope is *.informatica.com
Thanks for attention !

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
