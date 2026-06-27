---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '81701'
original_report_id: '81701'
title: Possible SQL injection on "Jump to twitter"
weakness: SQL Injection
team_handle: gratipay
created_at: '2015-08-11T10:48:01.553Z'
disclosed_at: '2016-03-21T02:41:05.176Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- sql-injection
---

# Possible SQL injection on "Jump to twitter"

## Metadata

- HackerOne Report ID: 81701
- Weakness: SQL Injection
- Program: gratipay
- Disclosed At: 2016-03-21T02:41:05.176Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The https://gratipay.com/on/twitter/'  (single-quote at the end) request returns 500 Error, but https://gratipay.com/on/twitter/" returns 404 so i believe it may be an injection. To find the url, go to /search and jump to ' twitter.

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
