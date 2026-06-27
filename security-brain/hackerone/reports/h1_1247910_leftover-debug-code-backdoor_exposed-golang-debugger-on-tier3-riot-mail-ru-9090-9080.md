---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1247910'
original_report_id: '1247910'
title: Exposed Golang debugger on tier3.riot.mail.ru:9090, 9080
weakness: Leftover Debug Code (Backdoor)
team_handle: mailru
created_at: '2021-06-30T04:44:57.024Z'
disclosed_at: '2022-01-19T07:48:05.699Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- leftover-debug-code-backdoor
---

# Exposed Golang debugger on tier3.riot.mail.ru:9090, 9080

## Metadata

- HackerOne Report ID: 1247910
- Weakness: Leftover Debug Code (Backdoor)
- Program: mailru
- Disclosed At: 2022-01-19T07:48:05.699Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi there, the Golang pprof debug interface is exposed on tier3.riot.mail.ru:9090 (and port 9080). This allows introspection of stack traces, application timing, memory usage, command line parameters, and allows triggering GC pauses, which allows a denial-of-service via repeatedly triggering a garbage collection.

You can see the interface at the following URLs:
* http://tier3.riot.mail.ru:9080/debug/pprof/ (cmdline: `/opt/WWWRoot/zbs-dev/esrv/bin/gameproxy -cfg proxy.yml -pid-file proxy.pid`)
* http://tier3.riot.mail.ru:9090/debug/pprof/ (cmdline: `/opt/WWWRoot/zbs-test/esrv/bin/gameproxy -cfg proxy.yml -pid-file proxy.pid`)

From the Goroutine stack traces, we can see that this is probably something to do with `esrvproxy` or `eproxy`: `/opt/WWWRoot/zbs-test/esrv/eproxy/cmd/esrvproxy/proxy.go`. I will not pretend to know where in your scope this issue is.

## Impact

Denial of service, information disclosure

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
