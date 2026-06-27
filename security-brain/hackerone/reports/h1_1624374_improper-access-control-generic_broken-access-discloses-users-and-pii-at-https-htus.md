---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1624374'
original_report_id: '1624374'
title: Broken access discloses users and PII at https://███████ [HtUS]
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2022-07-04T14:10:27.134Z'
disclosed_at: '2022-10-14T13:53:44.609Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-access-control-generic
---

# Broken access discloses users and PII at https://███████ [HtUS]

## Metadata

- HackerOne Report ID: 1624374
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2022-10-14T13:53:44.609Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good morning,

I was able to register at https://████/ and get the list of users.
1- Go to https://██████████/OA_HTML/ibeCAcpSSOReg.jsp and register.
2- Go to https://███/OA_HTML/AppsLocalLogin.jsp with the created user and login.
3- On the homepage, click on vacations rules, create, and search users.
4- User are disclosed.

██████

Regards,

G4MB4

## Impact

An attacker is able to access users information.

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
