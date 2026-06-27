---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '647130'
original_report_id: '647130'
title: Stored XSS in "Create Groups"
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2019-07-17T06:17:40.240Z'
disclosed_at: '2020-08-26T14:15:21.414Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 87
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in "Create Groups"

## Metadata

- HackerOne Report ID: 647130
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2020-08-26T14:15:21.414Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS. 

### Steps to reproduce

1. Login to [Gitlab](https://gitlab.com)
2. Create a new group with xss payload
payload i use = "><img src=x onerror=prompt(123)>
3. Open Group
4. To trigger XSS you can click "NEW PROJECT"
5. XSS Trigger

## Impact

Can steal Cookie, Can run javascript code, etc

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
