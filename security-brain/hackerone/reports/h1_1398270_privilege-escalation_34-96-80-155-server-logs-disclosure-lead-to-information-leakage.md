---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1398270'
original_report_id: '1398270'
title: '[34.96.80.155] Server Logs Disclosure lead to Information Leakage'
weakness: Privilege Escalation
team_handle: evernote
created_at: '2021-11-11T13:26:03.552Z'
disclosed_at: '2021-12-09T16:52:23.982Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: www.evernote.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [34.96.80.155] Server Logs Disclosure lead to Information Leakage

## Metadata

- HackerOne Report ID: 1398270
- Weakness: Privilege Escalation
- Program: evernote
- Disclosed At: 2021-12-09T16:52:23.982Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
In this case server log is available for any in `/server-status` 

## Steps To Reproduce:
1. Go to https://34.96.80.155/server-status/ and follow attack scenario's

### Attack Scenario's: 

**[Serg.io]**
  1. User go to server and enter sensitive info that can be logged (example : `http://host/login?private_key=<KEY>`)
  2. Attacker read the logs and founded sensitive information that user entered (example : `private_key=<KEY>`)
{F1510839}

**[translate.evernote.com]**
 In this site login and many features available and it's increase the impact 

  1. Users login with sso ( example : `/sso?sso_private_key=<key>&next=/ssoreturn` )
  2. Attacker can read full sso key and login (Account Take Over)

## Supporting Material/References:

### Why [34.96.80.155] blongs to www.evernote.com :
* the ssl certificate : https://www.shodan.io/host/34.96.80.155 (SSL Cert related to *Evernote Corporation*)
* copywrite section : 
> © 2014–2021 Evernote Corporation

## Impact

attacker can read all log on server

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
