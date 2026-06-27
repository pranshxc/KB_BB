---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507159'
original_report_id: '507159'
title: '[fileview] Inadequate Output Encoding and Escaping'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2019-03-09T15:12:41.309Z'
disclosed_at: '2019-12-28T21:09:28.894Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: fileview
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [fileview] Inadequate Output Encoding and Escaping

## Metadata

- HackerOne Report ID: 507159
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2019-12-28T21:09:28.894Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report stored xss in fileview module
It allows an attacker to embed malicious js code in filename there was no sanitization performed. 

# Module

**module name:**fileview
**version:** 0.1.6
**npm page:** https://www.npmjs.com/package/fileview

## Module Description
File browsers on web. It's easy to browser your local file.


# Vulnerability

## Vulnerability Description

since there was no sanitizations performed on filenames ,an attacker can include filenames with malicious js code which gets executed when browsed to the file  over the web browser

## Steps To Reproduce:
1.install fileview:
npm install fileview -g

2:now create a file with xss payload as follows:
"><img src=x onerror=alert("xss")>.jpg

3.running below command on terminal  will start a file server at port 8080

fileview -p /root/ -P 8080

4.now goto http://127.0.0.1:8080/

you will see the xss got executed



## Patch

> If you're able to provide a patch with the fix please post it in this section

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION] KALI LINUX
- [NODEJS VERSION] 11.8.0
- [NPM VERSION]  6.5.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

this could have allowed an attacker to embed malicious js code in filename and executes it when  victim browse to file over the web browser

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
