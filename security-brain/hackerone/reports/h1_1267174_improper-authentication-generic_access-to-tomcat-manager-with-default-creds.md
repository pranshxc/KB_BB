---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1267174'
original_report_id: '1267174'
title: Access to tomcat-manager with default creds
weakness: Improper Authentication - Generic
team_handle: jetblue
created_at: '2021-07-17T23:24:05.092Z'
disclosed_at: '2023-02-05T12:59:44.752Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: checkin.jetblue.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Access to tomcat-manager with default creds

## Metadata

- HackerOne Report ID: 1267174
- Weakness: Improper Authentication - Generic
- Program: jetblue
- Disclosed At: 2023-02-05T12:59:44.752Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi jetblue Security Team.

I Found that this domain `█████████` using Apache Tomcat/6.0.35 , And i was able to login to https://██████████/manager/html With default credentials `tomcat:tomcat`
See the following Screenshots:-

██████████

███

## Steps To Reproduce:
1. Go To https://███████/manager/html
2. Login with default creds `tomcat:tomcat`

## Supporting Material/References:
- https://book.hacktricks.xyz/pentesting/pentesting-web/tomcat

## Impact

Improper Authentication
Default Credentials lead to access admin manager.

##Fix:-
- Change default creds.

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
