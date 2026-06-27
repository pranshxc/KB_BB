---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173721'
original_report_id: '173721'
title: Bad content-type in response header when getting document can lead to html
  injection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-10-03T21:13:23.868Z'
disclosed_at: '2017-01-12T20:45:39.433Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Bad content-type in response header when getting document can lead to html injection

## Metadata

- HackerOne Report ID: 173721
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2017-01-12T20:45:39.433Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Bug
When request document by genesis_id or filename, the content-type field in response header is 'text/html'.
And the document content can be anything. So if we upload an odt file with html format and share with other users, it can lead to html injection when others request that file.

## PoC
- img1 via es_id
- img2 via filename (share with others)

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
