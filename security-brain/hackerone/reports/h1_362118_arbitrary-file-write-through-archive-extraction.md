---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '362118'
original_report_id: '362118'
title: Arbitrary File Write Through Archive Extraction
team_handle: nodejs-ecosystem
created_at: '2018-06-05T15:58:26.005Z'
disclosed_at: '2018-08-12T14:46:51.027Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Arbitrary File Write Through Archive Extraction

## Metadata

- HackerOne Report ID: 362118
- Weakness: 
- Program: nodejs-ecosystem
- Disclosed At: 2018-08-12T14:46:51.027Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report arbitrary file write vulnerability in adm-zip module
It allows attackers to write arbitrary files when a malicious archive is extracted.
More info here: 
https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability#affected-libraries


# Module

**module name:** adm-zip
**version:** <0.4.9
**npm page:** `https://www.npmjs.com/package/adm-zip`

## Module Description
ADM-ZIP for NodeJS with added support for electron original-fs
ADM-ZIP is a pure JavaScript implementation for zip data compression for NodeJS.

## Module Stats

> Replace stats below with numbers from npm’s module page:

1.5M downloads in the last week

# Vulnerability

## Vulnerability Description
The vulnerability is a form of directory traversal that can be exploited by extracting files from an archive. The premise of the directory traversal vulnerability is that an attacker can gain access to parts of the file system outside of the target folder in which they should reside. The attacker can then overwrite executable files and either invoke them remotely or wait for the system or user to call them, thus achieving remote command execution on the victim’s machine. The vulnerability can also cause damage by overwriting configuration files or other sensitive resources, and can be exploited on both client (user) machines and servers.

The vulnerability is exploited using a specially crafted archive that holds directory traversal filenames (e.g.  ../../evil.sh). The Zip Slip vulnerability can affect numerous archive formats, including tar, jar, war,  cpio, apk, rar and 7z. If you’d like the information on this page in a downloadable technical white paper, click the button below.

More info here: 
https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability


## Steps To Reproduce:

Sample files can be found here: https://github.com/snyk/zip-slip-vulnerability/tree/master/archives


## Patch

Vulnerability is already fixed in ver 0.4.9.
We opened a fix PR on 23rd of April, https://github.com/cthackers/adm-zip/pull/212

CVE id for the vuln was assigned: CVE-2018-1002204

## Supporting Material/References:

There are multiple libraries affected, across different ecosystems. 
Full list here: https://github.com/snyk/zip-slip-vulnerability#affected-libraries

https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability

# Wrap up

- I contacted the maintainer to let them know: Y, and helped fix the issue
- I opened an issue in the related repository: N

## Impact

Writing arbitrary files on the system

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
