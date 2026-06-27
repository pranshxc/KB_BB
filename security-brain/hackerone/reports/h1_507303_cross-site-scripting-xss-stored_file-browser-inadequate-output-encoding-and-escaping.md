---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507303'
original_report_id: '507303'
title: '[file-browser] Inadequate Output Encoding and Escaping'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2019-03-10T04:04:35.878Z'
disclosed_at: '2020-01-29T16:24:06.082Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [file-browser] Inadequate Output Encoding and Escaping

## Metadata

- HackerOne Report ID: 507303
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-29T16:24:06.082Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report stored xss in file-browser module
It allows an attacker to embed malicious js code as filenames,which get executed once browsed to the file over the web browser

# Module

**module name:** file-browser
**version:** 0.0.5
**npm page:** https://www.npmjs.com/package/file-browser

## Module Description
file-browser is a utility to browse files on your file system using your browser. Its equivalent of creating a file share that can be accessed over http. Using this you can share files between different machines, and across different operating systems.


## Vulnerability Description

due to improper output encoding and escaping ,it was possible for an attacker to embed malicious js code as filenames,which get executed once browsed to the file over the web browser
## Steps To Reproduce:
1.  npm -g install file-browser

2.now running below command will start a file server on the specified port:
  file-browser

3.now create a file with xss payload as filename in current dir

touch '"><img src=x onerror=alert("xss")>.jpg'

4.now goto url at which the file server is running

http://127.0.0.1:8088/lib/template.html

now xss will popup

## Supporting Material/References:

- [OPERATING SYSTEM VERSION] Kali linux
- [NODEJS VERSION] 11.8.0
- [NPM VERSION] 6.5.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

this could have enabled an attacker to execute malicous js code which might lead to session stealing,hooking up browser with frameworks like beef and so on

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
