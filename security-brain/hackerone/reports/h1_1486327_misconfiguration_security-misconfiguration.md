---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1486327'
original_report_id: '1486327'
title: Security misconfiguration
weakness: Misconfiguration
team_handle: lemlist
created_at: '2022-02-20T07:42:18.379Z'
disclosed_at: '2022-05-16T09:41:20.201Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# Security misconfiguration

## Metadata

- HackerOne Report ID: 1486327
- Weakness: Misconfiguration
- Program: lemlist
- Disclosed At: 2022-05-16T09:41:20.201Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description :
When we request a magic link to login into the application, and use that same link in multiple browsers, it working there isn't any limit on use of link.

Steps to reproduce :
1. go to app.lemilist.com
2. create a magic link 
3. use it to login 
4. now open another browser or incognito window
5. use that same magic link

And You'll be logged in in your account.

## Impact

If Attacker gets the magic link of user he can login into victim's account.
Account takeover.

Mitigation :
1. Add a limit to magic link and remove the magic link from database after 1 use.
2. only allow the Requester IP to login using the magic link.

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
