---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50358'
original_report_id: '50358'
title: files.acrobat.com stored XSS via send file
weakness: Cross-site Scripting (XSS) - Generic
team_handle: adobe
created_at: '2015-03-06T12:57:35.508Z'
disclosed_at: '2015-04-14T22:55:20.804Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# files.acrobat.com stored XSS via send file

## Metadata

- HackerOne Report ID: 50358
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: adobe
- Disclosed At: 2015-04-14T22:55:20.804Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Description of the sending file vulnerable to xss
Proof:
https://files.acrobat.com/a/preview/c9efeb22-75a5-4268-ad57-f8f694aa7a1d

steps to reproduce:
- go to https://cloud.acrobat.com/send and select file to send
-  check an option "Create Anonymous Link"
- input any subject 
- input payload `<img src=x onerror=alert(1)>` to description
- click "Create Link" button
- follow to created link

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
