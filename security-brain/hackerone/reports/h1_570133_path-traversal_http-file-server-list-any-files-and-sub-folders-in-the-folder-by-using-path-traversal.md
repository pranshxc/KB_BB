---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '570133'
original_report_id: '570133'
title: '[http-file-server] List any files and sub folders in the folder by using path
  traversal.'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-05-07T10:47:20.981Z'
disclosed_at: '2019-07-10T08:58:27.767Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [http-file-server] List any files and sub folders in the folder by using path traversal.

## Metadata

- HackerOne Report ID: 570133
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2019-07-10T08:58:27.767Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Path Traversal in http-file-server. It allows to list any files and sub folders in another folder of web root.

# Module

**module name:** http-file-server
**version:** 0.2.6
**npm page:** https://www.npmjs.com/package/http-file-server

# Vulnerability

## Vulnerability Description

http-file-server is simply get the path name of url and add it to the web root. it means if you input ../, it will happy add it to web root and you can list the folder you choose. But the trick is web browser or curl are also to try rebuild the url containing ../. I used the burp to make a raw url and send it to server.

## Steps To Reproduce:

install `http-file-server`
`$ npm install -g http-file-server`

start program: go to the folder of the module and run the file
`$ ./http-file-server.js --path=/tmp/ --host=* --port=1234`

start burpsuite and enter the url contain ../. you should see the files in the folder.
{F485870}

## Patch

filter .. in the path name.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

- kali linux 4.15.0
- nodejs v8.9.3
- npm 6.4.1
- Burpsuite

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilities.

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
