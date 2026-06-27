---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57918'
original_report_id: '57918'
title: 'Insecure Local Data Storage  : Application stores data using a binary sqlite
  database'
weakness: Information Disclosure
team_handle: whisper
created_at: '2015-04-23T18:13:42.951Z'
disclosed_at: '2017-03-03T14:20:31.819Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Insecure Local Data Storage  : Application stores data using a binary sqlite database

## Metadata

- HackerOne Report ID: 57918
- Weakness: Information Disclosure
- Program: whisper
- Disclosed At: 2017-03-03T14:20:31.819Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Android provides several options for developers to save persistent application data. The local DB should store data depending on whether the data should be private to your application or accessible to other applications and users. In any case, sensible data always have to be encrypted to avoid privacy violation. Linkedin App keeps user data  in  a  SQLite  database

 w.db

OWASP:  Insecure Storage

OWASP:  Insecure Data Storage

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
