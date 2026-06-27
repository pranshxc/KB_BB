---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1023920'
original_report_id: '1023920'
title: SSRF external interaction
weakness: Server-Side Request Forgery (SSRF)
team_handle: stripo
created_at: '2020-11-01T15:18:17.113Z'
disclosed_at: '2020-12-11T12:56:40.002Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF external interaction

## Metadata

- HackerOne Report ID: 1023920
- Weakness: Server-Side Request Forgery (SSRF)
- Program: stripo
- Disclosed At: 2020-12-11T12:56:40.002Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team,

i found ssrf external interaction on your website which is https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en on chatbox 

description:- the attacker might cause the server to make connection back to it self
or to other web services within the organization infrastructure or to external third party systems

steps to reproduce:-

1)navigate to this website  https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en 
2))there you can find chat box
3)paste burp collaborator URL or http://pingb.in
4)you will get HTTP request to your server

note:-i previously submitted this issues in bug crowd it marked as p4 so i set severity to low and i tested many chat application not all are vulnerable example bug crowd chat system.

## Impact

by this vulnerability attacker can map out attack surface

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
