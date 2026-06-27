---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '606526'
original_report_id: '606526'
title: '[tianma-static] Security issue with XSS.'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2019-06-11T16:08:58.926Z'
disclosed_at: '2020-10-12T20:44:40.207Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [tianma-static] Security issue with XSS.

## Metadata

- HackerOne Report ID: 606526
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2020-10-12T20:44:40.207Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report XSS in tianma-static
It allows XSS and HTML Injection

First of all, It is my first report and I am sorry that I am not good at English T.T 
thank you.

# Module

**module name:** tianma-static
**version:** 1.0.4
**npm page:** `https://www.npmjs.com/package/tianma-static`

## Module Description

> Provide a static file service.

# Vulnerability

## Vulnerability Description

1) File content type
when I look a CVE-2018-16474([CVE-2018-16474](https://www.cvedetails.com/cve/CVE-2018-16474/), #403692), I think that's vulnerability need arbitrary file(name) upload.

If upload is possible, Attacker can upload `html` file. Also content type of the response header becomes `text/html` and it is possible to Stored XSS.

{F506823}

2) HTML Injection (It can lead to reflected XSS)
when a send `%2f` in path (example: http://127.0.0.1:8080/%2f), `resolve` function make a normal path on the filesystem. but `req.pathname` will print out a manipulated path.

so I can insert any html.

{F506824}

Reflected XSS using HTML only is not easy bypass the modern browser.
but if I can upload any file, Reflected XSS is possible Using load script.

{F506825}

## Steps To Reproduce:

1) File content type
> - upload html file with XSS script. 
> - xss fired

2) HTML Injection (reflected XSS)
> - upload any file with XSS script.
> - access `/%2f<script src='/[filename]'></script>`
> - xss fired

## Patch

1. add content type header in response. 
2. change `decodeURI` to `decodeURIComponent`. or denied malicious path.

# Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

If file upload is possible, XSS can occur.

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
