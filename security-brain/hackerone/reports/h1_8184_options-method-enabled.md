---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8184'
original_report_id: '8184'
title: OPTIONS Method Enabled
team_handle: localize
created_at: '2014-04-20T09:02:35.556Z'
disclosed_at: '2014-04-21T07:03:33.741Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# OPTIONS Method Enabled

## Metadata

- HackerOne Report ID: 8184
- Weakness: 
- Program: localize
- Disclosed At: 2014-04-21T07:03:33.741Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

HTTP OPTIONS method is enabled on the web server of Localize. The OPTIONS method provides a list of the methods that are supported by the web server, it represents a request for information about the communication options available on the request/response chain identified by the Request-URI.

This vulnerability affects the Web Server of InvisionApp!

Attack details:

Methods allowed: GET,HEAD,POST,OPTIONS 

The OPTIONS method may expose sensitive information that may help an malicious user to prepare more advanced attacks.

Fix:It's recommended to disable OPTIONS Method on the web server.

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
