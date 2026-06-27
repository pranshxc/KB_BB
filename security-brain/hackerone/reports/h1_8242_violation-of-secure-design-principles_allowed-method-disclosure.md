---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8242'
original_report_id: '8242'
title: Allowed method disclosure
weakness: Violation of Secure Design Principles
team_handle: respondly
created_at: '2014-04-20T22:03:35.602Z'
disclosed_at: '2014-04-21T17:16:41.260Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Allowed method disclosure

## Metadata

- HackerOne Report ID: 8242
- Weakness: Violation of Secure Design Principles
- Program: respondly
- Disclosed At: 2014-04-21T17:16:41.260Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The URL "https://respond.ly/" has the following allowed methods, which include DAV methods: ACL, BASELINE_CONTROL, CHECKIN, CHECKOUT, CONNECT, COPY, DEBUG, GET, HEAD, INDEX, INVALID, INVOKE, LABEL, LINK, LOCK, MERGE, MKACTIVITY, MKCOL, MKDIR, MKWORKSPACE, MOVE, NOTIFY, OPTIONS, PATCH, PIN, POLL, POST, PROPFIND, PROPPATCH, REPLY, REPORT, RMDIR, SEARCH, SHOWMETHOD, SPACEJUMP, SUBSCRIBE, SUBSCRIPTIONS, TEXTSEARCH, TRACK, UNCHECKOUT, UNLINK, UNLOCK, UNSUBSCRIBE, VERSION_CONTROL.

Might wanna remove this

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
