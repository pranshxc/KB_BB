---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '231510'
original_report_id: '231510'
title: Gratipay Website CSP "script-scr" includes "unsafe-inline"
weakness: HTTP Request Smuggling
team_handle: gratipay
created_at: '2017-05-24T18:20:18.539Z'
disclosed_at: '2017-05-25T14:58:39.121Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- http-request-smuggling
---

# Gratipay Website CSP "script-scr" includes "unsafe-inline"

## Metadata

- HackerOne Report ID: 231510
- Weakness: HTTP Request Smuggling
- Program: gratipay
- Disclosed At: 2017-05-25T14:58:39.121Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Summary:
========
The HTTP header of the gratipay.com website includes an unsafe CSP parameter for "script-src".

Description:
==========
has a Content-Security-Policy configured the "script-src" parameter is set to "unsafe-inline", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks.

Steps to Reproduce:
================
Go to the following link to check your gratipay.com website's http header response: https://hackertarget.com/http-header-check/
``` Content-Security-Policy-Report-Only: default-src self;script-src self assets.gratipay.com unsafe-inline;```

As can be seen, "unsafe-inline" is included in in the list of "script-src" parameters. For further information, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Similar Report: #225833
------------------------

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
