---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11945'
original_report_id: '11945'
title: HTTP Strict Transport Security (HSTS) Policy Not Enabled
weakness: Violation of Secure Design Principles
team_handle: joola-io
created_at: '2014-05-13T17:21:30.500Z'
disclosed_at: '2014-07-08T10:00:34.593Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTP Strict Transport Security (HSTS) Policy Not Enabled

## Metadata

- HackerOne Report ID: 11945
- Weakness: Violation of Secure Design Principles
- Program: joola-io
- Disclosed At: 2014-07-08T10:00:34.593Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Team,

Step-by-step instructions on how to reproduce the problem:

It was found the application is vulnerable to HTTP Strict Transport Security (HSTS) Policy Not Enabled.

HTTP Strict Transport Security (HSTS) is an opt-in security enhancement that is specified by a web application through the use of a special response header. Once a supported browser receives this header that browser will prevent any communications from being sent over HTTP to the specified domain and will instead send all communications over HTTPS. It also prevents HTTPS click through prompts on browsers.

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
